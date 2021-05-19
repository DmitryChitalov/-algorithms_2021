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

import memory_profiler
from random import randint
from itertools import cycle
from time import sleep
from pympler import asizeof
from numpy import array
from timeit import default_timer, timeit


def decor(func):  # Декоратор доработан
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        res = func(args[0])
        time_diff = default_timer() - start_time
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff, time_diff

    return wrapper


################################### Script 1 ###################################
print('################################### Script 1 ###################################')


#  Во втором задании к четвертому уроку курса "Основ" я заполнял список через list comprehension.

#  Задание:
#  Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

#  Решим задачу его через генератор и сравним использование памяти.

@decor
def selector(some_data):
    base_list = [randint(0, 1000) for i in range(1000000)]
    return [base_list[i + 1] for i in range(len(base_list) - 1) if base_list[i + 1] > base_list[i]]


@decor
def selector1(some_data):
    base_gen = (randint(0, 1000) for i in range(1000000))
    prev = next(base_gen)
    res = []
    nxt = next(base_gen)
    for i in range(999998):
        if nxt > prev:
            res.append(nxt)
        prev, nxt = nxt, next(base_gen)
    return res


print('Исходный скрипт (память):', selector('some_input')[1])
print('Новый скрипт (память):', selector1('some_input')[1])

print('Исходный скрипт (время):', selector('some_input')[2])
print('Новый скрипт (время):', selector1('some_input')[2])

'''
Результаты профилирования памяти:
Исходный скрипт: 28.453125
Новый скрипт: 17.16015625

Мы видим, что использование генератора здесь снижает затраты памяти в полтора раза.

Результаты профилирования памяти:
Исходный скрипт (время): 1.3980072999999997
Новый скрипт (время): 1.1479558

Кроме того, мы имееемы небольшой выигрыш по времени на большинстве запусков.

А значит, оптимизация имеет место)
'''

################################### Script 2 ###################################
print('################################### Script 2 ###################################')


#  В первой задаче шестого урока курса "Оновы языка Python" был написан следующий класс(Имитатор светофора)
#  Создадим экземпляр класса и замерим его:


class TrafficLight:  # Создать класс TrafficLight (светофор)

    def __init__(self, color):  # Определить у него один атрибут color (цвет)
        self.__color = color.lower()
        self.__t_colors = {'red': 7, 'yellow': 3, 'green': 3}

    def running(self):
        times_to_stop = 10
        order = list(self.__t_colors.keys()) + ['yellow']
        our_index = order.index(self.__color)
        another_list = order[our_index:] + order[:our_index]
        for i in cycle(another_list):
            if not times_to_stop:
                break
            print(i.capitalize())
            times_to_stop -= 1
            sleep(self.__t_colors[i])


t = TrafficLight('red')
print('Размер элемента класса:', asizeof.asizeof((t)))
print('Словарь класса:', t.__dict__)


class TrafficLight:  # Создать класс TrafficLight (светофор)
    __slots__ = 'color', 't_colors'

    def __init__(self, color):  # Определить у него один атрибут color (цвет)
        self.color = color.lower()
        self.t_colors = {'red': 7, 'yellow': 3, 'green': 3}

    def running(self):
        times_to_stop = 10
        order = list(self.t_colors.keys()) + ['yellow']
        our_index = order.index(self.color)
        another_list = order[our_index:] + order[:our_index]
        for i in cycle(another_list):
            if not times_to_stop:
                break
            print(i.capitalize())
            times_to_stop -= 1
            sleep(self.t_colors[i])


t = TrafficLight('red')
print('Размер элемента класса:', asizeof.asizeof((t)))
print('Слоты класса:', t.__slots__)

'''
Результаты профилирования:
Размер элемента класса: 816
Словарь класса: {'_TrafficLight__color': 'red', '_TrafficLight__t_colors': {'red': 7, 'yellow': 3, 'green': 3}}
Размер элемента класса: 568
Слоты класса: ('color', 't_colors')

Видим, что слоты дают существенную выгоду в размере экземплярова класса. Обратной стороной медали естественно будет 
отсутствие возможности добавить атрибут.

Оптимизация проведена)
'''

################################### Script 3 ###################################
print('################################### Script 3 ###################################')


#  Задачу с решетом эратосфена я реализовал вот так:

@decor
def eratosthenes(i):  # сложность O(log(log(n))), если я все правильно сделал) Так на занятии сказали)
    numbers = [_ for _ in range(10000)]
    numbers[1] = 0
    count = 0
    for n in numbers:
        if n:
            for _ in range(n + 2, len(numbers)):
                if numbers[_] % n == 0:
                    numbers[_] = 0
            count += 1
            if count == i:
                return n


print('Затраты памяти при поиске сотого элемента при использовании списка:', eratosthenes(100)[1])
print('Затраты времени при поиске сотого элемента при использовании списка:', eratosthenes(100)[2])


#  Теперь применим array из numpy:

@decor
def eratosthenes1(i):  # сложность O(log(log(n))), если я все правильно сделал) Так на занятии сказали)
    numbers = array([_ for _ in range(10000)])
    numbers[1] = 0
    count = 0
    for n in numbers:
        if n:
            for _ in range(n + 2, len(numbers)):
                if numbers[_] % n == 0:
                    numbers[_] = 0
            count += 1
            if count == i:
                return n


print('Затраты памяти при поиске сотого элемента при использовании array:', eratosthenes1(100)[1])
print('Затраты времени при поиске сотого элемента при использовании array:', eratosthenes1(100)[2])

'''
Результаты профилирования:

Затраты памяти при поиске сотого элемента при использовании списка: 0.12890625
Затраты времени при поиске сотого элемента при использовании списка: 0.2652884999999987
Затраты памяти при поиске сотого элемента при использовании array: 0.01171875
Затраты времени при поиске сотого элемента при использовании array: 0.7023651999999991

Мы убедились, что array из numpy показывает себя в разы эффективнее по памяти, чем простой список.
Оптимизация более чем удалась) Однако со временем тут обратная история. Менее прожорливый по памяти работает в три раза 
дольше. Итог, выбираем реализацию исходя из наших ресурсов.
'''
################################### Script 4 ###################################
print('################################### Script 4 ###################################')


#  Рассмотрим рекурсивный алгоритм из задания 2 второго урока, перепишем через цикл и замерим его.

#  Старый код:

def numbers():
    number = input('Введите натуральное число: ')
    if not number.isdigit() or not int(number):  # После этого остаются только натуральные числа. Последним отсекаем '0'
        print('Вы должны были ввести натуральное число. Попробуйте еще раз.')
        return numbers()
    return even_odd(int(number))


@decor
def wrap(number):
    def even_odd(number):
        values = [0, 0]
        if not number // 10:
            if number % 2:
                values[1] += 1
            else:
                values[0] += 1
            return values
        return tuple(x + y for x, y in zip(even_odd(number // 10), even_odd(number % 10)))

    return even_odd(number)


@decor
def even_odd1(number):
    values = [0, 0]
    while number:
        if number % 10 % 2:
            values[1] += 1
        else:
            values[0] += 1
        number = number // 10
    return values


a = 1
for i in range(200):
    a *= randint(2, 1000)

print('Затраты памяти при решении задачи старым способом:', wrap(a)[1])
print('Затраты памяти при решении задачи новым способом:', even_odd1(a)[1])
print('Затраты времени при решении задачи старым способом:', wrap(a)[2])
print('Затраты времени при решении задачи новым способом:', even_odd1(a)[2])

'''
Результаты профилирования:

Затраты памяти при решении задачи старым способом: 0.5390625
Затраты памяти при решении задачи новым способом: 0.0
Затраты времени при решении задачи старым способом: 0.003068900000000596
Затраты времени при решении задачи новым способом: 0.0006637000000004889

Решение без рекурсии оптимальнее и по памяти и по времени. Что говорит нам о том, чтобы не использовать ее без 
необходимости. 
'''