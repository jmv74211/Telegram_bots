# Botones desde el teclado

En este ejemplo, se ha realizado un pequeño bot para mostrar cómo se implementaría la funcionalidad de añadir botones de selección en el teclado del usuario.

Para ello se ha usado la clase `ReplyKeyboardMarkup` de pyTelegramBotAPI.

Su constructor puede tomar los siguientes argumentos:
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

- `/start1`

![ex1](https://raw.githubusercontent.com/jmv74211/Telegram_bots/master/images/bots/buttons/ex1.png)

- `/start2`

![ex1](https://raw.githubusercontent.com/jmv74211/Telegram_bots/master/images/bots/buttons/ex2.png)


# Referencias

[1] How to create a telegram bot from scratch (tutorial), disponible en: https://www.smartspate.com/how-to-create-a-telegram-bot-from-scratch-tutorial/

[2] Github pyTelegramBotAPI, disponible en: https://github.com/eternnoir/pyTelegramBotAPI#methods
