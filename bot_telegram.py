from aiogram.utils import executor
from create_bot import dp,bot
from aiogram import types
from phrases import *
from keyboards import *
from dicts.admins import admin_ids
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils.exceptions import ChatNotFound
# admin_ids = ['875231826','5336662587', '213'] #969667049 - митяй


async def on_startup(message: types.Message):
    for i in admin_ids:
        try:
            await bot.send_message(i,start_phrase,reply_markup=mainMenu_kb)
        except Exception as ex:
            print(f"[ERROR {ex}]: Пользователь с id = {i} не найден!")
    # сюда подрубим БД с user_id пользователей, которые включили бота, и будем им рассылать сообщение
    # о начале работы бота после перезапуска
    # await bot.send_message(message.from_user.id, "Бот работает!")



from handlers import main_menu, admin, other, navigation, schedule, faq

admin.register_handlers_admin(dp)
main_menu.register_handlers_client(dp)
navigation.register_handlers_navigation(dp)
schedule.register_handlers_schedule(dp)
faq.register_handlers_faq(dp)


other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup) #, on_startup=on_startup
