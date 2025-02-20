import asyncio
import os

from pyrogram import Client, filters
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "123456"))  # Default for safety
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

DELETE_DELAY = int(os.getenv("DELETE_DELAY", "2"))  # Time before deletion

app = Client("bot_session", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


async def delete_message_with_delay(message):
    try:
        await asyncio.sleep(DELETE_DELAY)
        await message.delete()
    except Exception as e:
        print(f"Failed to delete message: {e}")


@app.on_message(filters.me)
async def delete_own_messages(client, message):
    await delete_message_with_delay(message)


@app.on_edited_message(filters.me)
async def delete_own_edited_messages(client, message):
    await delete_message_with_delay(message)


if __name__ == "__main__":
    print("Bot is running...")
    app.run()
