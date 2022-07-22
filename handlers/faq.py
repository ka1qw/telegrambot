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

# эмодзи
import emoji


class FSMfaq(StatesGroup):
    faq_start = State()
    holidays = State()
    holidays_1 = State()
    session = State()
    session_1 = State()
    session_2 = State()
    session_3 = State()
    scholarship = State()
    scholarship_1 = State()
    militaryDep = State()
    militaryDep_1 = State()
    dormitory = State()
    dormitory_1 = State()


# главное меню FAQ
async def command_faq_start(message: types.Message, state: FSMContext):
    await FSMfaq.faq_start.set()
    await bot.send_message(message.from_user.id, faq_start_phrase, reply_markup=faq_main_kb)
    async with state.proxy() as data:
        data['way'] = ['faq_start']
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


# каникулы
async def command_faq_holidays_choice_group(message: types.Message, state: FSMContext):
    await FSMfaq.holidays.set()
    await bot.send_message(message.from_user.id, faq_holiday_main_info)
    await bot.send_message(message.from_user.id, faq_holiday_info_individual,
                           reply_markup=faq_addSession_department_group_input_kb,
                           parse_mode="Markdown")
    async with state.proxy() as data:
        data['way'].append('holidays')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


async def command_faq_holidays_group_input(message: types.Message, state: FSMContext):
    if message.text == "Я не знаю свою группу":
        await FSMfaq.holidays_1.set()
        async with state.proxy() as data:
            print(
                f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")
        await bot.send_message(message.from_user.id, emoji.emojize(faq_addSession_group_info),
                               reply_markup=only_to_main_menu_kb)
    elif message.text in [i[0] for i in groups.items()]:
        await FSMfaq.holidays_1.set()
        async with state.proxy() as data:
            data['way'].append('holidays_1')
            print(f"Ветка состояний: {data['way']}")
            print(
                f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")
            data['group'] = message.text
            await bot.send_message(message.from_user.id, emoji.emojize(f'Твоя группа: {data["group"]}\n'
                                                                       f':sunflower: Летние каникулы: {groups.get(message.text).get("summer_holidays")}\n'
                                                                       f':snowflake: Зимние каникулы: {groups.get(message.text).get("winter_holidays")}'),
                                   reply_markup=back_and_to_main_menu_kb)
    elif message.text not in [i[0] for i in groups.items()]:
        await bot.send_message(message.from_user.id, "Такой группы в моей базе нет!\nВведи еще раз.",
                               reply_markup=faq_addSession_department_group_input_kb_without_back_btn)


# сессии
async def command_faq_session(message: types.Message, state: FSMContext):
    await FSMfaq.session.set()
    await bot.send_message(message.from_user.id, faq_session_main_info, reply_markup=faq_session_kb)
    async with state.proxy() as data:
        data['way'].append('session')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


async def command_faq_common_session(message: types.Message, state: FSMContext):
    await FSMfaq.session_1.set()
    await bot.send_message(message.from_user.id, faq_common_session_info, reply_markup=back_and_to_main_menu_kb)
    async with state.proxy() as data:
        data['way'].append('session_1')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


async def command_faq_add_session(message: types.Message, state: FSMContext):
    await FSMfaq.session_1.set()
    await bot.send_message(message.from_user.id, faq_addSession_info, reply_markup=faq_addSession_choice_kb)
    async with state.proxy() as data:
        data['way'].append('session_1')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


async def command_faq_addsession_department_choice(message: types.Message, state: FSMContext):
    await FSMfaq.session_2.set()
    await bot.send_message(message.from_user.id, faq_addSession_department_info,
                           reply_markup=faq_addSession_department_group_input_kb)
    async with state.proxy() as data:
        data['way'].append('session_2')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


async def command_faq_addsession_group_input(message: types.Message, state: FSMContext):
    if message.text == "Я не знаю свою группу":
        await FSMfaq.session_3.set()
        await bot.send_message(message.from_user.id, emoji.emojize(faq_addSession_group_info),
                               reply_markup=only_to_main_menu_kb)
    elif message.text in [i[0] for i in groups.items()]:
        await FSMfaq.session_3.set()
        async with state.proxy() as data:
            data['way'].append('session_3')
            print(f"Ветка состояний: {data['way']}")
            print(
                f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")
            data['group'] = message.text
            await bot.send_message(message.from_user.id, f'*Твоя группа:* {data["group"]}\n'
                                                         f'*Твой деканат:* деканат факультета/института '
                                                         f'{groups.get(message.text).get("Institute")}.\n\n'
                                                         f'Если ты не знаешь, как до него добраться, воспользуйся разделом'
                                                         f' *"Навигация по корпусу"* на главном экране.',
                                   reply_markup=back_and_to_main_menu_kb, parse_mode='Markdown')
    elif message.text not in [i[0] for i in groups.items()]:
        await bot.send_message(message.from_user.id, "Такой группы в моей базе нет!\nВведи еще раз.",
                               reply_markup=faq_addSession_department_group_input_kb_without_back_btn)


# стипендии
async def command_faq_scholarship(message: types.Message, state: FSMContext):
    await FSMfaq.scholarship.set()
    await bot.send_message(message.from_user.id, faq_scholarship_choice, reply_markup=faq_scholarship_choice_kb)
    async with state.proxy() as data:
        data['way'].append('scholarship')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


async def command_faq_increased_scholarship(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, faq_waiting_for_doc, reply_markup=faq_empty_kb)
    await bot.send_document(message.from_user.id,
                            document=open("resources/docs/increased_scholarship/Заявление.docx", 'rb'))
    await bot.send_document(message.from_user.id,
                            document=open("resources/docs/increased_scholarship/Карта_претендента.docx", 'rb'))
    await bot.send_document(message.from_user.id,
                            document=open("resources/docs/increased_scholarship/Регламент.pdf", 'rb'))
    await bot.send_message(message.from_user.id, faq_scholarship_increased_scholarship_info,
                           reply_markup=back_and_to_main_menu_kb)
    await FSMfaq.scholarship_1.set()
    async with state.proxy() as data:
        data['way'].append('scholarship_1')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


async def command_faq_common_scholarship(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, faq_waiting_for_doc, reply_markup=faq_empty_kb)
    await bot.send_document(message.from_user.id,
                            document=open("resources/docs/common_scholarship/Приказ о размере стипендий.pdf", 'rb'))
    await bot.send_message(message.from_user.id, faq_scholarship_common_scholarship_info,
                           reply_markup=back_and_to_main_menu_kb)
    await FSMfaq.scholarship_1.set()
    async with state.proxy() as data:
        data['way'].append('scholarship_1')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


async def command_faq_social_scholarship(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, faq_waiting_for_doc, reply_markup=faq_empty_kb)
    await bot.send_document(message.from_user.id,
                            document=open("resources/docs/social_scholarship/Положение о назначении стипендий.pdf",
                                          'rb'))
    await bot.send_document(message.from_user.id,
                            document=open("resources/docs/common_scholarship/Приказ о размере стипендий.pdf", 'rb'))
    await bot.send_message(message.from_user.id, faq_scholarship_social_scholarship_info,
                           reply_markup=back_and_to_main_menu_kb, parse_mode="Markdown")
    await FSMfaq.scholarship_1.set()
    async with state.proxy() as data:
        data['way'].append('scholarship_1')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


# военка
async def command_faq_military_department_choice(message: types.Message, state: FSMContext):
    await FSMfaq.militaryDep.set()
    await bot.send_message(message.from_user.id, faq_militaryDep_info_choice, reply_markup=faq_militaryDep_choice)
    async with state.proxy() as data:
        data['way'].append('militaryDep')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


async def command_faq_military_department_centre(message: types.Message, state: FSMContext):
    await FSMfaq.militaryDep_1.set()
    await bot.send_message(message.from_user.id, faq_militaryDep_info_centre, reply_markup=back_and_to_main_menu_kb)
    async with state.proxy() as data:
        data['way'].append('militaryDep_1')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


async def command_faq_military_department_table(message: types.Message, state: FSMContext):
    await FSMfaq.militaryDep_1.set()
    await bot.send_message(message.from_user.id, faq_militaryDep_info_table, reply_markup=back_and_to_main_menu_kb)
    async with state.proxy() as data:
        data['way'].append('militaryDep_1')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


# общежития
async def command_faq_dormitory(message: types.Message, state: FSMContext):
    await FSMfaq.dormitory.set()
    await bot.send_message(message.from_user.id, faq_dormitory_main_info, reply_markup=faq_dormitory_choice_kb,
                           parse_mode="Markdown")
    async with state.proxy() as data:
        data['way'].append('dormitory')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


async def command_faq_dormitory_1st(message: types.Message, state: FSMContext):
    await FSMfaq.dormitory_1.set()
    await message.reply(faq_dormitory_1st_info, reply_markup=back_and_to_main_menu_kb,
                        parse_mode="Markdown")
    async with state.proxy() as data:
        data['way'].append('dormitory_1')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


async def command_faq_dormitory_2nd(message: types.Message, state: FSMContext):
    await FSMfaq.dormitory_1.set()
    await message.reply(faq_dormitory_2nd_info, reply_markup=back_and_to_main_menu_kb,
                        parse_mode="Markdown")
    async with state.proxy() as data:
        data['way'].append('dormitory_1')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


async def command_faq_dormitory_3rd(message: types.Message, state: FSMContext):
    await FSMfaq.dormitory_1.set()
    await message.reply(faq_dormitory_3rd_info, reply_markup=back_and_to_main_menu_kb,
                        parse_mode="Markdown")
    async with state.proxy() as data:
        data['way'].append('dormitory_1')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


async def command_faq_dormitory_4th(message: types.Message, state: FSMContext):
    await FSMfaq.dormitory_1.set()
    await message.reply(faq_dormitory_4th_info, reply_markup=back_and_to_main_menu_kb,
                        parse_mode="Markdown")
    async with state.proxy() as data:
        data['way'].append('dormitory_1')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


async def command_faq_dormitory_5th(message: types.Message, state: FSMContext):
    await FSMfaq.dormitory_1.set()
    await message.reply(faq_dormitory_5th_info, reply_markup=back_and_to_main_menu_kb,
                        parse_mode="Markdown")
    async with state.proxy() as data:
        data['way'].append('dormitory_1')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


async def command_faq_dormitory_pay_info(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, faq_waiting_for_doc, reply_markup=faq_empty_kb)
    await bot.send_document(message.from_user.id,
                            document=open('resources/docs/dormitory_pay/Размеры платы за проживание.pdf', 'rb'))
    await bot.send_photo(message.from_user.id,
                         open('resources/docs/dormitory_pay/Бланк квитанции на оплату.jpg', 'rb'),
                         'Квитанция об оплате')
    await message.reply(faq_dormitory_pay_info, reply_markup=back_and_to_main_menu_kb, parse_mode="Markdown")
    await FSMfaq.dormitory_1.set()
    async with state.proxy() as data:
        data['way'].append('dormitory_1')
        print(f"Ветка состояний: {data['way']}")
        print(
            f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


# Выход из состояний
async def to_start_faq(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    print(
        f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")
    await bot.send_message(message.from_user.id, "Возвращаю на главную", reply_markup=mainMenu_kb)


# кнопка "назад"
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
        elif data['way'][-1] == 'faq_start':
            await FSMfaq.faq_start.set()
            await bot.send_message(message.from_user.id, faq_start_phrase, reply_markup=faq_main_kb)
            print(
                f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")
        elif data['way'][-1] == 'holidays':
            await FSMfaq.holidays.set()
            await bot.send_message(message.from_user.id, faq_holiday_main_info)
            await bot.send_message(message.from_user.id, faq_holiday_info_individual,
                                   reply_markup=faq_addSession_department_group_input_kb, parse_mode='Markdown')
            print(
                f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")
        elif data['way'][-1] == 'scholarship':
            await FSMfaq.scholarship.set()
            await bot.send_message(message.from_user.id, faq_scholarship_choice, reply_markup=faq_scholarship_choice_kb)
            print(
                f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")
        elif data['way'][-1] == 'scholarship_1':
            await FSMfaq.scholarship_1.set()
            await bot.send_message(message.from_user.id, faq_scholarship_choice, reply_markup=faq_scholarship_choice_kb)
            print(
                f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")
        elif data['way'][-1] == 'dormitory':
            await FSMfaq.dormitory.set()
            await bot.send_message(message.from_user.id, faq_dormitory_main_info,
                                   reply_markup=faq_dormitory_choice_kb)
            print(
                f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")
        elif data['way'][-1] == 'dormitory_1':
            await FSMfaq.dormitory_1.set()
            await bot.send_message(message.from_user.id, faq_dormitory_main_info,
                                   reply_markup=back_and_to_main_menu_kb)
            print(
                f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")
        elif data['way'][-1] == 'militaryDep':
            await FSMfaq.militaryDep.set()
            await bot.send_message(message.from_user.id, faq_militaryDep_info_choice,
                                   reply_markup=faq_militaryDep_choice)
            print(
                f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")
        elif data['way'][-1] == 'militaryDep_1':
            await FSMfaq.militaryDep_1.set()
            await bot.send_message(message.from_user.id, faq_militaryDep_info_choice,
                                   reply_markup=back_and_to_main_menu_kb)
            print(
                f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")
        elif data['way'][-1] == 'session':
            await FSMfaq.session.set()
            await bot.send_message(message.from_user.id, faq_session_main_info, reply_markup=faq_session_kb)
            print(
                f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")
        elif data['way'][-1] == 'session_1':
            await FSMfaq.session_1.set()
            await bot.send_message(message.from_user.id, faq_addSession_info,
                                   reply_markup=faq_addSession_choice_kb)
            print(
                f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")
        elif data['way'][-1] == 'session_2':
            await FSMfaq.session_2.set()
            await bot.send_message(message.from_user.id, faq_addSession_department_info,
                                   reply_markup=faq_addSession_department_group_input_kb)
            print(
                f"Нынешнее состояние для юзера [{message.from_user.username}] с id [{message.from_user.id}]: {await state.get_state()}\n")


# команда для обработки неизвестных сообщений
async def unknown_command_faq(message: types.Message):
    await bot.send_message(message.from_user.id, "Неизвестная команда")


# регистрация хендлеров
def register_handlers_faq(dp: Dispatcher):
    dp.register_message_handler(on_back_faq, Text(equals='Назад', ignore_case=True),
                                state=[i for i in FSMfaq.all_states])
    dp.register_message_handler(to_start_faq, Text(equals='Вернуться на главный экран', ignore_case=True),
                                state=[i for i in FSMfaq.all_states])
    dp.register_message_handler(command_faq_start, Text(equals='FAQ', ignore_case=True), state=None)

    # каникулы
    dp.register_message_handler(command_faq_holidays_choice_group,
                                Text(equals='Каникулы', ignore_case=True),
                                state=FSMfaq.faq_start)
    dp.register_message_handler(command_faq_holidays_group_input, state=FSMfaq.holidays)

    # сессия
    dp.register_message_handler(command_faq_session, Text(equals='Сессия', ignore_case=True),
                                state=FSMfaq.faq_start)
    dp.register_message_handler(command_faq_common_session, Text(equals='Обычная сессия', ignore_case=True),
                                state=FSMfaq.session)
    dp.register_message_handler(command_faq_add_session, Text(equals='Дополнительная сессия', ignore_case=True),
                                state=FSMfaq.session)
    dp.register_message_handler(command_faq_addsession_department_choice,
                                Text(equals='Какой у меня деканат?', ignore_case=True),
                                state=FSMfaq.session_1)
    dp.register_message_handler(command_faq_addsession_group_input, state=FSMfaq.session_2)

    # стипендия
    dp.register_message_handler(command_faq_scholarship, Text(equals='Стипендия', ignore_case=True),
                                state=FSMfaq.faq_start)
    dp.register_message_handler(command_faq_increased_scholarship, Text(equals='ПГАС', ignore_case=True),
                                state=FSMfaq.scholarship)
    dp.register_message_handler(command_faq_common_scholarship,
                                Text(equals='Академическая стипендия', ignore_case=True),
                                state=FSMfaq.scholarship)
    dp.register_message_handler(command_faq_social_scholarship,
                                Text(equals='Социальная стипендия', ignore_case=True), state=FSMfaq.scholarship)

    # военка
    dp.register_message_handler(command_faq_military_department_choice,
                                Text(equals='Военная кафедра', ignore_case=True),
                                state=FSMfaq.faq_start)
    dp.register_message_handler(command_faq_military_department_centre,
                                Text(equals='Военно-учебный центр', ignore_case=True),
                                state=FSMfaq.militaryDep)
    dp.register_message_handler(command_faq_military_department_table,
                                Text(equals='Военно-учетный стол', ignore_case=True),
                                state=FSMfaq.militaryDep)

    # общежития
    dp.register_message_handler(command_faq_dormitory, Text(equals='Общежития', ignore_case=True),
                                state=FSMfaq.faq_start)
    dp.register_message_handler(command_faq_dormitory_1st, Text(equals='Общежитие №1', ignore_case=True),
                                state=FSMfaq.dormitory)
    dp.register_message_handler(command_faq_dormitory_2nd, Text(equals='Общежитие №2', ignore_case=True),
                                state=FSMfaq.dormitory)
    dp.register_message_handler(command_faq_dormitory_3rd, Text(equals='Общежитие №3', ignore_case=True),
                                state=FSMfaq.dormitory)
    dp.register_message_handler(command_faq_dormitory_4th, Text(equals='Общежитие №4', ignore_case=True),
                                state=FSMfaq.dormitory)
    dp.register_message_handler(command_faq_dormitory_5th, Text(equals='Общежитие №5', ignore_case=True),
                                state=FSMfaq.dormitory)
    dp.register_message_handler(command_faq_dormitory_pay_info, Text(equals='Оплата проживания', ignore_case=True),
                                state=FSMfaq.dormitory)

    # должна быть в конце
    dp.register_message_handler(unknown_command_faq, state=[i for i in FSMfaq.all_states])
