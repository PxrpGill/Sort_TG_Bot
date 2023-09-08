import telebot
from telebot import types

import algorithm
import time


token_bot = 'Ваш-ключ'
bot = telebot.TeleBot(token=token_bot)

# Начальное сообщение при запуске.
MESSAGE_START = (
    'Привет! Я бот,'
    ' который производит сортировку следующими методами:\n\n'
    'Обменом, Вставками, Выбором, Быстрой,'
    ' Пирамидальной, Шелла, Слиянием.\n\n'
    'Каким методом будем сортировать?'
)

# Сообщение выбора сортировок.
MESSAGE_CHOICE_SIZE = (
    'Хорошо! Выбери размер массива:\n\n'
    '1000, 10000, 100000, 150000'
)

# Кнопки видов сортировок.
markup_1 = types.ReplyKeyboardMarkup()
btn_1 = types.KeyboardButton('Обменом')
btn_2 = types.KeyboardButton('Вставками')
markup_1.row(btn_1, btn_2)
btn_3 = types.KeyboardButton('Выбором')
btn_4 = types.KeyboardButton('Быстрой')
markup_1.row(btn_3, btn_4)
btn_5 = types.KeyboardButton('Пирамидальной')
btn_6 = types.KeyboardButton('Шелла')
markup_1.row(btn_5, btn_6)
btn_7 = types.KeyboardButton('Слиянием')
btn_8 = types.KeyboardButton('Деревом')
markup_1.row(btn_7, btn_8)

# Кнопки размеров массива.
markup_2 = types.ReplyKeyboardMarkup()
btn_size_1000 = types.KeyboardButton('1000')
btn_size_10000 = types.KeyboardButton('10000')
btn_size_100000 = types.KeyboardButton('100000')
btn_size_150000 = types.KeyboardButton('150000')
markup_2.row(btn_size_1000)
markup_2.row(btn_size_10000)
markup_2.row(btn_size_100000)
markup_2.row(btn_size_150000)


@bot.message_handler(commands=['start'])
def main(message):
    """Стартовая функция."""
    bot.send_message(message.chat.id, MESSAGE_START, reply_markup=markup_1)
    bot.register_next_step_handler(message, on_click)


@bot.message_handler(func=lambda message: True)
def on_click(message):
    """Отслеживание нажатия."""
    bot.send_message(message.chat.id, MESSAGE_CHOICE_SIZE, reply_markup=markup_2)
    if message.text == 'Обменом':
        bot.register_next_step_handler(message, on_click_sizer_bubble_sort)
    elif message.text == 'Вставками':
        bot.register_next_step_handler(message, on_click_sizer_insert_sort)
    elif message.text == 'Выбором':
        bot.register_next_step_handler(message, on_click_sizer_selection_sort)
    elif message.text == 'Быстрой':
        bot.register_next_step_handler(message, on_click_sizer_quick_sort)
    elif message.text == 'Пирамидальной':
        bot.register_next_step_handler(message, on_click_sizer_heap_sort)
    elif message.text == 'Шелла':
        bot.register_next_step_handler(message, on_click_sizer_shell_sort)
    elif message.text == 'Слиянием':
        bot.register_next_step_handler(message, on_click_sizer_merge_sort)
    else:
        bot.send_message(message.chat.id, 'Такой сортировки не знаю :(', reply_markup=markup_1)


def on_click_sizer_bubble_sort(message):
    """Функция обработки BubbleSort."""
    bot.send_message(message.chat.id, 'Начинаю сортировать!')

    size = int(message.text)
    my_object = algorithm.BubbleSort(size)
    sort_type = type(my_object).__name__

    start_time = time.time()
    sorted_massive = my_object.do_sort()

    if start_time > 2:
        bot.send_message(message.chat.id, 'Ща, погоди, еще сортирую...')

    end_time = time.time()
    execution_time = end_time - start_time

    info = algorithm.InfoMessage(sorted_massive, size, sort_type, execution_time)
    info_message = info.get_message()

    print(sorted_massive)
    print(sort_type)
    print()

    bot.send_message(message.chat.id, info_message, reply_markup=markup_1)


def on_click_sizer_insert_sort(message):
    """Функция обработки InsertSort."""
    bot.send_message(message.chat.id, 'Начинаю сортировать!')

    size = int(message.text)
    my_object = algorithm.InsertSort(size)
    sort_type = type(my_object).__name__

    start_time = time.time()
    sorted_massive = my_object.do_sort()

    if start_time > 2:
        bot.send_message(message.chat.id, 'Ща, погоди, еще сортирую...')

    end_time = time.time()
    execution_time = end_time - start_time

    info = algorithm.InfoMessage(sorted_massive, size, sort_type, execution_time)
    info_message = info.get_message()

    print(sorted_massive)
    print(sort_type)

    bot.send_message(message.chat.id, info_message, reply_markup=markup_1)


def on_click_sizer_selection_sort(message):
    """Функция обработки SelectionSort."""
    bot.send_message(message.chat.id, 'Начинаю сортировать!')

    size = int(message.text)
    my_object = algorithm.SelectionSort(size)
    sort_type = type(my_object).__name__

    start_time = time.time()
    sorted_massive = my_object.do_sort()

    if start_time > 2:
        bot.send_message(message.chat.id, 'Ща, погоди, еще сортирую...')

    end_time = time.time()
    execution_time = end_time - start_time

    info = algorithm.InfoMessage(sorted_massive, size, sort_type, execution_time)
    info_message = info.get_message()

    print(sorted_massive)
    print(sort_type)

    bot.send_message(message.chat.id, info_message, reply_markup=markup_1)


def on_click_sizer_quick_sort(message):
    """Функция обработки QuickSort."""
    bot.send_message(message.chat.id, 'Начинаю сортировать!')

    size = int(message.text)
    my_object = algorithm.QuickSort(size)
    sort_type = type(my_object).__name__

    start_time = time.time()
    sorted_massive = my_object.do_sort()

    if start_time > 2:
        bot.send_message(message.chat.id, 'Ща, погоди, еще сортирую...')

    end_time = time.time()
    execution_time = end_time - start_time

    info = algorithm.InfoMessage(sorted_massive, size, sort_type, execution_time)
    info_message = info.get_message()

    print(sorted_massive)
    print(sort_type)

    bot.send_message(message.chat.id, info_message, reply_markup=markup_1)


def on_click_sizer_heap_sort(message):
    """Функция обработки HeapSort."""
    bot.send_message(message.chat.id, 'Начинаю сортировать!')

    size = int(message.text)
    my_object = algorithm.HeapSort(size)
    sort_type = type(my_object).__name__

    start_time = time.time()
    sorted_massive = my_object.do_sort()

    if start_time > 2:
        bot.send_message(message.chat.id, 'Ща, погоди, еще сортирую...')

    end_time = time.time()
    execution_time = end_time - start_time

    info = algorithm.InfoMessage(sorted_massive, size, sort_type, execution_time)
    info_message = info.get_message()

    print(sorted_massive)
    print(sort_type)

    bot.send_message(message.chat.id, info_message, reply_markup=markup_1)


def on_click_sizer_shell_sort(message):
    """Функция обработки ShellSort."""
    bot.send_message(message.chat.id, 'Начинаю сортировать!')

    size = int(message.text)
    my_object = algorithm.ShellSort(size)
    sort_type = type(my_object).__name__

    start_time = time.time()
    sorted_massive = my_object.do_sort()

    if start_time > 2:
        bot.send_message(message.chat.id, 'Ща, погоди, еще сортирую...')

    end_time = time.time()
    execution_time = end_time - start_time

    info = algorithm.InfoMessage(sorted_massive, size, sort_type, execution_time)
    info_message = info.get_message()

    print(sorted_massive)
    print(sort_type)

    bot.send_message(message.chat.id, info_message, reply_markup=markup_1)


def on_click_sizer_merge_sort(message):
    """Функция обработки MergeSort."""
    bot.send_message(message.chat.id, 'Начинаю сортировать!')

    size = int(message.text)
    my_object = algorithm.MergeSort(size)
    sort_type = type(my_object).__name__

    start_time = time.time()
    sorted_massive = my_object.do_sort()

    if start_time > 2:
        bot.send_message(message.chat.id, 'Ща, погоди, еще сортирую...')

    end_time = time.time()
    execution_time = end_time - start_time

    info = algorithm.InfoMessage(sorted_massive, size, sort_type, execution_time)
    info_message = info.get_message()

    print(sorted_massive)
    print(sort_type)

    bot.send_message(message.chat.id, info_message, reply_markup=markup_1)


# Метод, позволяющий непрерывно работать боту.
bot.polling(none_stop=True)
