import telebot     # Biblioteca para usar la API de telegram
import os          # Para utilizar las variables de entorno del sistema.
from telebot import types # Import para los botones

TOKEN = os.environ['TELEGRAM_TOKEN']

# Creamos la instancia del bot
bot = telebot.TeleBot(TOKEN)

###################################################################
#                                                                 #
#                    ReplyKeyboardMarkup                          #
#                                                                 #
###################################################################

# Usando la ReplyKeyboardMarkup class
# Su constructor puede tomar los siguientes argumentos:
# - resize_keyboard: True/False (default False)
# - one_time_keyboard: True/False (default False)
# - selective: True/False (default False)
# - row_width: integer (default 3)

## FORMA 1: Se definen cuantos botones se van a usar por fila

# Creamos el grupo de botones
reply_keyboard_markup = types.ReplyKeyboardMarkup(  row_width = 2,
                                                    resize_keyboard = True,
                                                    one_time_keyboard = False,
                                                    selective = False,
                                                 )
# Creamos los botones
reply_keyboard_markup_btn1 = types.KeyboardButton('Botón-1')
reply_keyboard_markup_btn2 = types.KeyboardButton('Botón-2')

# Añadimos los botones al grupo
reply_keyboard_markup.add(reply_keyboard_markup_btn1,reply_keyboard_markup_btn2)

###################################################################

## FORMA 2: Se definen los botones y se asocian a las filas

reply_keyboard_markup2 = types.ReplyKeyboardMarkup()
reply_keyboard_markup2_btn1 = types.KeyboardButton('a')
reply_keyboard_markup2_btn2 = types.KeyboardButton('b')
reply_keyboard_markup2_btn3= types.KeyboardButton('c')
reply_keyboard_markup2_btn4 = types.KeyboardButton('d')
reply_keyboard_markup2_btn5= types.KeyboardButton('e')

reply_keyboard_markup2 .row(reply_keyboard_markup2_btn1,reply_keyboard_markup2_btn2)
reply_keyboard_markup2 .row(reply_keyboard_markup2_btn3, reply_keyboard_markup2_btn4,
                            reply_keyboard_markup2_btn5)

###################################################################

# Referencia https://core.telegram.org/bots/api#inlinekeyboardmarkup

###################################################################
#                                                                 #
#                    InlineKeyboardMarkup()                       #
#                                                                 #
###################################################################

## FORMA 1: Se definen cuantos botones se van a usar por fila

inline_keyboard_markup = types.InlineKeyboardMarkup()
inline_keyboard_markup.add(  types.InlineKeyboardButton("Primer botón", callback_data="a"),
                             types.InlineKeyboardButton("Segundo botón", callback_data="b"),
                             types.InlineKeyboardButton("Botón URL", url="https://core.telegram.org/bots/api#inlinekeyboardmarkup"),
                             types.InlineKeyboardButton("Cuarto botón", callback_data="c"),
                             types.InlineKeyboardButton("Quinto botón", callback_data="d"),
                          )

## FORMA 2: Se definen los botones y se asocian a las filas

inline_keyboard_markup2  = types.InlineKeyboardMarkup()
inline_keyboard_markup2_btn1 =  types.InlineKeyboardButton("Contenido del primer botón", callback_data="a")
inline_keyboard_markup2_btn2 =  types.InlineKeyboardButton("Botón enlace ", url="https://core.telegram.org/bots/api#inlinekeyboardmarkup")
inline_keyboard_markup2_btn3 =  types.InlineKeyboardButton("Contenido del tercer botón", callback_data="b")
inline_keyboard_markup2.row(inline_keyboard_markup2_btn1)
inline_keyboard_markup2.row(inline_keyboard_markup2_btn2)
inline_keyboard_markup2.row(inline_keyboard_markup2_btn3)

#####################################################
#           GESTIÓN DE MENSAJES

@bot.message_handler(commands=['a'])
def start1(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Elige uno:", reply_markup=reply_keyboard_markup)

@bot.message_handler(commands=['b'])
def start2(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Elige uno:", reply_markup=reply_keyboard_markup2)

@bot.message_handler(commands=['c'])
def start3(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Elige uno:", reply_markup=inline_keyboard_markup)

@bot.message_handler(commands=['d'])
def start4(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Elige uno:", reply_markup=inline_keyboard_markup2)

#####################################################
#           GESTIÓN DE CALLBACKS

@bot.callback_query_handler(lambda query: query.data == "a")
def process_callback_1(query):
  chat_id = query.message.chat.id
  bot.send_message(chat_id, "Se ha pulsado el botón!")

@bot.callback_query_handler(lambda query: query.data in ["b", "c","d"])
def process_callback_2(query):
    chat_id = query.message.chat.id
    bot.send_message(chat_id, "Se ha pulsado el otro botón!")

#####################################################

print("El bot se está ejecutando!")

# Ejecutamos el programa
bot.polling()
