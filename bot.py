import os
import threading

from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEB_APP_URL = os.environ.get("WEB_APP_URL")

app = Flask(__name__)

@app.get("/")
def home():
    return """<!doctype html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Walin Fast</title>
<style>
body{margin:0;min-height:100vh;display:grid;place-items:center;background:#11101a;color:white;font-family:Arial,sans-serif;text-align:center}
.box{padding:30px} h1{font-size:36px} p{opacity:.8}
</style>
</head>
<body>
<div class="box"><h1>Walin Fast 🚀</h1><p>Walin Fast Web App is running successfully.</p></div>
</body>
</html>"""

@app.get("/health")
def health():
    return "OK", 200

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton(
            "🚀 Open Walin Fast",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )
    ]]
    await update.message.reply_text(
        "👋 Baga nagaan dhuftan!\n\n"
        "Walin Fast Web App banaachuuf button armaan gadii tuqi:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def run_web():
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port, threaded=True)

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN hin jiru.")
    if not WEB_APP_URL:
        raise RuntimeError("WEB_APP_URL hin jiru.")

    threading.Thread(target=run_web, daemon=True).start()

    bot = Application.builder().token(BOT_TOKEN).build()
    bot.add_handler(CommandHandler("start", start))

    print("Walin Fast Bot started...")
    bot.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
app.run
