from pyrogram import Client, filters
from config import API_ID, API_HASH, SESSION, DEVELOPER_NAME, DEVELOPER_USER, SOURCE_CHANNEL

app = Client(session_name=SESSION, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.command("بدء") & filters.me)
async def welcome(client, message):
    await message.reply_text(
        f"أهلاً بك في السورس!\n\n"
        f"المطور: [{DEVELOPER_NAME}](https://t.me/{DEVELOPER_USER.strip('@')})\n"
        f"القناة: {SOURCE_CHANNEL}"
    )

app.run()