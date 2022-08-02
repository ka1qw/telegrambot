from aiogram.utils import executor
from create_bot import dp, bot
from aiogram import types
from phrases.common_phrases import *
from keyboards.main_menu_kbs import *


async def on_startup(message: types.Message):
    pass
    # for _, user_id in admins_dict.items():
    #     try:
    #         pass
    #         #await bot.send_message(user_id.get('id'), start_phrase, reply_markup=mainMenu_kb)
    #     except Exception as ex:
    #         print(f"[ERROR {ex}]: Пользователь с id = {user_id} не найден!")


# async def on_shutdown(message: types.Message):
#     await bot.send_message('875231826', 'Завершаю работу', reply_markup=mainMenu_kb)
# await bot.send_message(message.from_user.id, "Бот работает!")


from handlers import main_menu, admin, other, navigation, schedule, faq

admin.register_handlers_admin(dp)
main_menu.register_handlers_client(dp)
navigation.register_handlers_navigation(dp)
schedule.register_handlers_schedule(dp)
faq.register_handlers_faq(dp)

other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  # , on_startup=on_startup
