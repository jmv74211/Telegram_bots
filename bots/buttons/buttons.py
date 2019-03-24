import telebot     # Biblioteca para usar la API de telegram
import os          # Para utilizar las variables de entorno del sistema.
from telebot import types # Import para los botones

TOKEN = os.environ['TELEGRAM_TOKEN']

# Creamos la instancia del bot
bot = telebot.TeleBot(TOKEN)

# Usando la ReplyKeyboardMarkup class
# Su constructor puede tomar los siguientes argumentos:
# - resize_keyboard: True/False (default False)
# - one_time_keyboard: True/False (default False)
# - selective: True/False (default False)
# - row_width: integer (default 3)

###################################################################

## FORMA 1: Se definen cuantos botones se van a usar por fila

# Creamos el grupo de botones
markup1 = types.ReplyKeyboardMarkup(row_width = 2,
                                    resize_keyboard = True,
                                    one_time_keyboard = False,
                                    selective = False,
                                    )
# Creamos los botones
markup1_btn1 = types.KeyboardButton('Botón-1')
markup1_btn2 = types.KeyboardButton('Botón-2')

# Añadimos los botones al grupo
markup1.add(markup1_btn1,markup1_btn2)

###################################################################

## FORMA 2: Se definen los botones y se asocian a las filas

markup2 = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('a')
btn2 = types.KeyboardButton('v')
btn3= types.KeyboardButton('c')
btn4 = types.KeyboardButton('d')
btn5= types.KeyboardButton('e')
markup2.row(btn1, btn2)
markup2.row(btn3, btn4, btn5)

###################################################################

@bot.message_handler(commands=['start1'])
def start1(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Elige uno:", reply_markup=markup1)

@bot.message_handler(commands=['start2'])
def start1(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Elige uno:", reply_markup=markup2)

print("El bot se está ejecutando!")

# Ejecutamos el programa
bot.polling()
