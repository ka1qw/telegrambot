from keyboards.stdafx import *
from keyboards.common_kbs_and_btns import to_main_menu_btn, back_btn


'''--------------------------------РАСПИСАНИЕ--------------------------------'''

'''--------------------------------Начальная клава--------------------------------'''
schedule_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
schedule_economic = KeyboardButton('Экономический факультет')
schedule_iisigt = KeyboardButton('ИИСиГТ')
schedule_polar = KeyboardButton('Полярная академия')
schedule_igio = KeyboardButton('ИГиО')
schedule_meteo = KeyboardButton('Метеорологический факультет')
schedule_gmo = KeyboardButton('Факультет ГМO')
schedule_fmipp = KeyboardButton('ФМиПП')
schedule_weeks = KeyboardButton('Чередование учебных недель')

schedule_keyboard.insert(schedule_economic).insert(schedule_iisigt)
schedule_keyboard.insert(schedule_polar).insert(schedule_igio)
schedule_keyboard.insert(schedule_meteo).insert(schedule_gmo)
schedule_keyboard.insert(schedule_fmipp).insert(schedule_weeks)
schedule_keyboard.add(to_main_menu_btn).insert(back_btn)

'''--------------------------------Выбор сезона--------------------------------'''
schedule_keyboard_season_as = ReplyKeyboardMarkup(resize_keyboard=True)
schedule_autumn = KeyboardButton('Осенний семестр')
schedule_spring = KeyboardButton('Весенний семестр')

schedule_keyboard_season_as.insert(schedule_autumn).insert(schedule_spring)
schedule_keyboard_season_as.add(to_main_menu_btn).insert(back_btn)

schedule_keyboard_season_a = ReplyKeyboardMarkup(resize_keyboard=True)
schedule_keyboard_season_a.insert(schedule_autumn)
schedule_keyboard_season_a.add(to_main_menu_btn).insert(back_btn)

schedule_keyboard_season_s = ReplyKeyboardMarkup(resize_keyboard=True)
schedule_keyboard_season_s.insert(schedule_autumn)
schedule_keyboard_season_s.add(to_main_menu_btn).insert(back_btn)

schedule_keyboard_season_no_sch = ReplyKeyboardMarkup(resize_keyboard=True)
schedule_keyboard_season_no_sch.add(to_main_menu_btn).insert(back_btn)