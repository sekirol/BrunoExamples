
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Определения имён используемых файлов
ACCESS_FILE_NAME = 'botAccess.txt'
HELP_FILE_NAME = 'botHelp.txt'

# Бот имеет базу слов, которые польззователю необходимо выучить
# Бот периодически просит пользователя ввести перевод слова (перевести на английский или русский)
# Пользователь может пополнять базу слов, парами слово-перевод
# -- Для добавления слова в базу используется команда add_word

# Обработчик команды '/help'
def getInstruction(update, context):
    helpData = None
    
    try:
        with open(HELP_FILE_NAME, 'r', encoding='utf-8') as helpFile:
            helpData = helpFile.read()
    except:
        pass

    if helpData:
        context.bot.send_message(update.effective_chat.id, text=helpData)
    else:
        errorMessage = "Инструкция не определена"
        logMessage(context, update.effective_chat.id, errorMessage)
           
# Обработчик сообщения пользователя
def addWordToBase(update, context):
    userMessage = update.message.text
    
    word = None
    translate = None
    
    try:
        word, translate = [subStr.strip() for subStr in userMessage.split('=')]
    except:
        pass
        
    if word and translate:
        logMessage(context, update.effective_chat.id, "Слово {} добавлено в словарь с переводом {}.".format(word, translate))
    else:
        logMessage(context, update.effective_chat.id, "Сообщение не соответствует шаблону для добавления слов. Воспользуйтесь /help.")
        
# Функция для отправки служебных сообщений в чат
def logMessage(context, chatId, messageText):
    context.bot.send_message(chat_id=chatId, text=messageText)

# Функция открытия файла и чтения токена доступа
def getAccessToken():
    accessToken = None
    
    try:
        with open(ACCESS_FILE_NAME, 'r', encoding='utf-8') as accFile:
            accessToken = accFile.read()
    except:
        pass
    
    return accessToken
    
accessToken = getAccessToken()
if accessToken:
    updaterObj = Updater(accessToken, use_context=True)
    dispatcherObj = updaterObj.dispatcher

    dispatcherObj.add_handler(CommandHandler("help", getInstruction))
    dispatcherObj.add_handler(MessageHandler(Filters.all, addWordToBase))

    print('Сервер запущен')
    
    updaterObj.start_polling()
    updaterObj.idle()
else:
    print('Ошибка чтения AccessToken')