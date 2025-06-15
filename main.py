import os
import telebot
import openai

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda m: True)
def reply(m):
    try:
        r = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":m.text}]
        )
        bot.reply_to(m, r.choices[0].message.content)
    except Exception as e:
        bot.reply_to(m, f"Error: {e}")

if __name__ == "__main__":
    bot.infinity_polling()
add main file
