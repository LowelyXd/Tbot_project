from bs4 import BeautifulSoup
import requests
import telebot
from telebot import types

Url = 'https://habr.com/ru/news/'
page = requests.get(Url)

soup = BeautifulSoup(page.text, "html.parser")
allNews = soup.findAll('a', class_='tm-article-snippet__title-link',)

a_list = []

for item in allNews:
    item_text = item.text
    item_href = ' ' +'https://habr.com' + item.get("href")
    a_list.append(item.text +'\n' + item_href)

print(a_list)

link = 'https://www.igromania.ru/news/'
page = requests.get(link)

b_list=[]

soup = BeautifulSoup(page.text, "html.parser")
allNews = soup.find('div', class_='aubl_cont').findAll('a',href_='' ,class_='aubli_name')

for item in allNews:
    item_text = item.text
    item_href = ' ' + 'https://www.igromania.ru' + item.get("href")
    b_list.append(item.text + '' + item_href)

print(b_list)

link = 'https://yandex.ru/news/region/moscow_and_moscow_oblast'
page = requests.get(link)

c_list=[]

soup = BeautifulSoup(page.text, "html.parser")
allNews = soup.find('div', class_="mg-grid__row mg-grid__row_gap_8 news-top-flexible-stories news-app__top").findAll('a', href_='')

for item in allNews:
    item_text = item.text
    item_href = ' ' +'\n'+ item.get("href")
    c_list.append(item.text + '' + item_href)

print(c_list)

bot=telebot.TeleBot('5389614141:AAFUE2KSD6V87Z8DEBCgIA3_z4FjiGNgD4g')

@bot.message_handler(commands=['start'])
def website(message):
    mess = f'Привет, {message.from_user.first_name}, выберите сайт с которого хотите увидеть новость'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website1=types.KeyboardButton('IT')
    website2=types.KeyboardButton('Игры')
    website3 = types.KeyboardButton('Новости Москвы')
    markup.add(website1, website2, website3)
    bot.send_message(message.chat.id, mess, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'IT':
            for i in range(0, 5, 1):
                bot.send_message(message.chat.id, a_list[i])
        elif message.text == 'Игры':
            for t in b_list:
                bot.send_message(message.chat.id, t)
        elif message.text == 'Новости Москвы':
            for u in c_list:
                bot.send_message(message.chat.id, u)

bot.polling(none_stop=True)