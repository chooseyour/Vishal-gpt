import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import openai

# Set your OpenAI API key securely from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Setup logging for debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! 🤖 I'm VishalGPT. Ask me anything!")

# Message handler to get AI response
async def handle_message
