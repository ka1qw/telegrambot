from create_bot import bot
from aiogram import types, Dispatcher
from phrases.schedule_phrases import *
from keyboards.schedule_kbs import *
from keyboards.main_menu_kbs import *
from keyboards.common_kbs_and_btns import *
from aiogram.dispatcher.filters import Text

import requests
from bs4 import BeautifulSoup

url = "https://www.rshu.ru/university/stud/"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

hrefs = {}

for link in soup.find_all('a'):
    key_shot = str(link)[str(link).find('>')+1:str(link).find('</a>')]
    if link.get('href').find("second") != -1:
        hrefs[key_shot] = link.get('href')

# for key in hrefs:
#     print(key, "----", hrefs[key])
#     url_2 = "https://www.rshu.ru/university/stud/" + hrefs[key]
#     page_2 = requests.get(url_2)
#     soup_2  = BeautifulSoup(page_2.text, "html.parser")
#     print(soup_2)




# выдача расписания
async def command_schedule(message: types.Message):
    await bot.send_message(message.from_user.id, schedule_phrase, reply_markup=schedule_kb)



def register_handlers_schedule(dp: Dispatcher):
    dp.register_message_handler(command_schedule, Text(equals='Расписание', ignore_case=True))
