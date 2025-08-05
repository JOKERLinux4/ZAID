from pyrogram import Client
import asyncio
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION")

DEVELOPER_NAME = "قِٰـِۢــآئــد آلِٰـِۢــشِٰـِۢــيِٰـِۢـآطِٰـِۢـيِٰـِـنَ"
DEVELOPER_USER = "@X_5NN"
SOURCE_CHANNEL = "@C_9KK"

async def main():
    async with Client(name="mybot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION) as app:
        me = await app.get_me()
        print(f"✅ تم تشغيل الجلسة بنجاح: {me.first_name} (@{me.username})")

if __name__ == "__main__":
    asyncio.run(main())
