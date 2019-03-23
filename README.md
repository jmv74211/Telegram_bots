# Telegram bots con python
## Autor: Jonathan Martín Valera
### Fecha de realización: Marzo 2019

---

![Status](https://img.shields.io/badge/language-Python-yellow.svg)
![Status](https://img.shields.io/badge/library-pyTelegramBotAPI-blue.svg)
![Status](https://img.shields.io/badge/Status-building-red.svg)

![logo](https://raw.githubusercontent.com/jmv74211/Telegram_bots/master/images/logo.png)

---

# Telegram

Telegram  es  un  servicio  de  mensajería  por Internet desarrollado  desde  el año 2013 por los hermanos Nikolai y Pavel Durov. El servicio está enfocado en la gestión  de mensajes  de  texto  y  multimedia,inicialmente  fue  empleado  para teléfonos móviles y el año siguiente para multiplataforma.

## API de telegram

La API de Bot está formada por una serie de URI’s a través de las cuales se envían y reciben datos de una conversación de Telegram.

La  comunicación  entre  el  bot  y  la  API  se  hace  a  través  del  lenguaje  de marcado **JSON**.

El primer paso para programar un bot es obtener un **token**, es decir, un identificador que Telegram le asigna al bot.

Las URI’s están formadas por:

- Protocolo a utilizar: `https://`
- Servidor de la API de Telegram Bot: `api.telegram.org/`
- La palabra “bot” seguida del token asignado al registro: `Bot23453242:SSASKMffdsUIOdfDNBVTYdoopfdbydDINFhb`
- El comando que se solicite.

Telegram hace de intermediario entre el usuario y el bot, encriptando la transmisión  con  su  protocolo  MTProto.  Dicho  protocolo  encripta los mensajes simétricamente con *AES-256* y la clave compartida está firmada en *SHA-1*.

## Bots

### BotFather

@BotFather, es un bot que sirve para crear y administrar bots.Para crear un bot se inicia una conversación con el: https://telegram.me/botfather

![botFather](https://raw.githubusercontent.com/jmv74211/Telegram_bots/master/images/bot_father.png)


### Creación de un bot

Una vez estemos en la conversación con botFather (ver figura anterior),  se escribe el comando `/newbot` y se asigna el nombre al bot.

Seguidamente se introduceel nombrede usuario para el bot, éste tiene que  terminar  obligatoriamente  en  bot,  porejemplo  TetrisBot  o tetris_bot. Este nombre, a diferencia del anterior **no puede ser modificado**.

Una vez asignados estos dos nombres BotFatherproporcionará un **token**, el cual se guardaráporqueservirá para identificar al bot.

**Introducción y ejemplos bots de telegram**

Para ver una pequeña introducción a los bots de telegram y algunos ejemplos de uso más corrientes se puede visitar este **[enlace](https://github.com/jmv74211/Telegram_bots/blob/master/docs/Introducci%C3%B3n.md)**

**Configuración del bot y comunicación con el usuario**

Para ver los posibles comandos de configuración se puede consultar este **[enlace](https://github.com/jmv74211/Telegram_bots/blob/master/docs/Configuraci%C3%B3n_bot.md)**.

### ¿Cuál es su función real?

 - **Recibe notificaciones y noticias personalizadas**. Un bot puede actuar como un periódico inteligente, enviándole contenido relevante tan pronto como se publique.

 - **Integrar con otros servicios**. Un robot puede enriquecer los chats de Telegram con contenido de servicios externos.

 - **Acepte pagos de los usuarios de Telegram**. Un bot puede ofrecer servicios pagados o trabajar como una tienda virtual.

 - **Crea herramientas personalizadas**. Un bot puede proporcionarle alertas, pronósticos del tiempo, traducciones, formato u otros servicios.

 - **Compila juegos de un solo jugador y multijugador**. Un robot puede ofrecer experiencias ricas en HTML5, desde simples arcades y acertijos hasta tiradores 3D y juegos de estrategia en tiempo real.

 - **Construye servicios sociales**. Un bot podría conectar a las personas que buscan interlocutores basados ​​en intereses comunes o proximidad.

### Tipos de bots

Hay dos tipos de bots en Telegram: los **bots normales** y los llamados **“Inline”**.

Para utilizar los **bots normales** tenemos que abrir un chat con ellos o incluirlos en el grupo donde queramos utilizarlo, pudiendo utilizarlo todas las veces que queramos, utilizando normalmente la típica sintaxis de `/` seguido del comando, ejemplo: `/tiempo`.

Por otro lado, los **Inline Bots** están disponible desde principios del año 2016 y la diferencia es en que no necesitamos incluirlos en ninguna grupo para usarlos. Los podemos utilizar en cualquier momento, simplemente tendremos que añadir una arroba con su nombre a la hora de escribir un nuevo mensaje para poder empezar a utilizarlos. Los resultados que nos ofrezcan aparecerán en un menú flotante dentro de la misma conversación y podremos elegir el resultado que más nos guste para mostrar al resto de miembros de dicha conversación.

## Arquitectura

Los usuarios pueden interactuar con éstos enviándoles mensajes, comandos y solicitudes en línea, se controlan mediante llamadas HTTPS a la API de BOT de Telegram, esto es lo que se conoce como **WebHook**, es decir, callbackHTTPS de usuario.

Para que los servidores de Telegram conozcan la dirección del servidor externo donde  está  alojado el  bot y su  TOKEN  (identificador  utilizado  para  facilitar  el proceso de autenticación),es necesario enviar un WebHook a la API deBOT con la URI (Uniform Resource Identifier) del servidor externo, junto con el  TOKEN del bot.La petición HTTPSquedaría de la siguiente manera:

      https://api.telegram.org/bot[TOKEN]/setWebhook?url=[URL]

Los mensajes,comandos y peticiones enviadas por los usuarios se procesan en el software que se ejecuta en los servidores de Telegram. El intercambio de datos entre los servidores de Telegram y el servidor externo donde está alojado el bot se hace en formato **JSON(JavaScript Object Notation)**, un formato de texto ligero para el intercambio de datos que describe éstos con una sintaxis dedicada que se usa para identificarlos y gestionarlos.

La siguiente figura muestra el flujo de información que se produce en la comunicación:

![arquitectura](https://raw.githubusercontent.com/jmv74211/Telegram_bots/master/images/arquitectura.png)
---

# Referencias

[1] Github pyTelegramBotAPI disponible en https://github.com/eternnoir/pyTelegramBotAPI

[2] Álvaro Cubillo Pascual, Jesús Daniel Trigo Vilaseca, Victoria Duro Suárez, 2017-06-28, TFG: DESARROLLO DE UN JUEGO DE PREGUNTAS BASADO EN UN BOT ENFOCADO A LA EDUCACIÓN EN SALUD, disponible en : https://academica-e.unavarra.es/bitstream/handle/2454/24669/Memoria%20TFG.pdf?sequence=1&isAllowed=y
