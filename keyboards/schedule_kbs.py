from stdafx import *
from common_kbs_and_btns import to_main_menu_btn

'''--------------------------------РАСПИСАНИЕ--------------------------------'''
schedule_kb = ReplyKeyboardMarkup(resize_keyboard=True)

# schedule_kb.add(back_btn) в дальнейшем через state's сделаем назад
schedule_kb.add(to_main_menu_btn)
