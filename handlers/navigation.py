# общее
from create_bot import bot
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

# фразы
from phrases.navi_phrases import *

# клавиатуры
from keyboards.navi_kbs import navigation_kb, navigation_decanat_kb, navigation_department_kb, navigation_auditorium_kb, navigation_other_kb, clear_keyboard
from keyboards.common_kbs_and_btns import *
from keyboards.main_menu_kbs import *

# словари
from dicts.graf import graf
from dicts.cabs import cabs

#навигационные алгоритмы
from repository.implementation import *

example_graph = SimpleGraph()
example_graph.edges = graf

class FSMnavi(StatesGroup):
    navigation_start = State()  # начальный
    decanat = State()  # ввод деканата
    department = State()  # ввод кафедры
    auditorium = State()  # ввод искомой аудитории
    other = State()
    place_now = State()  # ввод местонахождения
    pathfinder = State()
    last_one = State()


async def navi_start(message: types.Message, state: FSMContext):
    await FSMnavi.navigation_start.set()
    await bot.send_message(message.from_user.id, navigation_start_phrase, reply_markup=navigation_kb)
    async with state.proxy() as data:
        # data['way'].clear
        data['way'] = ['start']


async def command_navigation_decanat(message: types.Message, state: FSMContext):
    await FSMnavi.decanat.set()
    await bot.send_message(message.from_user.id, navigation_decanat, reply_markup=navigation_decanat_kb)
    async with state.proxy() as data:
        data['way'].append('decanat')

    await FSMnavi.place_now.set()


async def command_navigation_department(message: types.Message, state: FSMContext):
    await FSMnavi.department.set()
    await bot.send_message(message.from_user.id, navigation_department, reply_markup=navigation_department_kb)
    async with state.proxy() as data:
        data['way'].append('department')

    await FSMnavi.place_now.set()


async def command_navigation_auditorium(message: types.Message, state: FSMContext):
    await FSMnavi.auditorium.set()
    await bot.send_message(message.from_user.id, navigation_auditorium, reply_markup=navigation_auditorium_kb)
    async with state.proxy() as data:
        data['way'].append('auditorium')

    await FSMnavi.place_now.set()


async def command_navigation_other(message: types.Message, state: FSMContext):
    await FSMnavi.other.set()
    await bot.send_message(message.from_user.id, navigation_other, reply_markup=navigation_other_kb)
    async with state.proxy() as data:
        data['way'].append('other')

    await FSMnavi.place_now.set()


async def command_place_now_get(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, navigation_get_place, reply_markup=clear_keyboard)
    async with state.proxy() as data:
        data['to'] = message.text
        data['way'].append('place_now')
    await FSMnavi.next()


async def command_get_way(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['from'] = message.text
        data['way'].append('get_way')
    ##Функция поиска пути
    ##Вывод результата

    check_result = check_points(data['from'], data['to'], graf)

    if check_result == "Маршрут построен":
        async with state.proxy() as data:
            if(data['from'][0].isnumeric() == True):
                await bot.send_message(message.from_user.id, "Искомый путь: от аудитории " + str(data['from']) + " до " + str(data['to']))
            else:
                await bot.send_message(message.from_user.id, "Искомый путь: от " + str(data['from']) + " до " + str(data['to']))
            await bot.send_message(message.from_user.id, str(check_result))
            came_from, cost_so_far = dijkstra_search(example_graph, data['from'], data['to'])

            path = reconstruct_path(came_from, data['from'], data['to'])

            path_stages = []

            for next in path:
                if cabs.get(next) not in path_stages:
                    path_stages.append(cabs.get(next))

            new_path = path_auditorium(path)

            #Вывод одним сообщением
            path_1 = ''
            for next in new_path:
                path_1+=str(next)+'\n'
            await bot.send_message(message.from_user.id, f'*{path_1}*',parse_mode='Markdown')
            await bot.send_message(message.from_user.id, "Маршрут завершен")
            await bot.send_message(message.from_user.id, "Для наглядности ниже представлены схемы нужных тебе этажей, "
                                                         "можешь дополнительно сориентироваться по ним.")

            '''Вывод в несколько сообщений
            for next in new_path:
                await bot.send_message(message.from_user.id, str(next))
            await bot.send_message(message.from_user.id, "Маршрут завершен")'''

            for next in path_stages:
                if (next == "0"):
                    await bot.send_photo(message.from_user.id, open("resources/images/0_floor.jpg", 'rb'), "Цокольный этаж")
                elif(next == "1"):
                    await bot.send_photo(message.from_user.id, open("resources/images/1_floor.jpg", 'rb'), "Первый этаж")
                elif (next == "2"):
                    await bot.send_photo(message.from_user.id, open("resources/images/2_floor.jpg", 'rb'), "Второй этаж")
                elif (next == "3"):
                    await bot.send_photo(message.from_user.id, open("resources/images/3_floor.jpg", 'rb'), "Третий этаж")
            await FSMnavi.next()
           #отладка графа
           #came_from_2 = breadth_first_search_1(example_graph, data['from'])
    else:
        await bot.send_message(message.from_user.id, str(check_result))
        await bot.send_message(message.from_user.id, "Попробуйте еще раз")
        async with state.proxy() as data:
            data['way'].pop()
    #await FSMnavi.next()


async def to_start(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(message.from_user.id, "Возвращаю на главную", reply_markup=mainMenu_kb)


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
            await FSMnavi.navigation_start.set()
            await bot.send_message(message.from_user.id, navigation_start_phrase, reply_markup=navigation_kb)
        elif data['way'][-1] == 'decanat':
            await FSMnavi.place_now.set()
            await bot.send_message(message.from_user.id, navigation_decanat, reply_markup=navigation_decanat_kb)
        elif data['way'][-1] == 'department':
            await FSMnavi.place_now.set()
            await bot.send_message(message.from_user.id, navigation_department, reply_markup=navigation_department_kb)
        elif data['way'][-1] == 'auditorium':
            await FSMnavi.place_now.set()
            await bot.send_message(message.from_user.id, navigation_auditorium, reply_markup=navigation_auditorium_kb)
        elif data['way'][-1] == 'other':
            await FSMnavi.place_now.set()
            await bot.send_message(message.from_user.id, navigation_other, reply_markup=navigation_other_kb)
        elif data['way'][-1] == 'place_now':
            await FSMnavi.pathfinder.set()
            await bot.send_message(message.from_user.id, navigation_get_place, reply_markup=clear_keyboard)
        elif data['way'][-1] == 'get_way':
            await FSMnavi.place_now.set()
            await bot.send_message(message.from_user.id, navigation_get_place, reply_markup=clear_keyboard)


def register_handlers_navigation(dp: Dispatcher):
    dp.register_message_handler(to_start, Text(equals='Вернуться на главный экран', ignore_case=True),
                                state=[i for i in FSMnavi.all_states])
    dp.register_message_handler(on_back, Text(equals='Назад', ignore_case=True), state=[i for i in FSMnavi.all_states])
    dp.register_message_handler(navi_start, Text(equals='Навигация по корпусу', ignore_case=True), state=None)
    dp.register_message_handler(command_navigation_decanat, Text(equals='Поиск деканата', ignore_case=True),
                                state=FSMnavi.navigation_start)
    dp.register_message_handler(command_navigation_department, Text(equals='Поиск кафедры', ignore_case=True),
                                state=FSMnavi.navigation_start)
    dp.register_message_handler(command_navigation_auditorium, Text(equals='Поиск аудитории', ignore_case=True),
                                state=FSMnavi.navigation_start)
    dp.register_message_handler(command_navigation_other, Text(equals='Другое', ignore_case=True),
                                state=FSMnavi.navigation_start)
    dp.register_message_handler(command_place_now_get, state=FSMnavi.place_now)
    dp.register_message_handler(command_get_way, state=FSMnavi.pathfinder)








