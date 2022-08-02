from aiogram import types, Dispatcher
from create_bot import bot
from keyboards.main_menu_kbs import mainMenu_kb
from aiogram.dispatcher.filters import Text
from emoji import emojize


async def echo_send(message: types.Message):
    await bot.send_message(message.from_user.id, emojize("Неизвестная команда\n"
                                                         "Если ты заблудился, выйди в главное меню с помощью клавиатуры :winking_face:"))


async def thank_command(message: types.Message):
    b = []
    with open("users.txt", 'r') as user_data:
        for line in user_data:
            b.append(line.replace('\n', ''))
    c = ['5336662587', '875231826']
    count = 1
    print(
        f'########################################################################\nНачинаю рассылку для {len(b)} юзеров.')
    # тут надо for item in b чтобы идти по юзерам
    for item in c:
        try:
            await bot.send_photo(item, open("resources/cat.jpg", 'rb'), 'Это ты тестишь бота')
            await bot.send_message(item, 'Спасибо за участие в первом тесте!\nБлижайшее время бот будет выключен :)',
                                   reply_markup=mainMenu_kb)
            print(f'[{count}/{len(b)}] Сообщение пользователю с id = {item} успешно отправлено')
        except Exception as ex:
            print(f'[{count}/{len(b)} ERROR] Ошибка у пользователя с id = {item}: {ex}')
        finally:
            count += 1
    print('Рассылка закончена\n########################################################################')


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(thank_command, Text(equals='Спасибо за тест', ignore_case=True), state='*')
    dp.register_message_handler(echo_send)
