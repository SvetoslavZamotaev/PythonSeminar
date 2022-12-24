
import telebot
import random
candys = 117
botwin = False
playerwin = False
def Break_while():
    if botwin or playerwin:
        return 1

def botTake():
    global candys
    candys = candys - random.randint(1,29)
    

def playerTake(howmuch):
    global candys
    candys = candys - howmuch

def checkForPlayer():
    global candys
    global playerwin
    if candys <= 0:
        playerwin = True


def checkForBot():
    global candys
    global botwin 
    if candys <= 0:
        botwin = True

def deleteWord (command):
    res = command.split()
    for i in res:
        if not i.isnumeric():
            res.remove(i)
    return int(res[0])
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.send_message(message.chat.id, 'test')


bot = telebot.TeleBot("5870581285:AAHbtEZ4Ie3xo9kzGFsfeZQgyMoaVzibOds")

@bot.message_handler(commands=['start'])		
def send_welcome(message):
    bot.send_message(message.chat.id,'Это игра в конфеты , введите число от 1 до 28, после этого введите любое сообщение и бот походит тоже')


mode = True

def mode_handler(thing):
    global mode
    thing = mode
    if thing:
        return True
    else:
        return False

@bot.message_handler(func=mode_handler)
def mode_true(message):  
    bot.send_message(message.chat.id, 'Ход игрока ')
    playerTake(deleteWord(message.text))
    checkForPlayer()
    bot.send_message(message.chat.id, (f'осталось {candys} конфет '))
    if playerwin:
        bot.send_message(message.chat.id,'Выйграл человек')	
    bot.send_message(message.chat.id, (f'осталось {candys} конфет '))
    global mode
    mode = False

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, 'Ход бота')
    botTake()
    checkForBot()
    if botwin:
    	bot.send_message(message.chat.id,'Выйграл бот')	
    bot.send_message(message.chat.id, (f'осталось {candys} конфет '))
    global mode
    mode = True	
	
print('server run')

bot.infinity_polling()


