# общее
from create_bot import bot
from aiogram import types, Dispatcher
import collections
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

# фразы
from phrases.navi_phrases import *

# клавиатуры
from keyboards.navi_kbs import *
from keyboards.common_kbs_and_btns import *
from keyboards.main_menu_kbs import *

# словари
from dicts.graf import graf
from dicts.implementation import *

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
    async with state.proxy() as data:
        await bot.send_message(message.from_user.id,
                               "Искомый путь: от аудитории " + str(data['from']) + " до " + str(data['to']))
    await FSMnavi.next()


async def to_start(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(message.from_user.id, "Окей, на главную", reply_markup=mainMenu_kb)


async def on_back(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if len(data['way']) != 0:
            data['way'].pop()

        if len(data['way']) == 0:
            current_state = await state.get_state()
            if current_state is None:
                return
            await state.finish()
            await bot.send_message(message.from_user.id, "Окей, на главную", reply_markup=mainMenu_kb)
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


class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


def searcher(graph, start):
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True
