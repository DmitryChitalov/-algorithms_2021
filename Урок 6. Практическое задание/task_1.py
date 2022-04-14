"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
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
from memory_profiler import profile, memory_usage
from numpy import array
from timeit import default_timer
import requests
from collections import Counter
import pickle
from pympler import asizeof
import gzip
import json

""" Тест 1. Заполнение списка"""


def code_eff(func):
    """Декоратор для профилирования времени и памяти функции"""

    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        t1 = default_timer()
        res = func(*args, **kwargs)
        m2 = memory_usage()
        t2 = default_timer()
        func_mem = m2[0] - m1[0]
        func_time = t2 - t1
        return res, func_time, func_mem

    return wrapper


@ profile
def fill_list1(num):
    res_list1 = [num for num in range(num)]
    return res_list1


@ profile
def fill_list2(i):
    res_list2 = (i for i in range(i))
    return res_list2


if __name__ == '__main__':

    fill_list1(10000)
    fill_list2(10000)


"""
Замеры проводились по каждой функции отдельно (вторая в момент запуска первой
функция комментировалась, для чистоты эксперимента). 
Для тестирования выбран скрипт из задания, автоматишчески заполняющий список 
с помощью list comprehension. Прирост памяти для хранения словаря составил 0,4 Mib.
Для оптимизации используемой памяти был использован генератор списка. Прирост памяти 
в этом случае составил 0. (Есть недостаток: Невозможность работы со списком.
Для работы со списком потребуется передать его функции list. 
Также представлены данные замеров с использованием созданного декоратора
профилирующего время и использование памяти. По времени оба варианта одинаково затратны,
а по памяти - использование генератора предпочтительнее. 

 


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    44     30.2 MiB     30.2 MiB           1   @ profile
    45                                         def fill_list1(num):
    46     30.6 MiB      0.4 MiB       10003       res_list1 = [num for num in range(num)]
    47     30.6 MiB      0.0 MiB           1       return res_list1
 
 
 
    
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    51     30.2 MiB     30.2 MiB           1   @ profile
    52                                         def fill_list2(i):
    53     30.2 MiB      0.0 MiB           1       res_list2 = (i for i in range(i))
    54     30.2 MiB      0.0 MiB           1       return res_list2   
   

Замеры с помощью декоратора 'code_eff':

Время выполнения функции fill_list1: 0.10920630000000009 и заняло: 0.53515625 Mib
Время выполнения функции fill_list2: 0.10468659999999996 и заняло: 0.00390625 Mib
"""

""" Тест 2. Заполнение словаря"""


@profile
def fill_dict1():
    test_dict1 = {}
    for i in range(10000):
        test_dict1[i] = i * 2
    return test_dict1


@profile
def fill_dict2():
    test_dict2 = ((i, i*2) for i in range(10000))
    return test_dict2


if __name__ == '__main__':

    fill_dict1()
    fill_dict2()


"""
Оптимизация используемой памяти при заполнении словаря, первоначально, через цикл for
и с аккумуляцией данных в реальном словаре, производится через генератор.
При необходимости работы с элементами словаря придется использовать функцию 'dict'
Основной инкремент памяти в функции fill_dict1 происходит за счет заполнения реального словаря.
Заменяя этот момент на генератор, мы можем оптимизировать использование памяти.


 
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   107     30.1 MiB     30.1 MiB           1   @profile
   108                                         def fill_dict1():
   109     30.1 MiB      0.0 MiB           1       test_dict1 = {}
   110     31.3 MiB      0.0 MiB       10001       for i in range(10000):
   111     31.3 MiB      1.2 MiB       10000           test_dict1[i] = i * 2
   112     31.3 MiB      0.0 MiB           1       return test_dict1


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   115     30.3 MiB     30.3 MiB           1   @profile
   116                                         def fill_dict2():
   117     30.3 MiB      0.0 MiB           1       test_dict2 = ((i, i*2) for i in range(10000))
   118     30.3 MiB      0.0 MiB           1       return test_dict2



Время выполнения функции fill_dict1: 0.11119219999999996 и заняло: 1.1640625 Mib
Время выполнения функции fill_dict2: 0.11086429999999992 и заняло: 0.00390625 Mib
"""


""" Тест 3. Из курса "Основы Python"   """


@profile
class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.comp_num = complex(a, b)

    def view_cn(self):
        return self.comp_num

    def __add__(self, other):
        cn = ComplexNum((self.a + other.a), (self.b + other.b))
        return cn

    def __mul__(self, other):
        cn = ComplexNum(((self.a * other.a) - (self.b * other.b)), ((self.b * other.a) + (self.a * other.b)))
        return cn


@profile
class ComplexNum1:
    __slots__ = ['a', 'b', 'comp_num']

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.comp_num = complex(a, b)

    def view_cn(self):
        return self.comp_num

    def __add__(self, other):
        cn = ComplexNum1((self.a + other.a), (self.b + other.b))
        return cn

    def __mul__(self, other):
        cn = ComplexNum1(((self.a * other.a) - (self.b * other.b)), ((self.b * other.a) + (self.a * other.b)))
        return cn


if __name__ == '__main__':
    cn = ComplexNum(3, 7)  # object size: 424
    print(f'object size: {asizeof.asizeof(cn)}')
    print(cn.__dict__)
    cn1 = ComplexNum1(3, 7)  # object size: 152
    print(f'object size: {asizeof.asizeof(cn1)}')
    print(cn1.__slots__)

"""
Параметры объекта класса при инициализации хранятся в словаре (хэш-таблица тебует больше памяти)
оптимизировать можно через конструкцию __slots__ и хранить в списке (как в примере)

object size: 424
{'a': 3, 'b': 7, 'comp_num': (3+7j)}
object size: 152
['a', 'b', 'comp_num']

Почти в 3 раза меньше памяти, если верить замерам

"""


""" Тест 4. Из курса "Основы Python"   """

# Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
# Далее определить IP с которого было больше всего заходов.


@profile
def spam_finder():
    response = requests.get(
        'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

    lines = response.text.split('\n')
    info_list = []
    for line in lines[:-1]:  # почему-то последний элемент был "пустая строка" (его отрезаем)
        sp_line = line.split()
        elem = (sp_line[0], sp_line[5][1:], sp_line[6])
        # print(elem)
        info_list.append(elem)

    # Делаем список только ip адресов
    address_list = []
    for el in info_list:
        address_list.append(el[0])

    # создаем счетчик ("элемент":кол-во вхождений)
    spam_list = Counter(address_list)
    # выявляем максимальное значение количества вхождений
    max_value = max(spam_list.values())
    # выявляем ключ (ip адрес) соответствующий максимальному значению
    spam_ip = {k: v for k, v in spam_list.items() if v == max_value}
    return spam_ip


@profile
def spam_finder2():

    file_path = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

    ip_list = (line.split()[0] for line in requests.get(file_path, stream=True).iter_lines())
    # создаем счетчик ("элемент":кол-во вхождений)
    spam_list = Counter(ip_list)
    # выявляем максимальное значение количества вхождений
    max_value = max(spam_list.values())
    # выявляем ключ (ip адрес) соответствующий максимальному значению
    spam_ip = {key: val for key, val in spam_list.items() if val == max_value}
    return spam_ip


if __name__ == '__main__':
    spam_ip = spam_finder()

"""
Что было сделано для оптимизации используемой памяти для кода spam_finder().
При замерах были выделены проблемные моменты:
1. высокий инкремент при создании объекта response
2. создание массива lines - высокий инкремент
3. создание списка  info_list

Что было предпринято:
выброшен из кода промежуточный этап получения списка кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
Сразу создавался ip_list, с помощью генератора, без создания отдельно объекта response, с построчным считыванием
информации. Автоматически убрался незначительный инкремент при создании объекта spam_list.


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   171     34.4 MiB     34.4 MiB           1   @profile
   172                                         def spammer_finder():
   173     44.3 MiB      9.8 MiB           2       response = requests.get(
   174     34.4 MiB      0.0 MiB           1           'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
   175                                         
   176     54.9 MiB     10.6 MiB           1       lines = response.text.split('\n')
   177     54.9 MiB      0.0 MiB           1       info_list = []
   178     70.2 MiB      0.4 MiB       51463       for line in lines[:-1]:  # почему-то последний элемент был "пустая строка" (его отрезаем)
   179     70.2 MiB     13.6 MiB       51462           sp_line = line.split()
   180     70.2 MiB      0.0 MiB       51462           elem = (sp_line[0], sp_line[5][1:], sp_line[6])
   181                                                 # print(elem)
   182     70.2 MiB      1.4 MiB       51462           info_list.append(elem)
   183                                         
   184                                             # Делаем список только ip адресов
   185     70.2 MiB      0.0 MiB           1       address_list = []
   186     70.2 MiB      0.0 MiB       51463       for el in info_list:
   187     70.2 MiB      0.0 MiB       51462           address_list.append(el[0])
   188                                         
   189                                             # создаем счетчик ("элемент":кол-во вхождений)
   190     70.3 MiB      0.1 MiB           1       spam_list = Counter(address_list)
   191                                             # выявляем максимальное значение количества вхождений
   192     70.3 MiB      0.0 MiB           1       max_value = max(spam_list.values())
   193                                             # выявляем ключ (ip адрес) соответствующий максимальному значению
   194     70.3 MiB      0.0 MiB        2663       spammer = {k: v for k, v in spam_list.items() if v == max_value}
   195     70.3 MiB      0.0 MiB           1       return spammer
   


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   271     35.0 MiB     35.0 MiB           1   @profile
   272                                         def spam_finder2():
   273                                         
   274     35.0 MiB      0.0 MiB           1       file_path = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
   275                                         
   276     40.5 MiB    -87.5 MiB      102927       ip_list = (line.split()[0] for line in requests.get(file_path, stream=True).iter_lines())
   277                                             # создаем счетчик ("элемент":кол-во вхождений)
   278     39.7 MiB     -0.8 MiB           1       spam_list = Counter(ip_list)
   279                                             # выявляем максимальное значение количества вхождений
   280     39.7 MiB      0.0 MiB           1       max_value = max(spam_list.values())
   281                                             # выявляем ключ (ip адрес) соответствующий максимальному значению
   282     39.7 MiB      0.0 MiB        2663       spam_ip = {key: val for key, val in spam_list.items() if val == max_value}
   283     39.7 MiB      0.0 MiB           1       return spam_ip






C использованием декоратора 'code_eff'
   
Время выполнения функции spammer_finder: 0.9069670000000001 и заняло: 4.36328125 Mib

Время выполнения функции spammer_finder: 0.9819920999999999  и заняло: 3.703125 Mib
"""
