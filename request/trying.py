import requests 
import telebot
import re


mode = False



r = requests.get('https://www.cbr-xml-daily.ru/daily_utf8.xml')
r.encoding = 'utf-8'
data = r.text

newdata = data.split('<Name>') #Формируем список из элементов после <name>
newdata_ver2 = []

for i in range(len(newdata)):
    newdata_ver2.append(re.sub('[A-Za-z\/][^>]*', '', newdata[i]))# Колхозная очистка от знаков 
split = ''

result_list = []

for i in range(len(newdata_ver2)):
    split = newdata_ver2[i].split('<>')       # Результирующий список только с названием валюты и значением в Р.
    result_list.append(split[0] + ' ' + split[2])

def boolmode(arg):
    global mode
    arg = mode
    return arg

def change_mode():
    global mode
    mode = not mode
    return mode
         
bot = telebot.TeleBot("5870581285:AAHbtEZ4Ie3xo9kzGFsfeZQgyMoaVzibOds")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Этот бот покажет вам курс валюты по запросу , введите название валюты на русском")
    change_mode()


@bot.message_handler(func=boolmode)
def find(message):
	for i in result_list:
            if i.find(message.text) != -1:
                bot.send_message(message.chat.id, i)


@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id, 'Вы остановили режим ввода , наберите /start если хотите еще поиск')
    change_mode()




print('server is on')



bot.infinity_polling()                


