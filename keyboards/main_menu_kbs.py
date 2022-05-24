from keyboards.stdafx import *

'''--------------------------------ГЛАВНОЕ МЕНЮ--------------------------------'''
schedule_btn = KeyboardButton('Расписание')
FAQ_btn = KeyboardButton('FAQ')
navigation_btn = KeyboardButton('Навигация по корпусу')

mainMenu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu_kb.add(schedule_btn).insert(FAQ_btn).add(navigation_btn)
