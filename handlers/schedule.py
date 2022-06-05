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
        data['way'] = ['start']

    async with state.proxy() as data:
        data['spring_scheds'], data['autumn_scheds'] = pars_all()

    if len(data['autumn_scheds']) > 0:
        async with state.proxy() as data:
            data['Autumn'] = True
    else:
        async with state.proxy() as data:
            data['Autumn'] = False
    if len(data['spring_scheds']) > 0:
        async with state.proxy() as data:
            data['Spring'] = True
    else:
        async with state.proxy() as data:
            data['Spring'] = False


async def schedule_pick_season(message: types.Message, state: FSMContext):
    await FSM_schedule.next()
    async with state.proxy() as data:
        data['way'].append('pick_season')
    async with state.proxy() as data:
        data['faculty'] = message.text
    async with state.proxy() as data:
        if data['Autumn'] is True and data['Spring'] is True:
            await bot.send_message(message.from_user.id, schedule_pick_season_as, reply_markup=schedule_keyboard_season_as)
            data['phrase'] = schedule_pick_season_as
            data['keyboard'] = schedule_keyboard_season_as
        elif data['Autumn'] is True and data['Spring'] is False:
            await bot.send_message(message.from_user.id, schedule_pick_season_a, reply_markup=schedule_keyboard_season_a)
            data['phrase'] = schedule_pick_season_a
            data['keyboard'] = schedule_keyboard_season_a
        elif data['Autumn'] is False and data['Spring'] is True:
            await bot.send_message(message.from_user.id, schedule_pick_season_s, reply_markup=schedule_keyboard_season_s)
            data['phrase'] = schedule_pick_season_a
            data['keyboard'] = schedule_keyboard_season_s
        else:
            await bot.send_message(message.from_user.id, schedule_pick_season_no_sch, reply_markup=schedule_keyboard_season_no_sch)
            data['phrase'] = schedule_pick_season_no_sch
            data['keyboard'] = schedule_keyboard_season_no_sch

async def give_docs(message: types.Message, state: FSMContext):
    await FSM_schedule.next()
    async with state.proxy() as data:
        data['way'].append('give_docs')
    async with state.proxy() as data:
        data['season'] = message.text
        data['faculty'] = change_faculty_name(data['faculty'])
        url = "https://www.rshu.ru/university/stud/"
        if data['season'] == "Осенний семестр":
            await bot.send_message(message.from_user.id,"Ссылка на скачивание документа: "+ url + str(data['autumn_scheds'].get(data['faculty'])), reply_markup=schedule_keyboard_season_no_sch)
        elif data['season'] == "Весенний семестр":
            await bot.send_message(message.from_user.id,"Ссылка на скачивание документа: "+ url + str(data['spring_scheds'].get(data['faculty'])), reply_markup=schedule_keyboard_season_no_sch)


async def on_back(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if len(data['way']) != 0:
            data['way'].pop()
        if len(data['way']) == 0:
            current_state = await state.get_state()
            if current_state is None:
                return
            await state.finish()
            await bot.send_message(message.from_user.id, "Возвращаю на главную", reply_markup=mainMenu_kb)
        elif data['way'][-1] == 'start':
            await FSM_schedule.schedule_start.set()
            await bot.send_message(message.from_user.id, schedule_start_phrase, reply_markup=schedule_keyboard)
        elif data['way'][-1] == 'pick_season':
            await FSM_schedule.schedule_pick_season.set()
            await bot.send_message(message.from_user.id, data['phrase'], reply_markup=data['keyboard'])



async def to_start(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(message.from_user.id, "Возвращаю на главную", reply_markup=mainMenu_kb)


def register_handlers_schedule(dp: Dispatcher):
    dp.register_message_handler(to_start, Text(equals='Вернуться на главный экран', ignore_case=True), state=[i for i in FSM_schedule.all_states])
    dp.register_message_handler(on_back, Text(equals='Назад', ignore_case=True), state=[i for i in FSM_schedule.all_states])
    dp.register_message_handler(schedule_start, Text(equals='Расписание', ignore_case=True))
    dp.register_message_handler(schedule_pick_season, state=FSM_schedule.schedule_start)
    dp.register_message_handler(give_docs, state=FSM_schedule.schedule_pick_season)

