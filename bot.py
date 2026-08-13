import os
import threading

from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get(8885427769:AAEBm0aJwcGqIT7kpwCyUxqdEPxzGBAxgQQ")
WEB_APP_URL = os.environ.get("https://walinfast.onrender.com")

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Walin Fast</title>
    </head>
    <body>
        <h1>Walin Fast</h1>
        <p>Welcome to Walin Fast Web App!</p>
    </body>
    </html>
    """


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 Open Walin Fast",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ]

    await update.message.reply_text(
        "👋 Baga nagaan dhuftan!\n\n"
        "Walin Fast Web App banuuf button armaan gadii tuqi:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN hin jiru.")
    if not WEB_APP_URL:
        raise ValueError("WEB_APP_URL hin jiru.")

    threading.Thread(target=run_web, daemon=True).start()

    bot = Application.builder().token(8885427769:AAEBm0aJwcGqIT7kpwCyUxqdEPxzGBAxgQQ).build()
    bot.add_handler(CommandHandler("start", start))

    print("Walin Fast Bot started...")
    bot.run_polling()


if __name__ == "__main__":
    main()
