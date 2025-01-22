from telegram import Update
from telegram.ext import CallbackContext
from app.downloader import download_video
import os

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! Send me an URL to download a YouTube video/audio.')

# Command to download the video
async def dv(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Please, enter the video URL.')
    return 1

# Command to download the audio
async def da(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Please, enter the audio URL.')
    return 1






