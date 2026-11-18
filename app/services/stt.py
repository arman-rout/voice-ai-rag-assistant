#Responsibility: Convert the customer's recorded voice into text using Deepgram.

import httpx

from app.config import DEEPGRAM_API_KEY


async def transcribe_audio(audio_bytes, content_type):

    url = "https://api.deepgram.com/v1/listen"

    params = {
        "model": "nova-3",
        "smart_format": "true"
    }

    headers = {
        "Authorization": f"Token {DEEPGRAM_API_KEY}",
        "Content-Type": content_type
    }

    async with httpx.AsyncClient(timeout=60) as client:

        response = await client.post(
            url,
            params=params,
            headers=headers,
            content=audio_bytes
        )

        response.raise_for_status()

        data = response.json()

    transcript = (
        data["results"]["channels"][0]
        ["alternatives"][0]["transcript"]
    )

    return transcript