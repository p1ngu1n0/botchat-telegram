import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
import chatbot


update_id = None


def main():
    
    global update_id
    
    
    #TOKEN
    bot = telegram.Bot('TOKEN AQUI')

    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
        
            update_id += 1


def echo(bot):
    global update_id
    
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  
            a = chatbot.bott(update.message.text)
            print(" recibido: "+ str(update.message.text))
            update.message.reply_text(a)


if __name__ == '__main__':
    main()
