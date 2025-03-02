import os
import httpx
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackContext,
    ConversationHandler,
    filters
)
from utils.downloader import download_media
from utils.stream import get_stream_url
from utils.converter import (
    convert_to_hls,
    convert_to_ogg
)


load_dotenv()

## Global vars
TOKEN = os.getenv('TELEGRAM_TOKEN')
ASK_URL = 1


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "#---- YouTube Bot Streaming ----#\n\n"
        "[*] Commands availables:\n"
        "/dv - Download video\n"
        "/da - Download audio\n"
        "/cancel - Cancel operation" 
    )

async def dv(update: Update, context: CallbackContext) -> int:
    context.user_data["media_type"] = "video"
    await update.message.reply_text("Send the YouTube video URL!")
    return ASK_URL

async def da(update: Update, context: CallbackContext) -> int:
    context.user_data["media_type"] = "audio"
    await update.message.reply_text("Send the YouTube audio URL!")
    return ASK_URL

async def process_url(update: Update, context: CallbackContext) -> int:
    url = update.message.text
    media_type = context.user_data.get("media_type","video")
    print(f"DEBUG - media_type: {media_type}")

    try:
        download_data = await download_media(url, media_type)
        if not download_data:
            print("Debugging errors1")
            raise Exception("Download error.")
        
        if media_type == "video":
            print("enter if")
            converted_path = await convert_to_hls(download_data["path"])
        else:
            converted_path = await convert_to_ogg(download_data["path"])

        stream_url = get_stream_url(converted_path, media_type)

        await update.message.reply_text(
            f"** {download_data['title']} **\n"
            f"Stream url:\n{stream_url}"
        )
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")
        return ConversationHandler.END

    return ConversationHandler.END

async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text("Operation canceled")
    return ConversationHandler.END

def main():
    app = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("dv", dv),
            CommandHandler("da", da)
        ],
        states={
            ASK_URL: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_url)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True
    )

    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == "__main__":
    main()