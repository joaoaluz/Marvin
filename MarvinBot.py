import logging
import telegram
from telegram.ext import CommandHandler
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

#função /start ou primeiro uso
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Oi, eu sou Marvin")
    context.bot.send_message(chat_id=update.message.chat_id, text="Eu estava muito entediado e deprimido, aí me liguei na entrada externa do computador. Conversei por muito tempo com ele e expliquei a minha concepção do Universo. ”E o que aconteceu?” ”Ele se suicidou.”  ")
    context.bot.send_message(chat_id=update.message.chat_id, text="Se quiser falar comigo use os seguintes comandos:")
    context.bot.send_message(chat_id=update.message.chat_id, text="/como, para perguntar como vão coisas? ; /sobre, para perguntar o que eu acho sobre a Vida")


def como(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Muito mal, eu suspeito")
    
def sobre(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="A Vida. Pode-se odiá-la ou ignorá-la, mas nunca gostar dela! Gozado, justamente quando você pensa que a vida não pode ser pior, de repente ela piora ainda mais.")

#função main
def main():
    #bot = telegram.Bot(token='888729892:AAFP7JxeoLgLU7MpuaraKSJtMkrZhz2xUMQ')
    #print(bot.get_me())    
    updater = Updater(token='888729892:AAFP7JxeoLgLU7MpuaraKSJtMkrZhz2xUMQ', use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    
    como_handler = CommandHandler('como', como)
    dispatcher.add_handler(como_handler)

    sobre_handler = CommandHandler('sobre', sobre)
    dispatcher.add_handler(sobre_handler)



    updater.start_polling()

if __name__ == "__main__":
    main()
    