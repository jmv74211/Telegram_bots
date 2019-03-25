# Botones desde el teclado

En este ejemplo, se ha realizado un pequeño bot para mostrar cómo se implementaría la funcionalidad de añadir botones tanto en el teclado del usuario, como en los mensajes enviados por el bot.

Para poder usar los botones en el teclado del usuario, se ha añadido clase `ReplyKeyboardMarkup`, y para los botones dentro de los mensajes se ha utilizado la clase `InlineKeyboardMarkup` dentro del paquetes `types`de pyTelegramBotAPI.

## ReplyKeyboardMarkup

El constructor de `ReplyKeyboardMarkup` puede tomar los siguientes argumentos:
 - **resize_keyboard:** True/False (default False)
 - **one_time_keyboard:** True/False (default False)
 - **selective:** True/False (default False)
 - **row_width:** integer (default 3)

Podemos estructurar dichos botones de dos formas: asignando un número **fijo o variable** de botones por fila.

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

El envío de la agrupación de dichos botones se tiene que hacer en el mensaje.

      bot.send_message(chat_id, "Elige uno:", reply_markup=markup1)

El resultado sería el siguiente:

- `/a`

![ex1](https://raw.githubusercontent.com/jmv74211/Telegram_bots/master/images/bots/keyboards_test/ex1.png)

- `/b`

![ex1](https://raw.githubusercontent.com/jmv74211/Telegram_bots/master/images/keyboards_test/buttons/ex2.png)

## InlineKeyboardMarkup

El constructor de `InlineKeyboardMarkup` puede tomar los siguientes argumentos:
 - **row_width:** integer (default 3)

Podemos estructurar dichos botones de dos formas: asignando un número **fijo o variable** de botones por fila.

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

Como se puede observar en el ejemplo anterior, se pueden asignar un `data_callback` al botón para poder gestionarlo:

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

El resultado sería el siguiente:

![ex3](https://raw.githubusercontent.com/jmv74211/Telegram_bots/master/images/keyboards_test/buttons/ex3.png)

![ex4](https://raw.githubusercontent.com/jmv74211/Telegram_bots/master/images/keyboards_test/buttons/ex4.png)

# Referencias

[1] How to create a telegram bot from scratch (tutorial), disponible en: https://www.smartspate.com/how-to-create-a-telegram-bot-from-scratch-tutorial/

[2] Github pyTelegramBotAPI, disponible en: https://github.com/eternnoir/pyTelegramBotAPI#methods

[3] https://github.com/eternnoir/pyTelegramBotAPI/blob/master/telebot/types.py

[4] https://core.telegram.org/bots/api
