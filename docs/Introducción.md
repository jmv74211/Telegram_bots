# 1. Introducción

Aunque actualmente existen infinidad de bots para diferentes plataformas, este proyecto  se  va  a  centrar  en  los  bots  de Telegram,que son  aplicaciones  de terceros que se ejecutan dentro de Telegram.

La  comunicación  con  los  servidores  se  hace  a  través  de  una  sencilla  interfaz HTTPS (Hypertext Transfer Protocol Secure) que ofrece una versión simplificada de la API de Telegram. Se llama a esa interfaz API de BOT.

# 2. BOT DE TELEGRAM

Los usuarios pueden interactuar con éstos enviándoles mensajes, comandos y solicitudes en línea, se controlan mediante llamadas HTTPS a la API de BOT de Telegram, esto es lo que se conoce como WebHook, es decir, callbackHTTPS de usuario.

Para que los servidores de Telegram conozcan la dirección del servidor externo donde  está  alojado el  bot y su  TOKEN  (identificador  utilizado  para  facilitar  el proceso de autenticación),es necesario enviar un WebHook a la API deBOT con la URI (Uniform Resource Identifier) del servidor externo, junto con el  TOKEN del bot.La petición HTTPSquedaría de la siguiente manera:

      https://api.telegram.org/bot[TOKEN]/setWebhook?url=[URL]

Los  bots de Telegram  son  cuentas  especiales  que no  necesitan un número  de teléfono que configurar.

Para enviar mensajes y comandos a los bots se abre un chat con ellos, también se pueden enviar solicitudes desde el campo de entrada escribiendo el nombre de usuario del bot y la consulta a realizar, paraesto es necesario que sea un tipo de bot especial llamado **“inline bot”**.

Los mensajes,comandos y peticiones enviadas por los usuarios se procesan en el software que se ejecuta en los servidores de Telegram. El intercambio de datos entre los servidores de Telegram y el servidor externo donde está alojado el bot se hace en formato **JSON(JavaScript Object Notation)**, un formato de texto ligero para el intercambio de datos que describe éstos con una sintaxis dedicada que se usa para identificarlos y gestionarlos.

Los servidores manejan todo el cifrado y la comunicación con la API de Telegram de  una  manera  transparente,  por  lo  que  **no  es  necesario  encargarse  de  la seguridad**.

Ejemplos de bots de telegram:

- **Gmail bot:** Bot mediante el cual se pueden enviar y recibir emails, descargar archivos adjuntos y documentos.

- **TweetItBot:** Es  capaz  de  enviar  y  borrar  tuits,  retuitear,  marcar  favoritos  y publicar imágenes.

- **BabelGram:** Sirve  para traducir  fragmentos  de  texto,  funciona  enviando `@BabelgramBot [idioma] [idioma] [texto]`.

- **GameBot:** Es un conjunto de minijuegos desarrollados en HTML5 adaptados para jugar en dispositivos móviles.
