# общее
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State, StatesGroupMeta
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
    scholarship = State()
    scholarship_1 = State()
    militaryDep = State()  # военка
    militaryDep_1 = State()


# faq
async def command_faq_start(message: types.Message, state: FSMContext):
    await FSMfaq.faq_start.set()
    await bot.send_message(message.from_user.id, faq_start_phrase, reply_markup=faq_main_kb)
    async with state.proxy() as data:
        # data['way'].clear
        data['way'] = ['start']
        print(f"Ветка состояний: {data['way']}")
        print(f"Нынешнее состояние: {await state.get_state()}\n")


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
        print(f"Ветка состояний: {data['way']}")
        print(f"Нынешнее состояние: {await state.get_state()}\n")


async def command_faq_addsession_department_choice(message: types.Message, state: FSMContext):
    await FSMfaq.addSession_1.set()
    await bot.send_message(message.from_user.id, faq_addSession_department_info,
                           reply_markup=faq_addSession_department_group_input_kb)
    async with state.proxy() as data:
        data['way'].append('addSession_1')
        print(f"Ветка состояний: {data['way']}")
        print(f"Нынешнее состояние: {await state.get_state()}\n")


async def command_faq_addsession_group_input(message: types.Message, state: FSMContext):
    if message.text == "Я не знаю свою группу :(":
        await FSMfaq.addSession_2.set()
        await bot.send_message(message.from_user.id, faq_addSession_group_info, reply_markup=only_to_main_menu_kb)
    elif message.text in [i[0] for i in groups.items()]:
        async with state.proxy() as data:
            data['group'] = message.text
            # todo: реализовать выдачу пути к деканату, связать с навигацией
            ### здесь надо выдавать деканат и (возможно) путь к нему ###
            await bot.send_message(message.from_user.id, f'Твоя группа: {data["group"]}\n'
                                                         f'Твой деканат: деканат факультета/института '
                                                         f'{groups.get(message.text).get("department")}')
    elif message.text not in [i[0] for i in groups.items()]:
        await bot.send_message(message.from_user.id, "Такой группы в моей базе нет!\nВведи еще раз.",
                               reply_markup=faq_addSession_department_group_input_kb_without_back_btn)
    async with state.proxy() as data:
        data['way'].append('addSession_2')


# todo: сделать разветвление на повышку по оценкам и по достижениям
# повышка
async def command_faq_scholarship(message: types.Message, state: FSMContext):
    await FSMfaq.scholarship.set()
    await bot.send_message(message.from_user.id, faq_scholarship_choice, reply_markup=faq_scholarship_choice_kb)
    async with state.proxy() as data:
        data['way'].append('scholarship')
        print(f"Ветка состояний: {data['way']}")
        print(f"Нынешнее состояние: {await state.get_state()}\n")


async def command_faq_increased_scholarship(message: types.Message, state: FSMContext):
    await FSMfaq.scholarship_1.set()
    await bot.send_message(message.from_user.id, faq_scholarship_increased_scholarship_info,
                           reply_markup=back_and_to_main_menu_kb)
    await bot.send_document(message.from_user.id,
                            document=open("resources/docs/increased_scholarship/Заявление.docx", 'rb'))
    await bot.send_document(message.from_user.id,
                            document=open("resources/docs/increased_scholarship/Карта_претендента.docx", 'rb'))
    await bot.send_document(message.from_user.id,
                            document=open("resources/docs/increased_scholarship/Регламент.pdf", 'rb'))
    async with state.proxy() as data:
        data['way'].append('scholarship_1')
        print(f"Ветка состояний: {data['way']}")
        print(f"Нынешнее состояние: {await state.get_state()}\n")


async def command_faq_common_scholarship(message: types.Message, state: FSMContext):
    await FSMfaq.scholarship_1.set()
    await bot.send_message(message.from_user.id, faq_scholarship_common_scholarship_info,
                           reply_markup=back_and_to_main_menu_kb)
    await bot.send_document(message.from_user.id,
                            document=open("resources/docs/common_scholarship/Приказ.pdf", 'rb'))
    async with state.proxy() as data:
        data['way'].append('scholarship_1')
        print(f"Ветка состояний: {data['way']}")
        print(f"Нынешнее состояние: {await state.get_state()}\n")


async def command_faq_military_department_choice(message: types.Message, state: FSMContext):
    await FSMfaq.militaryDep.set()
    await bot.send_message(message.from_user.id, faq_militaryDep_info_choice, reply_markup=faq_militaryDep_choice)
    async with state.proxy() as data:
        data['way'].append('militaryDep')
        print(f"Ветка состояний: {data['way']}")
        print(f"Нынешнее состояние: {await state.get_state()}\n")


async def command_faq_military_department_centre(message: types.Message, state: FSMContext):
    await FSMfaq.militaryDep_1.set()
    await bot.send_message(message.from_user.id, faq_militaryDep_info_centre, reply_markup=back_and_to_main_menu_kb)
    async with state.proxy() as data:
        data['way'].append('militaryDep_1')
        print(f"Ветка состояний: {data['way']}")
        print(f"Нынешнее состояние: {await state.get_state()}\n")


async def command_faq_military_department_table(message: types.Message, state: FSMContext):
    await FSMfaq.militaryDep_1.set()
    await bot.send_message(message.from_user.id, faq_militaryDep_info_table, reply_markup=back_and_to_main_menu_kb)
    async with state.proxy() as data:
        data['way'].append('militaryDep_1')
        print(f"Ветка состояний: {data['way']}")
        print(f"Нынешнее состояние: {await state.get_state()}\n")


# Выход из состояний
async def to_start_faq(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(message.from_user.id, "Возвращаю на главную", reply_markup=mainMenu_kb)


async def on_back_faq(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        current_state = await state.get_state()
        print(f"Удаляю {data['way'][-1]} состояние")
        data['way'].pop()
        print(f"Ветка состояний: {data['way']}")
        if len(data['way']) == 0:
            if current_state is None:
                return
            await state.finish()
            await bot.send_message(message.from_user.id, "Возвращаю на главную", reply_markup=mainMenu_kb)
        elif data['way'][-1] == 'start':
            await FSMfaq.faq_start.set()
            await bot.send_message(message.from_user.id, faq_start_phrase, reply_markup=faq_main_kb)
            print(f"Нынешнее состояние: {await state.get_state()}\n")
        elif data['way'][-1] == 'holidays':
            await FSMfaq.faq_start.set()
            await bot.send_message(message.from_user.id, faq_holiday_info, reply_markup=faq_main_kb)
            print(f"Нынешнее состояние: {await state.get_state()}\n")
        elif data['way'][-1] == 'scholarship':
            await FSMfaq.scholarship.set()
            await bot.send_message(message.from_user.id, faq_scholarship_choice, reply_markup=faq_scholarship_choice_kb)
            print(f"Нынешнее состояние: {await state.get_state()}\n")
        elif data['way'][-1] == 'scholarship_1':
            await FSMfaq.scholarship_1.set()
            await bot.send_message(message.from_user.id, faq_scholarship_choice, reply_markup=faq_scholarship_choice_kb)
            print(f"Нынешнее состояние: {await state.get_state()}\n")
        elif data['way'][-1] == 'militaryDep':
            await FSMfaq.militaryDep.set()
            await bot.send_message(message.from_user.id, faq_militaryDep_info_choice,
                                   reply_markup=faq_militaryDep_choice)
            print(f"Нынешнее состояние: {await state.get_state()}\n")
        elif data['way'][-1] == 'militaryDep_1':
            await FSMfaq.militaryDep_1.set()
            await bot.send_message(message.from_user.id, faq_militaryDep_info_choice,
                                   reply_markup=back_and_to_main_menu_kb)
            print(f"Нынешнее состояние: {await state.get_state()}\n")
        elif data['way'][-1] == 'addSession':
            await FSMfaq.addSession.set()
            await bot.send_message(message.from_user.id, faq_addSession_info, reply_markup=faq_addSession_choice)
            print(f"Нынешнее состояние: {await state.get_state()}\n")
        elif data['way'][-1] == 'addSession_1':
            await FSMfaq.addSession_1.set()
            await bot.send_message(message.from_user.id, faq_addSession_department_info,
                                   reply_markup=faq_addSession_department_group_input_kb)
            print(f"Нынешнее состояние: {await state.get_state()}\n")
        elif data['way'][-1] == 'addSession_2':
            await FSMfaq.addSession_2.set()
            await bot.send_message(message.from_user.id, faq_addSession_department_info,
                                   reply_markup=back_and_to_main_menu_kb)
            print(f"Нынешнее состояние: {await state.get_state()}\n")


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
    dp.register_message_handler(command_faq_addsession_department_choice,
                                Text(equals='Какой у меня деканат?', ignore_case=True),
                                state=FSMfaq.addSession)
    dp.register_message_handler(command_faq_addsession_group_input,
                                state=FSMfaq.addSession_1)

    dp.register_message_handler(command_faq_scholarship, Text(equals='Повышенная стипендия', ignore_case=True),
                                state=FSMfaq.faq_start)
    dp.register_message_handler(command_faq_increased_scholarship, Text(equals='ПГАС', ignore_case=True),
                                state=FSMfaq.scholarship)
    dp.register_message_handler(command_faq_common_scholarship,
                                Text(equals='Академическая стипендия', ignore_case=True),
                                state=FSMfaq.scholarship)

    dp.register_message_handler(command_faq_military_department_choice,
                                Text(equals='Военная кафедра', ignore_case=True),
                                state=FSMfaq.faq_start)
    dp.register_message_handler(command_faq_military_department_centre,
                                Text(equals='Военно-учебный центр', ignore_case=True),
                                state=FSMfaq.militaryDep)
    dp.register_message_handler(command_faq_military_department_table,
                                Text(equals='Военно-учетный стол', ignore_case=True),
                                state=FSMfaq.militaryDep)
