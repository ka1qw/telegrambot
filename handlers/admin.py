from create_bot import bot
from aiogram import types, Dispatcher
from phrases.admin_phrases import *
from keyboards.admin_kbs import *
from aiogram.dispatcher.filters import Text
from dicts.admins import admin_ids
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


async def command_admin_menu(message: types.Message):
    if str(message.from_user.id) in admin_ids:
        await bot.send_message(message.from_user.id, 'Админка', reply_markup=admin_start_kb)
    else:
        pass
        # await bot.send_message(message.from_user.id,message.from_user.id)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(command_admin_menu, Text(equals='/admin', ignore_case=True))
