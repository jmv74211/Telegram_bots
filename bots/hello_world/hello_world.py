import telebot     # Biblioteca para usar la API de telegram
import os          # Para utilizar las variables de entorno del sistema.

TOKEN = os.environ['TELEGRAM_TOKEN']

# Creamos la instancia del bot
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # Obtenemos el identificador del usuario
    chat_id = message.chat.id
    # Se envía el mensaje a dicho usuario
    bot.send_message(chat_id, "Hola mundo!")


# Será llamado si no se ha llamado a ningún otro método
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    # Obtenemos el identificador del usuario
    chat_id = message.chat.id
    # Se envía el mensaje a dicho usuario
    bot.send_message(chat_id, "Este bot solo funciona con los comandos /start y /help")

print("El bot se está ejecutando!")

# Ejecutamos el programa
bot.polling()
