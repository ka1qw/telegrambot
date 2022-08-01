# общее
from aiogram import types, Dispatcher
from create_bot import bot
from aiogram.dispatcher.filters import Text

# фразы
from phrases.common_phrases import *

# клавиатуры
from keyboards.main_menu_kbs import *


# команда /start или /help
async def command_start(message: types.Message):
    try:
        user_data = str(message.from_user.values)
        user_ids = []
        if message.from_user.username is None:
            await bot.send_message(message.from_user.id, f"Привет, незнакомец без имени пользователя!\n" + start_phrase,
                                   reply_markup=mainMenu_kb)
        else:
            await bot.send_message(message.from_user.id, f"Привет, {message.from_user.username}!\n" + start_phrase,
                                   reply_markup=mainMenu_kb)
        with open("users.txt", 'r') as users_data:
            for line in users_data:
                k = eval(line)
                user_ids.append(k.get('id'))
        with open("users.txt", 'a') as users_data:
            if message.from_user.id not in user_ids:
                users_data.write(user_data + '\n')
                if message.from_user.username is not None:
                    print(
                        f'Новый пользователь с именем {message.from_user.username} и id {message.from_user.id} добавлен!')
                else:
                    print(f'Новый пользователь без имени пользователя с id {message.from_user.id} добавлен!')
    except FileNotFoundError:
        print("[ERROR]: File users not found")


# возврат на главный экран
async def command_to_menu(message: types.Message):
    await bot.send_message(message.from_user.id, "Возвращаю на главную", reply_markup=mainMenu_kb)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_to_menu, Text(equals='Вернуться на главный экран', ignore_case=True))
