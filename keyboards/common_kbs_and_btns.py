from keyboards.stdafx import *

'''--------------------------------ОБЩИЕ КЛАВЫ--------------------------------'''
back_and_to_main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
to_main_menu_btn = KeyboardButton('Вернуться на главный экран')
back_btn = KeyboardButton('Назад')
back_and_to_main_menu_kb.add(to_main_menu_btn, back_btn)

only_to_main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
only_to_main_menu_kb.add(to_main_menu_btn)
