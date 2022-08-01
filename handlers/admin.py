from create_bot import bot
from aiogram import types, Dispatcher
from phrases.admin_phrases import *
from keyboards.admin_kbs import *
from phrases.common_phrases import *
from aiogram.dispatcher.filters import Text
from keyboards.main_menu_kbs import mainMenu_kb
from aiogram.dispatcher.filters.state import StatesGroup, State, default_state
from emoji import emojize


class FSMadmin(StatesGroup):
    admin_start = State()
    admin_refresh = State()
    admin_add = State()


async def command_admin_menu(message: types.Message):
    try:
        potential_admin_id = message.from_user.id
        admin_ids = []
        with open("admins.txt", 'r') as users_data:
            for line in users_data:
                try:
                    k = eval(line)
                    admin_ids.append(k.get('id'))
                except Exception as ex:
                    print(ex)
                    continue
        if potential_admin_id in admin_ids:
            await FSMadmin.admin_start.set()
            await bot.send_message(potential_admin_id, 'Админка', reply_markup=admin_start_kb)
    except FileNotFoundError:
        print("[ERROR]: File users not found")


async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, command_list)


async def command_refresh(message: types.Message):
    users_ids = []
    with open("users.txt", 'r') as users_data:
        for line in users_data:
            k = eval(line)
            users_ids.append(k.get('id'))
    count = 1
    print(
        f'########################################################################\n'
        f'                      Начинаю обновление для {len(users_ids)} юзеров.\n')
    for user in users_ids:
        try:
            await State.set(default_state)
            await bot.send_message(user, start_phrase, reply_markup=mainMenu_kb)
            print(f'[{count}/{len(users_ids)}] Сообщение пользователю с id = {user} успешно отправлено')
        except Exception as ex:
            print(f'[{count}/{len(users_ids)} ERROR] Ошибка у пользователя с id = {user}: {ex}')
        finally:
            count += 1
    print('\n                           Обновление закончено\n'
          '########################################################################')


async def command_add_admin(message: types.Message):
    id_of_potential_admin = int(message.text.split(' ')[1])
    users_ids = []
    with open("users.txt", 'r') as users_data:
        for line in users_data:
            try:
                k = eval(line)
                users_ids.append(k.get('id'))
            except Exception as ex:
                print(ex)
                continue
    if id_of_potential_admin in users_ids:
        with open("admins.txt", 'r+') as admins_data:
            for admin_line in admins_data:
                try:
                    if eval(admin_line).get('id') == id_of_potential_admin:
                        await bot.send_message(message.from_user.id, 'Этот админ уже добавлен в список админов')
                        return
                except Exception as ex:
                    print(ex)
                    continue
            with open('users.txt', 'r') as user_data:
                for line in user_data:
                    try:
                        if eval(line).get('id') == id_of_potential_admin:
                            admins_data.write(line.strip() + '\n')
                            await bot.send_message(message.from_user.id,
                                                   f'Добавлен админ, id = {id_of_potential_admin}, username = {eval(line).get("username")}')
                    except Exception as ex:
                        print(ex)
                        continue
    else:
        await bot.send_message(message.from_user.id, 'Этот человек не запускал бота')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(command_admin_menu, Text(equals='/admin', ignore_case=True), state='*')
    dp.register_message_handler(command_refresh, Text(
        equals=emojize(':double_exclamation_mark: refresh users :double_exclamation_mark:'), ignore_case=True),
                                state=FSMadmin.admin_start)
    dp.register_message_handler(command_add_admin, Text(contains='/add_admin ', ignore_case=True),
                                state=FSMadmin.admin_start)
    dp.register_message_handler(command_help, Text(equals='help', ignore_case=True),
                                state=FSMadmin.admin_start)
