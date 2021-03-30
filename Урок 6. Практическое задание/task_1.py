"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import memory_usage, profile
from random import randint
from timeit import default_timer
from pympler import asizeof
import json
import collections


# Скрипт 1. Придумал на ходу, чтоб проверить разницу между append, генератором и lc
print('\n---=== 1 ===---\n')
LIST_LENGHT = 100000
MIN_NUM = 1
MAX_NUM = 10


def mem_time_profiler(func):
    def wrapper(*args, **kwargs):
        mem_start = memory_usage()[0]
        time_start = default_timer()
        result = func(*args, **kwargs)
        total_mem = memory_usage()[0] - mem_start
        total_time = default_timer() - time_start
        print(f'Memory: {total_mem}. Time: {total_time}')
        return result
    return wrapper

@mem_time_profiler
def rand_list(list_lenght, min_num, max_num):
    """
    Функция генерирует список, заполенный случайными целыми числами
    :param list_lenght: длина списка
    :param min_num: минимальное случайное число
    :param max_num : максимальное случайное число
    """
    my_list = []
    for i in range(list_lenght):
        my_list.append(randint(min_num, max_num))
    return my_list

@mem_time_profiler
def rand_list_gen(list_lenght, min_num, max_num):
    """
    Генератор генерирует список, заполенный случайными целыми числами
    :param list_lenght: длина списка
    :param min_num: минимальное случайное число
    :param max_num : максимальное случайное число
    """
    for i in range(list_lenght):
        yield randint(min_num, max_num)

@mem_time_profiler
def rand_list_lc(list_lenght, min_num, max_num):
    """
    LC генерирует список, заполенный случайными целыми числами
    :param list_lenght: длина списка
    :param min_num: минимальное случайное число
    :param max_num : максимальное случайное число
    """
    lc_list = (randint(min_num, max_num) for _ in range(list_lenght))
    return lc_list

print('rand_list: ', end='')
list_list = rand_list(LIST_LENGHT, MIN_NUM, MAX_NUM)
# print(f'rand_list: {list_list}')

print('rand_list_gen: ', end='')
list_gen = rand_list_gen(LIST_LENGHT, MIN_NUM, MAX_NUM)
# for i in list_gen:
#     print(f'{i}, ', end='')
# print()

print('rand_list_lc: ', end='')
list_lc = rand_list_lc(LIST_LENGHT, MIN_NUM, MAX_NUM)
# for i in list_lc:
#     print(f'{i}, ', end='')
# print()

"""
Результаты:
rand_list: Memory: 1.1484375. Time: 0.200019345
rand_list_gen: Memory: 0.00390625. Time: 0.099668329
rand_list_lc: Memory: 0.0. Time: 0.099988678

Видно, что прожорливый append использует много процессорного времени, а готовый список занимат память
Генератор и list comprehention единтичны в плане скорости выполнения, но LC почти не занимает память.
Генератор тоже занимает ничтожно мало памяти, т.к. хранит только текущую переменную и свое состояние.
"""

# Скрипт 2 взят из задания 4, урока 1. Скрипт видоизменен для сохранения в json и упрощен
print('\n---=== 2 ===---\n')

accounts = {
    'kas': ['qwerty', True],
    'heromarine': ['qwe123', True],
    'rogue': ['Qwerty111', True],
    'serral': ['qwe', True],
    'kaby': ['asd12', True],
    'basset': ['qax123', False],
    'dark': ['zaq', False],
    'jaedong': ['qwer321', False],
    'parting': ['Asd1', True],
    'reynor': ['zxcv123', True],
}

with open('accounts.json', 'w', encoding='utf-8') as f:
    json.dump(accounts, f)

# user_name_input = input('Введите имя пользователя: ')
user_name_input = 'kaby'

# первый алгоритм O(n)

@profile
def check_user_1(user_name, user_pass):   # не будем передавать имя словаря, функция будет работать только с accounts{}
    """
    не будем парить пользователю мозги запросами ввода логина и пароля
    :param user_name: kaby
    :param user_pass: asd12
    :return:
    """
    with open('accounts.json', 'r') as f:
        accounts = json.load(f)
        if accounts[user_name][0] != user_pass:
            print('неправильный логин/пароль')
        elif not accounts[user_name][1]:
            print('учетная запись не активирована')
        elif accounts[user_name][0] == user_pass and accounts[user_name][1]:
            print('доступ разрешен')


print(check_user_1('kaby', 'asd12'))

@profile
def check_user_2(user_name, user_pass):     # O(1)
    if accounts[user_name][0] != user_pass:
        print('неправильный логин/пароль')
    elif not accounts[user_name][1]:
        print('учетная запись не активирована')
    elif accounts[user_name][0] == user_pass and accounts[user_name][1]:
        print('доступ разрешен')

print(check_user_2('kaby', 'asd12'))

print(f'Размер json: {asizeof.asizeof(json.dumps(accounts))}')
print(f'Размер dict: {asizeof.asizeof(accounts)}')

"""
Размер json: 328
Размер dict: 2272

Алгоритмы идентичны. Инкремент в обоих случаях слишком мал для замеров 0.0
Но json занимает в 7 раз меньше места в памяти
"""

# Скрипт 2 взят из задания 2, урока 1.
print('\n---=== 3 ===---\n')

class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im > 0:
            return f'{self.re} + {self.im}i'
        else:
            return f'{self.re} - {abs(self.im)}i'

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)


class ComplexNumberOptimized:
    __slots__ = ['re', 'im']

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im > 0:
            return f'{self.re} + {self.im}i'
        else:
            return f'{self.re} - {abs(self.im)}i'

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)


print('Задача 3')
cmplx_num = ComplexNumber(7, 8)
print(cmplx_num.__dict__)
print('Размер экземпляра класса со словарем:', asizeof.asizeof(cmplx_num))  # 328

cmplx_num = ComplexNumberOptimized(8, 7)
print(cmplx_num.__slots__)
print('Размер экземпляра класса со слотом:', asizeof.asizeof(cmplx_num))  # 112

"""
Размер экземпляра класса со словарем: 328
Размер экземпляра класса со слотом: 112
Использование слота уменьшило размер в три раза
"""
