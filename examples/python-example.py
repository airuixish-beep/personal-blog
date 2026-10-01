"""Minimal AI API learning example.

This example intentionally uses a placeholder endpoint so beginners can study
the request pattern without exposing real credentials.
"""

import os
import requests

API_URL = os.getenv("AI_API_URL", "https://example.com/v1/chat")
API_KEY = os.getenv("AI_API_KEY")

if not API_KEY:
    raise RuntimeError("Set AI_API_KEY in your environment before running this example.")

payload = {
    "model": "example-model",
    "messages": [
        {"role": "user", "content": "Explain tokens in simple language."}
    ],
}

response = requests.post(
    API_URL,
    headers={"Authorization": f"Bearer {API_KEY}"},
    json=payload,
    timeout=30,
)
response.raise_for_status()
print(response.json())
