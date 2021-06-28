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
from ast import dump
from memory_profiler import memory_usage
import numpy as np
from memory_profiler import profile


"""Скрипт принимает число и вставляет его на своё место в последовательности"""


@profile
def number_ins_1(user_rate_number):
    # user_rate_number = int(input('Input the rate number: '))
    # my_list = [7, 5, 3, 3, 2]
    my_list = [i for i in range(100000)]
    my_list2 = my_list.copy()
    trigger = True

    for i in range(len(my_list)):
        if user_rate_number > my_list[i]:
            my_list2.insert(i, user_rate_number)
            trigger = False
            break
    if trigger:
        my_list2.reverse()
        for i in range(len(my_list)):
            if user_rate_number <= my_list2[i]:
                my_list2.insert(i, user_rate_number)
                break
        my_list2.reverse()
    # return my_list2
    return None


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    30     30.1 MiB     30.1 MiB           1   @profile
    31                                         def number_ins_1(user_rate_number):
    32                                             # user_rate_number = int(input('Input the rate number: '))
    33                                             # my_list = [7, 5, 3, 3, 2]
    34     34.2 MiB      4.1 MiB      100003       my_list = [i for i in range(100000)]
    35     35.0 MiB      0.8 MiB           1       my_list2 = my_list.copy()
    36     35.0 MiB      0.0 MiB           1       trigger = True
    37
    38     35.0 MiB      0.0 MiB           1       for i in range(len(my_list)):
    39     35.0 MiB      0.0 MiB           1           if user_rate_number > my_list[i]:
    40     35.7 MiB      0.8 MiB           1               my_list2.insert(i, user_rate_number)
    41     35.7 MiB      0.0 MiB           1               trigger = False
    42     35.7 MiB      0.0 MiB           1               break
    43     35.7 MiB      0.0 MiB           1       if trigger:
    44                                                 my_list2.reverse()
    45                                                 for i in range(len(my_list)):
    46                                                     if user_rate_number <= my_list2[i]:
    47                                                         my_list2.insert(i, user_rate_number)     
    48                                                         break
    49                                                 my_list2.reverse()
    50                                             # return my_list2
    51     35.7 MiB      0.0 MiB           1       return None

Из профиля памяти в строке 34 видно создание списка, и затраты на n-ый объем памяти, затем
копия. Можно применить массив из библиотеки numpy, это даст меньший объем занимаемой памяти.
"""

@profile
def number_ins_2(user_rate_number):
    # user_rate_number = int(input('Input the rate number: '))
    # my_list = [7, 5, 3, 3, 2]
    my_list = np.array([i for i in range(100000)])
    my_list2 = my_list.copy()
    trigger = True

    for i in range(len(my_list)):
        if user_rate_number > my_list[i]:
            np.insert(my_list2, user_rate_number, i)
            trigger = False
            break
    if trigger:
        my_list2.reverse()
        for i in range(len(my_list)):
            if user_rate_number <= my_list2[i]:
                np.insert(my_list2, user_rate_number, i)
                break
        my_list2.reverse()
    # return my_list2
    return None


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    84     30.8 MiB     30.8 MiB           1   @profile
    85                                         def number_ins_2(user_rate_number):
    86                                             # user_rate_number = int(input('Input the rate number: '))
    87                                             # my_list = [7, 5, 3, 3, 2]
    88     34.1 MiB      1.2 MiB      100003       my_list = np.array([i for i in range(100000)])       
    89     32.0 MiB     -2.1 MiB           1       my_list2 = my_list.copy()
    90     32.0 MiB      0.0 MiB           1       trigger = True
    91
    92     32.0 MiB      0.0 MiB           1       for i in range(len(my_list)):
    93     32.0 MiB      0.0 MiB           1           if user_rate_number > my_list[i]:
    94     32.0 MiB      0.0 MiB           1               np.insert(my_list2, user_rate_number, i)     
    95     32.0 MiB      0.0 MiB           1               trigger = False
    96     32.0 MiB      0.0 MiB           1               break
    97     32.0 MiB      0.0 MiB           1       if trigger:
    98                                                 my_list2.reverse()
    99                                                 for i in range(len(my_list)):
   100                                                     if user_rate_number <= my_list2[i]:
   101                                                         np.insert(my_list2, user_rate_number, i) 
   102                                                         break
   103                                                 my_list2.reverse()
   104                                             # return my_list2
   105     32.0 MiB      0.0 MiB           1       return None

После использования массива из библиотеки numpy видно что расход памяти снизился не значительно, но
при создании копии объем уменьшился на 3 MiB. Это можно увидеть в строке 89.
"""


@profile
def number_ins_3(user_rate_number):
    # user_rate_number = int(input('Input the rate number: '))
    # my_list = [7, 5, 3, 3, 2]
    my_list = tuple([i for i in range(100000)])
    my_list2 = np.array(my_list)
    trigger = True

    for i in range(len(my_list)):
        if user_rate_number > my_list[i]:
            np.insert(my_list2, user_rate_number, i)
            trigger = False
            break
    if trigger:
        my_list2.reverse()
        for i in range(len(my_list)):
            if user_rate_number <= my_list2[i]:
                np.insert(my_list2, user_rate_number, i)
                break
        my_list2.reverse()
    # return my_list2
    return None


number_ins_1(11)
number_ins_2(11)
number_ins_3(11)

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   141     31.3 MiB     31.3 MiB           1   @profile
   142                                         def number_ins_3(user_rate_number):
   143                                             # user_rate_number = int(input('Input the rate number: '))
   144                                             # my_list = [7, 5, 3, 3, 2]
   145     34.5 MiB      2.9 MiB      100003       my_list = tuple([i for i in range(100000)])
   146     34.6 MiB      0.1 MiB           1       my_list2 = np.array(my_list)
   147     34.6 MiB      0.0 MiB           1       trigger = True
   148
   149     34.6 MiB      0.0 MiB           1       for i in range(len(my_list)):
   150     34.6 MiB      0.0 MiB           1           if user_rate_number > my_list[i]:
   151     34.9 MiB      0.4 MiB           1               np.insert(my_list2, user_rate_number, i)     
   152     34.9 MiB      0.0 MiB           1               trigger = False
   153     34.9 MiB      0.0 MiB           1               break
   154     34.9 MiB      0.0 MiB           1       if trigger:
   155                                                 my_list2.reverse()
   156                                                 for i in range(len(my_list)):
   157                                                     if user_rate_number <= my_list2[i]:
   158                                                         np.insert(my_list2, user_rate_number, i) 
   159                                                         break
   160                                                 my_list2.reverse()
   161                                             # return my_list2
   162     34.9 MiB      0.0 MiB           1       return None

Так же я попробовал применить кортеж. По сравнению со списком и массивом кортеж занимает немного больше памяти,
это видно в строке 145.
"""

"""
Огромная таблица занимает много места на экране, а нам, по сути, надо только общее количество
памяти. Делаю свой декоратор для подсчета.
"""


def mem_dec(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()[0]
        func(*args, **kwargs)
        m2 = memory_usage()[0]
        print(f'Memory usage: {m2 - m1}')
    return wrapper


"""функция хранит профиль в словаре и возвращает его"""
@mem_dec
def user_profile(name, l_name, year, city, mail, phone):
    return f'PROFILE -- Name: {name}, Last name: {l_name}, Year of birth: {year}' \
        f'City: {city}, Mail: {mail}, Phone: {phone}'


user_profile(name='Sergey', l_name='Ryzhov', year='2020',
             city='Mogilev', mail='ryzhovs@tut.by', phone='+375447820890', )

"""Реализация через слоты-списки"""
class UserProfile:
    __slots__ = ['name', 'l_name', 'year', 'city', 'mail', 'phone']

    def __init__(self, name, l_name, year, city, mail, phone):
        self.name = name
        self.l_name = l_name
        self.year = year
        self.city = city
        self.mail = mail
        self.phone = phone

    @mem_dec
    def user_profile2(self):
        return f'PROFILE -- Name: {self.name}, Last name: {self.l_name}, Year of birth: {self.year}' \
            f'City: {self.city}, Mail: {self.mail}, Phone: {self.phone}'


u_p = UserProfile(name='Sergey', l_name='Ryzhov', year='2020',
                  city='Mogilev', mail='ryzhovs@tut.by', phone='+375447820890')
u_p.user_profile2()

"""
Memory usage:  0.00390625
Memory usage:  0.0
Реализация через слоты-списки занимает меньше памяти, что видно из замеров.
"""

"""Реализуем через слоты-кортежи"""

class UserProfile2:
    __slots__ = ('name', 'l_name', 'year', 'city', 'mail', 'phone')

    def __init__(self, name, l_name, year, city, mail, phone):
        self.name = name
        self.l_name = l_name
        self.year = year
        self.city = city
        self.mail = mail
        self.phone = phone

    @mem_dec
    def user_profile3(self):
        return f'PROFILE -- Name: {self.name}, Last name: {self.l_name}, Year of birth: {self.year}' \
            f'City: {self.city}, Mail: {self.mail}, Phone: {self.phone}'


u_p = UserProfile2(name='Sergey', l_name='Ryzhov', year='2020',
                  city='Mogilev', mail='ryzhovs@tut.by', phone='+375447820890')
u_p.user_profile3()

"""
Memory usage:  0.00390625
Memory usage:  0.0
Memory usage:  0.0
Реализация через слоты-кортежи, по идее, должна занимать ещё меньше памяти, на замерах не видно.
"""

"""скрипт собирает данные в словарь и лист"""
@mem_dec
def goods():
    goods_number = int(input('Input the quantity of goods for the data: '))
    goods_list = []
    goods_dict = {}
    stat_list = ['название', 'цена', 'количество', 'eд']

    for i in range(goods_number):
        for k in stat_list:
            goods_dict.update({k: input(f'Input the "{k}" of the good {i + 1}: ')})
        good_tuple = (i + 1, goods_dict.copy())
        goods_list.append(good_tuple)

goods()
"""
Без оптимизации цифры выглядят так.

Input the quantity of goods for the data: 2
Input the "название" of the good 1: g1
Input the "цена" of the good 1: 1
Input the "количество" of the good 1: 1
Input the "eд" of the good 1: q
Input the "название" of the good 2: g2
Input the "цена" of the good 2: 2
Input the "количество" of the good 2: 2
Input the "eд" of the good 2: q

Memory usage: 0.046875

В первой реализации сделаем хранение данных в формате json, удалим ссылки соответственно тоже.
"""
import json

@mem_dec
def goods():
    goods_number = int(input('Input the quantity of goods for the data: '))
    goods_list = []
    goods_dict = {}
    stat_list = ['название', 'цена', 'количество', 'eд']

    for i in range(goods_number):
        for k in stat_list:
            goods_dict.update({k: input(f'Input the "{k}" of the good {i + 1}: ')})
        good_tuple = (i + 1, goods_dict.copy())
        goods_list.append(good_tuple)
    dump_list = json.dumps(goods_list)
    dump_dict = json.dumps(goods_dict)
    del goods_list
    del goods_dict
    del goods_number
    del stat_list

goods()
"""
После оптимизации памяти должно было стать меньше, однако результат точно такой же.
Предполагаю что объем хранимой информации очень мал и элементарные операции занимают
именно столько места в памяти, изменения не значительны при малых объемах.

Input the quantity of goods for the data: 2
Input the "название" of the good 1: g1
Input the "цена" of the good 1: 1
Input the "количество" of the good 1: 1
Input the "eд" of the good 1: q
Input the "название" of the good 2: g2
Input the "цена" of the good 2: 2
Input the "количество" of the good 2: 2
Input the "eд" of the good 2: q

Memory usage: 0.046875
"""
"""Во второй реализации используем список из библиотеки numpy"""

@mem_dec
def goods():
    goods_number = int(input('Input the quantity of goods for the data: '))
    goods_list = np.array([])
    goods_dict = {}
    stat_list = ['название', 'цена', 'количество', 'eд']

    for i in range(goods_number):
        for k in stat_list:
            goods_dict.update({k: input(f'Input the "{k}" of the good {i + 1}: ')})
        good_tuple = (i + 1, goods_dict.copy())
        np.append(goods_list, good_tuple)

goods()

"""
Input the quantity of goods for the data: 2
Input the "название" of the good 1: g1
Input the "цена" of the good 1: 1
Input the "количество" of the good 1: 1
Input the "eд" of the good 1: q
Input the "название" of the good 2: g2
Input the "цена" of the good 2: 2
Input the "количество" of the good 2: 2
Input the "eд" of the good 2: q

Memory usage: 0.05859375

По результату ззамера видно что памяти съело немного больше, хотя опять же должно быть 
меньше, так как библиотека numpy используется более эффективно. Делаю ставку опять же
на объем данных. При больших данных ситуация будет другая.

Вывод: После профилирования по памяти и доработки скриптов вывод напрашивается
сам собой - при разработке ПО или скрипта в первую очередь нужно думать об
эффективности использования памяти и работе скрипта.
"""