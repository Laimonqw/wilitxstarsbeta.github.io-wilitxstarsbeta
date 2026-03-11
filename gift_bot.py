import telebot

# Initialize the bot with your token
token = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(token)

# Command to start the bot
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Welcome to the NFT Gift Bot!')

# Command to gift an NFT
@bot.message_handler(commands=['gift'])
def gift_nft(message):
    bot.send_message(message.chat.id, 'You have received an NFT!')

# Start the bot
bot.polling()