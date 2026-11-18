#Responsibility: Convert Gemini's answer into spoken audio.

import httpx

from app.config import (
    ELEVENLABS_API_KEY,
    ELEVENLABS_VOICE_ID
)


async def generate_speech(text):

    url = (
        "https://api.elevenlabs.io/v1/text-to-speech/"
        f"{ELEVENLABS_VOICE_ID}"
    )

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "model_id": "eleven_turbo_v2_5"
    }

    async with httpx.AsyncClient(timeout=60) as client:

        response = await client.post(
            url,
            headers=headers,
            json=payload
        )

        response.raise_for_status()

        return response.content