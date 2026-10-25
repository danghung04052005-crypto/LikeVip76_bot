import os
import telebot

bot = telebot.TeleBot(os.environ["BOT_TOKEN"])

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "💎 Chào mừng đến LikeVip76!\nGõ /help để xem lệnh.")

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(message, "/likes - Dịch vụ\n/price - Bảng giá\n/contact - Hỗ trợ\n/5 - Tạo team 5")

@bot.message_handler(commands=["likes", "price", "contact", "5"])
def other(message):
    bot.reply_to(message, "💎 LikeVip76 Bot đang hoạt động!")

bot.infinity_polling()
