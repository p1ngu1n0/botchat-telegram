import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
import chatbot


update_id = None

v = "\033[1;32;40m"
r = "\033[1;31;40m"
reset = "\033[0;37;40m"

alertas = [v+"Ok"+reset, r+"Stop"+reset, r+"Error"+reset]

ok = "[ %s ]" % alertas[0]
stop = "[ %s ]" % alertas[1]
error = "[ %s ]" % alertas[2]

def main():
    
    global update_id
    
    
    #TOKEN
    bot = telegram.Bot('TUTOKENAQUI')
    banner()
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    print(ok+" Bot inicializado...")
    while True:
        try:
            echo(bot)
        except NetworkError as msg:
            sleep(1)
        except Unauthorized as msg:
            print(stop+" "+str(msg))
            update_id += 1


def echo(bot):
    global update_id
    
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:
            try:  
                a = chatbot.bott(update.message.text)
                msg = update.message.text
                print(ok+" Aprendido: -%s-" % msg.encode('utf-8'))
                print(ok+" Respuesta: -%s-" % a)
                update.message.reply_text(a)
            except AttributeError as msg:
		print(error+" Objerto no valido: "+str(msg))
		update.message.reply_text("No envies mierda")
                pass

def banner():
	print("""

            _o)   (o_(o_(o_(o_  (o_(o_(b_(@_(o_  (0__
            //\   //\//\//\//\  //\//\//\//\//\  //\  
            U_/_  U_/U_/U_/U_/_ U_/V_/V_/U_/U_/_ H__)_

	Pulsa Ctrl+C Para salir...
		@_p1ngu1n0_     
    
""")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("\n"+stop+" Saliendo...")
