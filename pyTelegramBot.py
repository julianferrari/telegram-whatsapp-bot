#Se utiliza la libreria "telepot"
#https://telepot.readthedocs.io/en/latest/
## pip install telepot
import telepot

################################
# Funciones

def handle(msg):
    if 'text' in msg and msg['text'] == '/start':
        bot.sendMessage(msg['chat']['id'],"BUEN DIA!")
        #bot.sendPhoto(msg['chat']['id'], photo=open('images/example.png', 'rb'))

def informar(msg):
    bot.sendMessage(group_id, msg) 
    
################################
# Variables
    
token = '**********' #Telegram Bot Token
receiver_id = 00000000 
group_id = 00000000 

bot = telepot.Bot(token)
bot.message_loop(handle)

#################################
#bot.sendMessage(group_id, 'Mensaje de prueba')
#bot.sendPhoto(group_id, photo=open('images/example.png', 'rb'))
#bot.sendDocument(group_id, document=open('report.pdf', 'rb'))
