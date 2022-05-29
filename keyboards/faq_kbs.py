from keyboards.stdafx import *
from keyboards.common_kbs_and_btns import to_main_menu_btn, back_btn

'''--------------------------------FAQ--------------------------------'''
faq_main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
faq_holiday_btn = KeyboardButton('Каникулы')
faq_addSession_btn = KeyboardButton('Сессия')
faq_scholarship_btn = KeyboardButton('Стипендия')
faq_militaryDep_btn = KeyboardButton('Военная кафедра')
faq_dormitory_btn = KeyboardButton('Общежития')
faq_main_kb.insert(faq_holiday_btn).insert(faq_addSession_btn)
faq_main_kb.add(faq_scholarship_btn).insert(faq_militaryDep_btn)
faq_main_kb.add(faq_dormitory_btn)
faq_main_kb.add(to_main_menu_btn).insert(back_btn)

# каникулы
faq_holidays_choice_kb = ReplyKeyboardMarkup(resize_keyboard=True)
faq_holidays_summer = KeyboardButton('Летние каникулы')
faq_holidays_winter = KeyboardButton('Зимние каникулы')
faq_holidays_choice_kb.add(faq_holidays_summer, faq_holidays_winter)

# сессии
faq_session_kb = ReplyKeyboardMarkup(resize_keyboard=True)
faq_session_common_btn = KeyboardButton('Обычная сессия')
faq_session_add_btn = KeyboardButton('Дополнительная сессия')
faq_session_kb.add(faq_session_common_btn, faq_session_add_btn)
faq_session_kb.add(to_main_menu_btn, back_btn)

faq_addSession_choice_kb = ReplyKeyboardMarkup(resize_keyboard=True)
faq_addSession_department_btn = KeyboardButton("Какой у меня деканат?")
faq_addSession_choice_kb.add(faq_addSession_department_btn)
faq_addSession_choice_kb.add(to_main_menu_btn).insert(back_btn)

faq_addSession_department_group_input_kb = ReplyKeyboardMarkup(resize_keyboard=True)
faq_addSession_know_dec_btn = KeyboardButton("Я не знаю свою группу")
faq_addSession_department_group_input_kb.add(faq_addSession_know_dec_btn)
faq_addSession_department_group_input_kb.add(to_main_menu_btn).insert(back_btn)

faq_addSession_department_group_input_kb_without_back_btn = ReplyKeyboardMarkup(resize_keyboard=True)
faq_addSession_department_group_input_kb_without_back_btn.add(faq_addSession_know_dec_btn)
faq_addSession_department_group_input_kb_without_back_btn.add(to_main_menu_btn)

# стипендии
faq_scholarship_choice_kb = ReplyKeyboardMarkup(resize_keyboard=True)
faq_scholarship_choice_increased_scholarship_btn = KeyboardButton('ПГАС')
faq_scholarship_choice_common_scholarship_btn = KeyboardButton('Академическая стипендия')
faq_scholarship_choice_social_scholarship_btn = KeyboardButton('Социальная стипендия')
faq_scholarship_choice_kb.add(faq_scholarship_choice_increased_scholarship_btn)
faq_scholarship_choice_kb.insert(faq_scholarship_choice_common_scholarship_btn)
faq_scholarship_choice_kb.add(faq_scholarship_choice_social_scholarship_btn)
faq_scholarship_choice_kb.add(to_main_menu_btn, back_btn)

# военка
faq_militaryDep_choice = ReplyKeyboardMarkup(resize_keyboard=True)
faq_militaryDep_centre_btn = KeyboardButton("Военно-учебный центр")
faq_militaryDep_table_btn = KeyboardButton("Военно-учетный стол")
faq_militaryDep_choice.add(faq_militaryDep_centre_btn).insert(faq_militaryDep_table_btn).add(to_main_menu_btn).insert(
    back_btn)

# общежития
faq_dormitory_choice_kb = ReplyKeyboardMarkup(resize_keyboard=True)
faq_dormitory_choice_1st_btn = KeyboardButton('Общежитие №1')
faq_dormitory_choice_2nd_btn = KeyboardButton('Общежитие №2')
faq_dormitory_choice_3rd_btn = KeyboardButton('Общежитие №3')
faq_dormitory_choice_4th_btn = KeyboardButton('Общежитие №4')
faq_dormitory_choice_5th_btn = KeyboardButton('Общежитие №5')
faq_dormitory_choice_pay_info_btn = KeyboardButton('Оплата проживания')
faq_dormitory_choice_kb.add(faq_dormitory_choice_1st_btn, faq_dormitory_choice_2nd_btn, faq_dormitory_choice_3rd_btn,
                            faq_dormitory_choice_4th_btn, faq_dormitory_choice_5th_btn)
faq_dormitory_choice_kb.add(faq_dormitory_choice_pay_info_btn)
faq_dormitory_choice_kb.add(to_main_menu_btn).insert(back_btn)
