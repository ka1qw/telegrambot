from keyboards.stdafx import *
from keyboards.common_kbs_and_btns import to_main_menu_btn, back_btn

'''--------------------------------FAQ--------------------------------'''  # тут будет ОЧЕНЬ много state's
faq_main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
faq_holiday_btn = KeyboardButton('Информация о каникулах')
faq_addSession_btn = KeyboardButton('Дополнительная сессия')
faq_scholarship = KeyboardButton('Повышенная стипендия')
faq_militaryDep = KeyboardButton('Военная кафедра')
faq_main_kb.insert(faq_holiday_btn).insert(faq_addSession_btn)
faq_main_kb.add(faq_scholarship).insert(faq_militaryDep)
faq_main_kb.add(to_main_menu_btn).insert(back_btn)

faq_militaryDep_choice = ReplyKeyboardMarkup(resize_keyboard=True)
faq_militaryDep_centre = KeyboardButton("Военно-учебный центр")
faq_militaryDep_table = KeyboardButton("Военно-учетный стол")
faq_militaryDep_choice.add(faq_militaryDep_centre).insert(faq_militaryDep_table).add(to_main_menu_btn).insert(back_btn)

faq_addSession_choice = ReplyKeyboardMarkup(resize_keyboard=True)
faq_addSession_decanat = KeyboardButton("Какой у меня деканат?")
faq_addSession_choice.add(faq_addSession_decanat)
faq_addSession_choice.add(to_main_menu_btn).insert(back_btn)

faq_addSession_decanat_kb = ReplyKeyboardMarkup(resize_keyboard=True)
faq_addSession_know_dec = KeyboardButton("Я не знаю свою группу :(")
faq_addSession_decanat_kb.add(faq_addSession_know_dec)
faq_addSession_decanat_kb.add(to_main_menu_btn).insert(back_btn)

faq_addSession_decanat_kb_2 = ReplyKeyboardMarkup(resize_keyboard=True)
faq_addSession_know_dec = KeyboardButton("Я не знаю свою группу :(")
faq_addSession_decanat_kb_2.add(faq_addSession_know_dec)
faq_addSession_decanat_kb_2.add(to_main_menu_btn)
