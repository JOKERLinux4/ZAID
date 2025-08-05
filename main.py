from pyrogram import Client
from config import API_ID, API_HASH, SESSION, DEVELOPER_NAME, DEVELOPER_USER, SOURCE_CHANNEL

# إنشاء الجلسة من معلومات المستخدم
app = Client(
    session_name=SESSION,
    api_id=API_ID,
    api_hash=API_HASH
)

# عند التشغيل
@app.on_message()
def start_handler(client, message):
    if message.text == "/start":
        message.reply_text(
            f"🎯 مرحبًا بك في سورس الشياطين\n\n"
            f"👤 المطور: [{DEVELOPER_NAME}](https://t.me/{DEVELOPER_USER.strip('@')})\n"
            f"📢 القناة: {SOURCE_CHANNEL}"
        )

# بدء التشغيل
print("✅ تم تشغيل الجلسة بنجاح")
app.run()
