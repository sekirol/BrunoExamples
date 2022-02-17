
from random import choice
from shutil import which
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Определения имён используемых файлов
ACCESS_FILE_NAME = 'botAccess.txt'
HELP_FILE_NAME = 'botHelp.txt'
BASE_FILE_NAME = 'wordBase.txt'
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
        errorMessage = "Данные документации отсутствуют"
        logMessage(context, update.effective_chat.id, errorMessage)
           
# Обработчик сообщения пользователя
def userMessageHandler(update, context):
    userMessage = update.message.text
    
    word = None
    translate = None
    try:
        word, translate = [subStr.strip() for subStr in userMessage.split('=')]
    except:
        pass
        
    if word and translate:
        try:
            addWordToBase(word, translate)
            logMessage(context, update.effective_chat.id, "Слово {} добавлено в словарь с переводом {}.".format(word, translate))
        except:
            logMessage(context, update.effective_chat.id, "Ошибка открытия базы слов.")
    else:
        logMessage(context, update.effective_chat.id, "Сообщение не соответствует шаблону для добавления слов. Воспользуйтесь /help.")
        
# Функция для отправки служебных сообщений в чат
def logMessage(context, chatId, messageText):
    context.bot.send_message(chat_id=chatId, text=messageText)

def addWordToBase(word1, word2):
    wordsPairString = '{}:{}\n'.format(word1, word2)
    #baseString = ':'.join(word1, word2) + '\n'

    with open(BASE_FILE_NAME, 'a', encoding='utf-8') as basef:
        basef.write(wordsPairString)

def getRandomWordFromBase():
    wordsPairsList = []
    with open(BASE_FILE_NAME, 'r', encoding='utf-8') as basef:
        for pair in basef:
            word1, word2 = pair.strip().split(':')
            wordsPairsList.append({word1:word2})
    
    return choice(wordsPairsList)

def sendWordForTrain(context: CallbackContext):
    trainPair = getRandomWordFromBase()
    word1, word2 = list(trainPair.items())[0]
    context.bot.send_message(chat_id=487841046, text=word1)

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
    dispatcherObj.add_handler(MessageHandler(Filters.all, userMessageHandler))
    dispatcherObj.job_queue.run_repeating(sendWordForTrain, interval=2, first=2)

    print('Сервер запущен')
    
    updaterObj.start_polling()
    updaterObj.idle()
else:
    print('Ошибка чтения AccessToken')