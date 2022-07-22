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
        user_id = str(message.from_user.id)
        k = []
        await bot.send_message(message.from_user.id, start_phrase, reply_markup=mainMenu_kb)
        # await message.delete()
        with open("users.txt", 'r') as user_data:
            for line in user_data:
                a = line.split(':')
                k.append(str(a[0]))
        with open("users.txt", 'a') as user_data:
            if str(message.from_user.id) + '\n' not in k:
                user_data.write(user_id + '\n')
                print(f'Новый пользователь {message.from_user.username} с id {message.from_user.id} добавлен!')
        k.clear()
    except FileNotFoundError:
        print("[ERROR]: File users not found")
    except:
        await message.reply("Общение с ботом происходит через личные сообщения\nhttps://t.me/TimeTableISIGTBot")


# возврат на главный экран
async def command_to_menu(message: types.Message):
    await bot.send_message(message.from_user.id, "Возвращаю на главную", reply_markup=mainMenu_kb)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_to_menu, Text(equals='Вернуться на главный экран', ignore_case=True))
