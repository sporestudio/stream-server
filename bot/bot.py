from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, ConversationHandler, filters
import os

load_dotenv()

# State of the conversation
ASK_URL = 1