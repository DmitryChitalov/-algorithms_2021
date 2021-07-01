"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
import json
from pympler import asizeof
from memory_profiler import memory_usage
from random import randint, choice
from timeit import default_timer
from recordclass import recordclass


def time_mem_decor(func):
    def wrapper(n=10000):
        time_start = default_timer()
        mem_start = memory_usage()
        res = func(n)
        time_diff = default_timer() - time_start
        mem_diff = memory_usage()[0] - mem_start[0]
        print(f'Время  "{func.__name__}": {time_diff}')
        print(f'Память "{func.__name__}": {mem_diff}')
        return res

    return wrapper


# Из курса основ. Урок 2, задача 3.
# 1 - до оптимизации
number = randint(1, 12)

seasons_dict = {'winter': [12, 1, 2],
                'spring': [3, 4, 5],
                'summer': [6, 7, 8],
                'fall': [9, 10, 11]}

for key, value in seasons_dict.items():
    if number in value:
        break  # print(f"It is {key}")

# 1 - оптимизация
seasons_dict_opti = json.dumps({'winter': [12, 1, 2],
                                'spring': [3, 4, 5],
                                'summer': [6, 7, 8],
                                'fall': [9, 10, 11]})

seasons_dict_opti_out = json.loads(seasons_dict_opti).items()
for key, value in seasons_dict_opti_out:
    if number in value:
        break  # print(f"It is {key}")

print('#1')
print('Dict:                ', asizeof.asizeof(seasons_dict))
print('JSON.dumps:          ', asizeof.asizeof(seasons_dict_opti), '\n')

'''
#1
Dict:                 608
JSON.dumps:           112

Словарь сезонов упакован в json формат.
Размер уменьшился более, чем в 5 раз.
'''

# Из курса основ. Урок 2, задача 6*.
print('#2')


@time_mem_decor
def get_goods(n=10000):
    goods = []
    # while True:
    for i in range(n):
        # print("Enter\033[1m Q\033[0;0m if you have finished entering data.")
        # my_good = input("Enter name, price, count, unit of your good separated by whitespaces: ")
        # if my_good.lower() == "q":
        #     break
        my_good = f'name_{i + 1} {randint(100, 10000)} {randint(0, 20)} {choice(["шт.", "уп.", "кг"])}'.split()
        my_dict = {"name": my_good[0], "price": int(my_good[1]), "count": int(my_good[2]), "unit": my_good[3]}
        my_tuple = (i, my_dict)
        goods.append(my_tuple)

    return goods


@time_mem_decor
def get_goods_opti_json(n=10000):
    goods = []

    for i in range(n):
        my_good = f'name_{i + 1} {randint(100, 10000)} {randint(0, 20)} {choice(["шт.", "уп.", "кг"])}'.split()
        my_dict = {"name": my_good[0], "price": int(my_good[1]), "count": int(my_good[2]), "unit": my_good[3]}
        goods.append((i, my_dict))
    goods_dumped = json.dumps(goods)
    return goods_dumped


@time_mem_decor
def get_goods_opti_rc(n=100000):
    goods = []
    record_dict = recordclass('record_dict', ('name', 'price', 'count', 'unit'))

    for i in range(n):
        my_good = f'name_{i + 1} {randint(100, 10000)} {randint(0, 20)} {choice(["шт.", "уп.", "кг"])}'.split()
        my_dict = record_dict(name=my_good[0],
                              price=int(my_good[1]),
                              count=int(my_good[2]),
                              unit=my_good[3])
        goods.append((i, my_dict))
    return goods


get_goods()
get_goods_opti_json()
get_goods_opti_rc()
print()

'''
#2
Время  "get_goods": 0.24008955600000004
Память "get_goods": 2.76171875
Время  "get_goods_opti_json": 0.2544414049999999
Память "get_goods_opti_json": 1.1796875
Время  "get_goods_opti_rc": 0.2543035920000001
Память "get_goods_opti_rc": 0.60546875


Третье место занимает список с кортежами,
Второе место - сериализация с помощью JSON:
    ~ в 2,5 раза меньше списка с кортежами
Первое место у recordclass: 
    ~ в 2 раза меньше JSON и
    ~ в 4,5 раза меньше списка кортежей.
    
Время у всех примерно одинаковое, так как все данные заполнены через цикл.
'''

# Из курса основ. Урок 6, задача 2.
# 3 - до оптимизации
print('#3')


class Road:
    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self._thickness = thickness

    def mass(self):
        mass = self._length * self._width * 25 * self._thickness
        print(f"{round(mass / 1000)} tons required.")


a = Road(20, 5000, 5)
print('Объект класса без __slots__:', asizeof.asizeof(a))


# 3 - оптимизация. __slots__
class Road:
    __slots__ = ['length', 'width', 'thickness']

    def __init__(self, length, width, thickness):
        self.length = length
        self.width = width
        self.thickness = thickness

    def mass(self):
        mass = self.length * self.width * 25 * self.thickness
        print(f"{round(mass / 1000)} tons required.")


a = Road(20, 5000, 5)
print('Объект класса  с  __slots__:', asizeof.asizeof(a))
'''
#3
Объект класса без __slots__: 240
Объект класса  с  __slots__: 80

При помощи __slots__ сократили объём используемой памяти в 3 раза
'''
