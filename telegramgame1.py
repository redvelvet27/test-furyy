import telebot
from telebot import types

# Your bot API token
TOKEN = '8124406610:AAHNyicYAFYi2NlQuRsSQors6FMjek4eLfE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'play'])
def send_game_button(message):
    markup = types.InlineKeyboardMarkup()
    # Create the button with your game's URL
    game_button = types.InlineKeyboardButton(text="Play the Game", url='https://gorgeous-swan-b7d07d.netlify.app/')
    markup.add(game_button)

    # Send the button to the user
    bot.send_message(chat_id=message.chat.id, text="Click the button below to play the game:", reply_markup=markup)

bot.polling()