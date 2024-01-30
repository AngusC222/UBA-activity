# https://discord.com/api/v9/channels/974808765046067281/messages?limit=100
import requests
import asyncio
import json
import os
from dotenv import load_dotenv

load_dotenv()

async def fetchMessages():
    url = "https://discord.com/api/v9/channels/974808765046067281/messages?limit=100"
    headers = {
        "User-Agent": os.getenv("User-Agent"),
        "Accept": os.getenv("Accept"),
        "Accept-Language": "en-GB,en;q=0.5",
        "Authorization": os.getenv("Authorization"),
        "X-Super-Properties": os.getenv("X-Super-Properties"),
        "X-Discord-Locale": os.getenv("X-Discord-Locale"),
        "X-Discord-Timezone": os.getenv("X-Discord-Timezone"),
        "X-Debug-Options": os.getenv("X-Debug-Options"),
        "Alt-Used": os.getenv("Alt-Used"),
        "Sec-Fetch-Dest": os.getenv("Sec-Fetch-Dest"),
        "Sec-Fetch-Mode": os.getenv("Sec-Fetch-Mode"),
        "Sec-Fetch-Site": os.getenv("Sec-Fetch-Site")
    }

    return json.loads(requests.get(url, headers=headers).content)
