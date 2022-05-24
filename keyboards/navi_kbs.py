from keyboards.stdafx import *
from keyboards.common_kbs_and_btns import to_main_menu_btn,back_btn

'''--------------------------------НАВИГАЦИЯ--------------------------------'''

#################################################################################
navigation_kb = ReplyKeyboardMarkup(resize_keyboard=True)
navigation_decanat = KeyboardButton('Поиск деканата')
navigation_department = KeyboardButton('Поиск кафедры')
navigation_auditorium = KeyboardButton('Поиск аудитории')
navigation_other = KeyboardButton('Другое')
navigation_kb.insert(navigation_decanat).insert(navigation_department)
navigation_kb.add(navigation_auditorium).insert(navigation_other)
navigation_kb.add(to_main_menu_btn).insert(back_btn)
#################################################################################
navigation_decanat_kb = ReplyKeyboardMarkup(resize_keyboard=True)
navigation_decanat_1 = KeyboardButton('Деканат ИИСиГТ')
navigation_decanat_2 = KeyboardButton('Деканат ИГиО')
navigation_decanat_kb.insert(navigation_decanat_1).insert(navigation_decanat_2)
navigation_decanat_kb.add(to_main_menu_btn).insert(back_btn)
#################################################################################
navigation_department_kb = ReplyKeyboardMarkup(resize_keyboard=True)
navigation_department_1 = KeyboardButton('Кафедра ВТИ')
navigation_department_2 = KeyboardButton('Кафедра океанологии')
navigation_department_3 = KeyboardButton('Кафедра ВМиИ')
navigation_department_4 = KeyboardButton('Кафедра ПИ')
navigation_department_5 = KeyboardButton('Кафедра ИТиСБ')
navigation_department_6 = KeyboardButton('Кафедра физики')
navigation_department_7 = KeyboardButton('Кафедра МИС')
navigation_department_8 = KeyboardButton('Кафедра КУПЗ')
navigation_department_kb.insert(navigation_department_1).insert(navigation_department_2)
navigation_department_kb.add(navigation_department_3).insert(navigation_department_4)
navigation_department_kb.add(navigation_department_5).insert(navigation_department_6)
navigation_department_kb.add(navigation_department_7).insert(navigation_department_8)
navigation_department_kb.add(to_main_menu_btn).insert(back_btn)
#################################################################################
navigation_auditorium_kb = ReplyKeyboardMarkup(resize_keyboard=True)
navigation_auditorium_1 = KeyboardButton('Лаб. физики океана')
navigation_auditorium_2 = KeyboardButton('Лаб. физики')
navigation_auditorium_3 = KeyboardButton('Лаб. КУПЗ')
navigation_auditorium_4 = KeyboardButton('Каб. геологии')
navigation_auditorium_5 = KeyboardButton('14 квартира')
navigation_auditorium_kb.insert(navigation_auditorium_1).insert(navigation_auditorium_2)
navigation_auditorium_kb.add(navigation_auditorium_3).insert(navigation_auditorium_4)
navigation_auditorium_kb.add(navigation_auditorium_5)
navigation_auditorium_kb.add(to_main_menu_btn).insert(back_btn)
#################################################################################
#################################################################################
navigation_other_kb = ReplyKeyboardMarkup(resize_keyboard=True)
navigation_other_1 = KeyboardButton('Гардероб')
navigation_other_2 = KeyboardButton('Вестибюль')
navigation_other_3 = KeyboardButton('Столовая')
navigation_other_4 = KeyboardButton('Библиотека')
navigation_other_5 = KeyboardButton('Архив')
navigation_other_kb.insert(navigation_other_1).insert(navigation_other_2)
navigation_other_kb.add(navigation_other_3).insert(navigation_other_4)
navigation_other_kb.add(navigation_other_5)
navigation_other_kb.add(to_main_menu_btn).insert(back_btn)
#################################################################################
clear_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
clear_keyboard.add(to_main_menu_btn).insert(back_btn)