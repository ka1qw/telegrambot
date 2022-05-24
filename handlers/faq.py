# общее
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from create_bot import bot
from aiogram import types, Dispatcher

# словари
from dicts.groups import groups

# фразы
from phrases.faq_phrases import *

# клавиатуры
from keyboards.faq_kbs import *
from keyboards.common_kbs_and_btns import *
from keyboards.main_menu_kbs import *


class FSMfaq(StatesGroup):
    faq_start = State()
    holidays = State()  # каникулы
    addSession = State()  # допса
    addSession_1 = State()  #
    addSession_2 = State()  #
    scholarship = State()  # повышка
    militaryDep = State()  # военка
    militaryDep_1 = State()


# faq
async def command_faq_start(message: types.Message, state: FSMContext):
    await FSMfaq.faq_start.set()
    await bot.send_message(message.from_user.id, faq_start_phrase, reply_markup=faq_main_kb)
    async with state.proxy() as data:
        # data['way'].clear
        data['way'] = ['start']


# каникулы
async def command_faq_holidays(message: types.Message):
    await FSMfaq.holidays.set()
    await bot.send_message(message.from_user.id, faq_holiday_info)
    # async with state.proxy() as data:
    #     data['way'].append('holidays')
    await FSMfaq.faq_start.set()


# допса
async def command_faq_addsession(message: types.Message, state: FSMContext):
    await FSMfaq.addSession.set()
    await bot.send_message(message.from_user.id, faq_addSession_info, reply_markup=faq_addSession_choice)
    async with state.proxy() as data:
        data['way'].append('addSession')


async def command_faq_addsession_1(message: types.Message, state: FSMContext):
    await FSMfaq.addSession_1.set()
    await bot.send_message(message.from_user.id, faq_addSession_department_info, reply_markup=faq_addSession_decanat_kb)
    async with state.proxy() as data:
        data['way'].append('addSession_1')


async def command_faq_addSession_2(message: types.Message, state: FSMContext):
    if message.text == "Я не знаю свою группу :(":
        await FSMfaq.addSession_2.set()
        await bot.send_message(message.from_user.id, faq_addSession_group_info, reply_markup=only_to_main_menu_kb)
    elif message.text in [i[0] for i in groups.items()]:
        async with state.proxy() as data:
            data['group'] = message.text
            ### здесь надо выдавать деканат и (возможно) путь к нему ###
            await bot.send_message(message.from_user.id, f'Твоя группа: {data["group"]}\n'
                                                         f'Твой деканат: деканат факультета/института '
                                                         f'{groups.get(message.text).get("department")}')
    elif message.text not in [i[0] for i in groups.items()]:
        await bot.send_message(message.from_user.id, "Такой группы в моей базе нет!\nВведи еще раз.",
                               reply_markup=faq_addSession_decanat_kb_2)
    async with state.proxy() as data:
        data['way'].append('addSession_2')


# повышка
async def command_faq_scholarship(message: types.Message, state: FSMContext):
    await FSMfaq.scholarship.set()
    await bot.send_message(message.from_user.id, faq_scholarship_info)
    await FSMfaq.faq_start.set()
    # async with state.proxy() as data:
    #     data['way'].append('scholarship')


# военка
async def command_faq_militaryDep(message: types.Message, state: FSMContext):
    await FSMfaq.militaryDep.set()
    await bot.send_message(message.from_user.id, faq_militaryDep_info_choice, reply_markup=faq_militaryDep_choice)
    async with state.proxy() as data:
        data['way'].append('militaryDep')


async def command_faq_militaryDep_centre(message: types.Message, state: FSMContext):
    await FSMfaq.militaryDep_1.set()
    await bot.send_message(message.from_user.id, faq_militaryDep_info_centre, reply_markup=back_and_to_main_menu_kb)
    async with state.proxy() as data:
        data['way'].append('militaryDep_1')


async def command_faq_militaryDep_table(message: types.Message, state: FSMContext):
    await FSMfaq.militaryDep_1.set()
    await bot.send_message(message.from_user.id, faq_militaryDep_info_table, reply_markup=back_and_to_main_menu_kb)
    async with state.proxy() as data:
        data['way'].append('militaryDep_1')


# Выход из состояний
async def to_start_faq(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(message.from_user.id, "Возвращаю на главную", reply_markup=mainMenu_kb)


async def on_back_faq(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['way'].pop()
        print(data['way'])
        if len(data['way']) == 0:
            current_state = await state.get_state()
            if current_state is None:
                return
            await state.finish()
            await bot.send_message(message.from_user.id, "Возвращаю на главную", reply_markup=mainMenu_kb)
        elif data['way'][-1] == 'start':
            await FSMfaq.faq_start.set()
            await bot.send_message(message.from_user.id, faq_start_phrase, reply_markup=faq_main_kb)
        elif data['way'][-1] == 'holidays':
            await FSMfaq.faq_start.set()
            await bot.send_message(message.from_user.id, faq_holiday_info, reply_markup=faq_main_kb)
        elif data['way'][-1] == 'scholarship':
            await FSMfaq.faq_start.set()
            await bot.send_message(message.from_user.id, faq_scholarship_info, reply_markup=faq_main_kb)
        elif data['way'][-1] == 'militaryDep':
            await FSMfaq.militaryDep.set()
            await bot.send_message(message.from_user.id, faq_militaryDep_info_choice,
                                   reply_markup=faq_militaryDep_choice)
        elif data['way'][-1] == 'militaryDep_1':
            await FSMfaq.militaryDep_1.set()
            await bot.send_message(message.from_user.id, faq_militaryDep_info_choice,
                                   reply_markup=back_and_to_main_menu_kb)
        elif data['way'][-1] == 'addSession':
            await FSMfaq.addSession.set()
            await bot.send_message(message.from_user.id, faq_addSession_info, reply_markup=faq_addSession_choice)
        elif data['way'][-1] == 'addSession_1':
            await FSMfaq.addSession_1.set()
            await bot.send_message(message.from_user.id, faq_addSession_department_info,
                                   reply_markup=faq_addSession_decanat_kb)
        elif data['way'][-1] == 'addSession_2':
            await FSMfaq.addSession_2.set()
            await bot.send_message(message.from_user.id, faq_addSession_department_info,
                                   reply_markup=back_and_to_main_menu_kb)


def register_handlers_faq(dp: Dispatcher):
    dp.register_message_handler(on_back_faq, Text(equals='Назад', ignore_case=True),
                                state=[i for i in FSMfaq.all_states])
    dp.register_message_handler(to_start_faq, Text(equals='Вернуться на главный экран', ignore_case=True),
                                state=[i for i in FSMfaq.all_states])
    dp.register_message_handler(command_faq_start, Text(equals='FAQ', ignore_case=True), state=None)
    dp.register_message_handler(command_faq_holidays, Text(equals='Информация о каникулах', ignore_case=True),
                                state=FSMfaq.faq_start)
    dp.register_message_handler(command_faq_addsession, Text(equals='Дополнительная сессия', ignore_case=True),
                                state=FSMfaq.faq_start)
    dp.register_message_handler(command_faq_addsession_1, Text(equals='Какой у меня деканат?', ignore_case=True),
                                state=FSMfaq.addSession)
    dp.register_message_handler(command_faq_addSession_2,
                                state=FSMfaq.addSession_1)  # Text(equals=[i for i in groups], ignore_case=True),

    dp.register_message_handler(command_faq_scholarship, Text(equals='Повышенная стипендия', ignore_case=True),
                                state=FSMfaq.faq_start)
    dp.register_message_handler(command_faq_militaryDep, Text(equals='Военная кафедра', ignore_case=True),
                                state=FSMfaq.faq_start)
    dp.register_message_handler(command_faq_militaryDep_centre, Text(equals='Военно-учебный центр', ignore_case=True),
                                state=FSMfaq.militaryDep)
    dp.register_message_handler(command_faq_militaryDep_table, Text(equals='Военно-учетный стол', ignore_case=True),
                                state=FSMfaq.militaryDep)
