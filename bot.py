import telebot
import config



bot = telebot.TeleBot(config.token)
id = '-1001463284489'
@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    bot.send_message('-1001463284489', 'example')

bot.send_photo('-1001463284489', 'https://apod.nasa.gov/apod/image/2006/EuropaJupiter_Voyager_2792.jpg')

if __name__ == '__main__':
    bot.infinity_polling()
