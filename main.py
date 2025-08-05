main.py

from pyrogram import Client, filters import os

API_ID = int(os.environ.get("API_ID")) API_HASH = os.environ.get("API_HASH") SESSION = os.environ.get("SESSION")

DEVELOPER_NAME = "قِٰـِۢــآئــد آلِٰـِۢــشِٰـِۢــيِٰـِۢـآطِٰـِۢـيِٰـِـنَ" DEVELOPER_USER = "@X_5NN" SOURCE_CHANNEL = "@C_9KK"

app = Client(name=SESSION, api_id=API_ID, api_hash=API_HASH, session_string=SESSION)

@app.on_message(filters.command("start") & filters.private) def start(client, message): message.reply_text( f"👋 مرحبًا بك في سورس {DEVELOPER_NAME}\n" f"👤 المطور: {DEVELOPER_USER}\n" f"📣 القناة: {SOURCE_CHANNEL}" )

app.run()

