import telebot
import os
import json
from datetime import datetime

TOKEN = os.getenv("ANALYTICS_BOT_TOKEN")  # এটা আলাদা বটের টোকেন হবে
bot = telebot.TeleBot(TOKEN, parse_mode="MarkdownV2")

STATS_FILE = "stats.json"

def load_stats():
    try:
        with open(STATS_FILE, "r") as f:
            return json.load(f)
    except:
        return {"users": [], "tasks": 0, "notes": 0}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
        "👋 Ahad Analytics Bot এ আপনাকে স্বাগতম!\n\n"
        "বট চালু থাকলে /stats দিয়ে To-Do Bot এর লাইভ স্ট্যাটাস দেখুন।"
    )

@bot.message_handler(commands=['stats'])
def stats(message):
    stats = load_stats()
    users = len(stats.get("users", []))
    tasks = stats.get("tasks", 0)
    notes = stats.get("notes", 0)
    now = datetime.now().strftime("%Y-%m-%d %I:%M %p")

    text = (
        f"📊 *Ahad To-Do Bot Report*\n\n"
        f"👥 মোট ব্যবহারকারী: *{users}* জন\n"
        f"📝 মোট টাস্ক: *{tasks}* টি\n"
        f"🗒️ মোট নোট: *{notes}* টি\n\n"
        f"📅 আপডেটেড: `{now}`"
    )
    bot.reply_to(message, text)

bot.infinity_polling()
