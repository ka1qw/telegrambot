from create_bot import bot
from aiogram import types, Dispatcher
from phrases.schedule_phrases import *
from keyboards.schedule_kbs import *
from keyboards.main_menu_kbs import *
from keyboards.common_kbs_and_btns import *
from aiogram.dispatcher.filters import Text
from repository.parser import *


spring_scheds, autumn_scheds = pars_all()

for key in spring_scheds:
    print("Весна ", key, "-----", spring_scheds[key])

for key in autumn_scheds:
    print("Осень ", key, "-----", spring_scheds[key])

# выдача расписания
async def command_schedule(message: types.Message):
    await bot.send_message(message.from_user.id, schedule_phrase, reply_markup=schedule_kb)



def register_handlers_schedule(dp: Dispatcher):
    dp.register_message_handler(command_schedule, Text(equals='Расписание', ignore_case=True))
