from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
# Импортируем нужные компоненты

# Функция, которая соединяется с платформой Telegram, "тело" бота

def main():
    updater = Updater("498747935:AAHANRICU65KYR1E-tcXjpMUMqrj47whGR8")
    dp = updater.dispatcher
#    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_location))
#    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()

#def greet_user(bot, update):
#    text = 'Вызван /start'
#    print(text)
#    update.message.reply_text(text)

#def talk_to_me(bot, update):
#    user_text = update.message.text 
#    print(user_text)
#    update.message.reply_text(user_text)

def planet_location(bot, update):
    planet = 'Вызван /planet'
    planet = update.message.text 
    print(planet)

    #date = datetime.datetime.now()
    #planet = ephem.Mars(date)
    #ephem.Mars()
    #constellation = ephem.constellation(planet)
    #update.message.reply_text(constellation)
    
    solar_system_planet = {"Mercury": ephem.Mercury, "Venus": ephem.Venus, "Earth": ephem.Earth, "Mars": ephem.Mars, "Jupiter": ephem.Jupiter, "Saturn": ephem.Saturn, "Uranus": ephem.Uranus, "Neptune": ephem.Neptune, "Pluto": ephem.Pluto}
    
    date = datetime.datetime.now()
    planet = solar_system_planet.get(planet)
    constellation = planet(date)
    result = ephem.constellation(constellation)    
    update.message.reply_text(result)

# Вызываем функцию - эта строчка запускает бота
main()