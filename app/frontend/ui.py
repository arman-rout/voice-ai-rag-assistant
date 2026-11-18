"""This gives you a browser interface where customers can type questions or record their voices.

It also prevents the same recorded audio from being processed repeatedly when Streamlit reruns."""

import asyncio
import hashlib

import streamlit as st

from app.main import VoiceRAGAgent

from app.services.stt import transcribe_audio
from app.services.tts import generate_speech


st.set_page_config(
    page_title="Voice AI RAG Assistant",
    page_icon="🎙️",
    layout="centered"
)

st.title("Voice AI + RAG Assistant")

st.write(
    "Ask questions about the company using your voice or text."
)


@st.cache_resource
def load_agent():
    return VoiceRAGAgent()


agent = load_agent()


if "history" not in st.session_state:
    st.session_state.history = []

if "last_audio_hash" not in st.session_state:
    st.session_state.last_audio_hash = None


# Display conversation history
for item in st.session_state.history:

    with st.chat_message("user"):
        st.write(item["question"])

    with st.chat_message("assistant"):

        st.write(item["answer"])

        if item.get("audio"):
            st.audio(
                item["audio"],
                format="audio/mpeg"
            )

        if item.get("sources"):

            with st.expander("Retrieved sources"):

                for source in item["sources"]:

                    st.write(
                        f"- {source['source']}"
                    )


question = st.chat_input(
    "Ask your company-related question..."
)

audio_file = st.audio_input(
    "Or record your voice"
)


if question:

    try:

        with st.spinner("Gemini is thinking..."):

            result = agent.ask(question)

            answer = result["answer"]

            audio_bytes = asyncio.run(
                generate_speech(answer)
            )

        st.session_state.history.append({
            "question": question,
            "answer": answer,
            "audio": audio_bytes,
            "sources": result["sources"]
        })

        st.rerun()

    except Exception as error:

        st.error(f"Error: {error}")


elif audio_file:

    audio_bytes = audio_file.getvalue()

    audio_hash = hashlib.sha256(
        audio_bytes
    ).hexdigest()

    if audio_hash != st.session_state.last_audio_hash:

        try:

            st.session_state.last_audio_hash = audio_hash

            with st.spinner("Converting your voice into text..."):

                transcript = asyncio.run(
                    transcribe_audio(
                        audio_bytes,
                        audio_file.type or "audio/webm"
                    )
                )

            if not transcript.strip():

                st.warning("I could not recognize your speech.")

            else:

                st.write(f"**You said:** {transcript}")

                with st.spinner("Searching company knowledge..."):

                    result = agent.ask(transcript)

                    answer = result["answer"]

                    audio_response = asyncio.run(
                        generate_speech(answer)
                    )

                st.session_state.history.append({
                    "question": transcript,
                    "answer": answer,
                    "audio": audio_response,
                    "sources": result["sources"]
                })

                st.rerun()

        except Exception as error:

            st.error(f"Error: {error}")