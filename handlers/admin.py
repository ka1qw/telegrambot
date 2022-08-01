from create_bot import bot
from aiogram import types, Dispatcher
from phrases.admin_phrases import *
from keyboards.admin_kbs import *
from phrases.common_phrases import *
from aiogram.dispatcher.filters import Text
from dicts.admins import admin_ids
from keyboards.main_menu_kbs import mainMenu_kb
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State, default_state


async def command_admin_menu(message: types.Message):
    if str(message.from_user.id) in admin_ids:
        await bot.send_message(message.from_user.id, 'Админка', reply_markup=admin_start_kb)
    else:
        pass
        # await bot.send_message(message.from_user.id,message.from_user.id)


'''
Команда для выдачи всем пользователям клавиатуры основного меню.
Используется после перезапуска бота.
'''
async def command_refresh(message: types.Message):
    # TODO: сделать словарь юзеров вместо списка, содержание - username, id
    admins = []
    # здесь должен быть список всех пользователей, сейчас только админы - для теста
    with open("admins.txt", 'r') as user_data:
        for line in user_data:
            admins.append(line.replace('\n', ''))
    count = 1
    print(
        f'########################################################################\n'
        f'                      Начинаю обновление для {len(admins)} юзеров.\n')
    for user in admins:
        try:
            await State.set(default_state)
            await bot.send_message(user, start_phrase,reply_markup=mainMenu_kb)
            print(f'[{count}/{len(admins)}] Сообщение пользователю с id = {user} успешно отправлено')
        except Exception as ex:
            print(f'[{count}/{len(admins)} ERROR] Ошибка у пользователя с id = {user}: {ex}')
        finally:
            count += 1
    print('\n                           Обновление закончено\n'
          '########################################################################')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(command_admin_menu, Text(equals='/admin', ignore_case=True), state='*')
    dp.register_message_handler(command_refresh, Text(equals='/refresh', ignore_case=True), state='*')
