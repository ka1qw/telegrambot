from keyboards.stdafx import *
from keyboards.common_kbs_and_btns import to_main_menu_btn, back_btn
import emoji

'''--------------------------------АДМИНКА--------------------------------'''
admin_start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
refresh_users_btn = KeyboardButton(emoji.emojize(':double_exclamation_mark: refresh users :double_exclamation_mark:'))
admin_start_kb.add(refresh_users_btn, to_main_menu_btn)
