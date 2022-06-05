from create_bot import bot
from aiogram import types, Dispatcher
from phrases.schedule_phrases import *
from keyboards.schedule_kbs import *
from keyboards.main_menu_kbs import *
from keyboards.common_kbs_and_btns import *

from phrases.schedule_phrases import *

from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from repository.parser import *


class FSM_schedule(StatesGroup):
    schedule_start = State()  # начальный
    schedule_pick_season = State()  # ввод деканата
    give_docs = State()  # ввод кафедры

async def schedule_start(message: types.Message, state: FSMContext):
    await FSM_schedule.schedule_start.set()
    await bot.send_message(message.from_user.id, schedule_start_phrase, reply_markup=schedule_keyboard)

    async with state.proxy() as data:
        data['spring_scheds'], data['autumn_scheds'] = pars_all()

    # for key in data['spring_scheds']:
    #     print("Весна", key, "-----", data['spring_scheds'][key])
    #
    # for key in data['autumn_scheds']:
    #     print("Осень", key, "-----", data['autumn_scheds'][key])

    if len(data['spring_scheds']) > 0:
        async with state.proxy() as data:
            data['Autumn'] = True
    else:
        async with state.proxy() as data:
            data['Autumn'] = False
    if len(data['autumn_scheds']) > 0:
        async with state.proxy() as data:
            data['Spring'] = True
    else:
        async with state.proxy() as data:
            data['Spring'] = False


async def schedule_pick_season(message: types.Message, state: FSMContext):
    await FSM_schedule.next()
    async with state.proxy() as data:
        data['faculty'] = message.text
    async with state.proxy() as data:
        if data['Autumn'] == True and data['Spring'] == True:
            await bot.send_message(message.from_user.id, schedule_pick_season_as, reply_markup=schedule_keyboard_season_as)
        elif data['Autumn'] == True and data['Spring'] == False:
            await bot.send_message(message.from_user.id, schedule_pick_season_a, reply_markup=schedule_keyboard_season_a)
        elif data['Autumn'] == False and data['Spring'] == True:
            await bot.send_message(message.from_user.id, schedule_pick_season_s, reply_markup=schedule_keyboard_season_s)
        else:
            await bot.send_message(message.from_user.id, schedule_pick_season_no_sch, reply_markup=schedule_keyboard_season_no_sch)

async def give_docs(message: types.Message, state: FSMContext):
    await FSM_schedule.next()
    async with state.proxy() as data:
        data['season'] = message.text
        print(data['faculty'])
        for key in data['autumn_scheds']:
            print("Весна", key, "-----", data['autumn_scheds'][key])
        if data['season'] == "Осенний семестр":
            await bot.send_message(message.from_user.id, str(data['autumn_scheds'].get(data['faculty'])), reply_markup=schedule_keyboard_season_no_sch)
        elif data['season'] == "Весенний семестр":
            await bot.send_message(message.from_user.id, str(data['spring_scheds'].get(data['faculty'])), reply_markup=schedule_keyboard_season_no_sch)



def register_handlers_schedule(dp: Dispatcher):
    dp.register_message_handler(schedule_start, Text(equals='Расписание', ignore_case=True))
    dp.register_message_handler(schedule_pick_season, state=FSM_schedule.schedule_start)
    dp.register_message_handler(give_docs, state=FSM_schedule.schedule_pick_season)

