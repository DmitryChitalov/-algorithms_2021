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
from random import randint
from prof import my_profile
import requests
from memory_profiler import profile
from itertools import islice
import requests.utils
from decimal import Decimal

from numpy import array, append


# У меня есть свой декоратор для таких случаев. Правда, я не использую совсем так как врет, но в эту реализацию добавим.
# Нужно также учитывать, что запускать их лучше поотдельности, иначе будет смущать вывод
# Первой возьмем наивную реализацию исследования файла и вывода инфо из него по условию.

# @my_profile
@profile
def data_seek(_data):
    with open('data_s.txt', 'w+') as f:
        f.write(_data.content.decode('utf-8'))
        f.seek(0)
        data_s_my = [tuple([x.split()[0], x.split()[5], x.split()[6]]) for x in f]
    return data_s_my[:100]


# Profiling:          <data_seek>  RSS: 983.04kB | VMS: 393.22kB | time:  146.3ms

"""Line #    Mem usage    Increment  Occurences   Line Contents 
============================================================ 30     54.4 MiB     54.4 MiB           1   @my_profile 
31                                         @profile 32                                         def data_seek(_data): 
33     54.5 MiB      0.1 MiB           1       with open('data_s.txt', 'w+') as f: 34     54.5 MiB      0.0 MiB       
    1           f.write(_data.content.decode('utf-8')) 35     54.5 MiB      0.0 MiB           1           f.seek(0) 
    36     69.1 MiB     14.6 MiB       51465           data_s_my = [tuple([x.split()[0], x.split()[5], x.split()[6]]) 
    for x in f] 37     69.1 MiB      0.0 MiB           1       return data_s_my[:100] 

"""


# Видим, что Lc дает инкремент, ну тогда заменим его на генератор

# @my_profile
@profile
def data_seek_1(_data):
    with open('data_s.txt', 'w+') as f:
        f.write(_data.content.decode('utf-8'))
        f.seek(0)
        data_s_my = (tuple([x.split()[0], x.split()[5], x.split()[6]]) for x in f)
    return islice(data_s_my, 100)


# Profiling:        <data_seek_1>  RSS:       0B | VMS:       0B | time:  48.92ms
"""Line #    Mem usage    Increment  Occurences   Line Contents 
============================================================ 63     56.7 MiB     56.7 MiB           1   @profile 64   
                                      def data_seek_1(_data): 65     56.7 MiB      0.0 MiB           1       with 
                                      open('data_s.txt', 'w+') as f: 66     56.7 MiB      0.0 MiB           1         
                                        f.write(_data.content.decode('utf-8')) 67     56.7 MiB      0.0 MiB           
                                        1           f.seek(0) 68     56.7 MiB      0.0 MiB           1           
                                        data_s_my = (tuple([x.split()[0], x.split()[5], x.split()[6]]) for x in f) 69 
                                            56.7 MiB      0.0 MiB           1       return islice(data_s_my, 100) 

"""


# Видим, что Increment фактически полностью удалось убрать на моменте lc. Время исполнения тоже сократилось втрое
# Больше тут оптимизировать нечего
#######################################################################################################################

def find_info(list_i, str_i):
    for ind, val in enumerate(list_i):
        if str_i in val:
            return ind


@profile
def currency_rates(cur):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    data = response.content.decode(encoding=encodings)
    data_cleaned = data.partition('ket">')[2].partition('</ValCurs>')[0].split('<Valute ID=')
    final = list(zip(list(map(lambda x: x.partition('<CharCode>')[2].partition('</CharCode>')[0], data_cleaned)),
                     list(map(lambda x: x.partition('<Nominal>')[2].partition('</Nominal>')[0], data_cleaned)),
                     list(map(lambda x: x.partition('<Name>')[2].partition('</Name>')[0], data_cleaned)),
                     list(map(lambda x: x.partition('<Value>')[2].partition('</Value>')[0].replace(',', '.'),
                              data_cleaned))))
    if find_info(final, cur.upper()) is None:
        return None
    else:
        return f'1 {final[find_info(final, cur.upper())][2]} = {(Decimal(final[find_info(final, cur.upper())][3]) / Decimal(final[find_info(final, cur.upper())][1])).quantize(Decimal("0.01"))} руб. '


# Profiling:     <currency_rates>  RSS: 835.58kB | VMS: 327.68kB | time: 273.35ms
"""Line #    Mem usage    Increment  Occurences   Line Contents 
============================================================ 100     45.1 MiB     45.1 MiB           1   @profile 101 
                                        def currency_rates(cur): 102     45.8 MiB      0.7 MiB           1       
                                        response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp') 103     
                                        45.8 MiB      0.0 MiB           1       encodings = 
                                        requests.utils.get_encoding_from_headers(response.headers) 104     45.8 MiB   
                                           0.0 MiB           1       data = response.content.decode(
                                           encoding=encodings) 105     45.8 MiB      0.1 MiB           1       
                                           data_cleaned = data.partition('ket">')[2].partition('</ValCurs>')[
                                           0].split('<Valute ID=') 106     45.8 MiB      0.0 MiB          72       
                                           final = list(zip(list(map(lambda x: x.partition('<CharCode>')[
                                           2].partition('</CharCode>')[0], data_cleaned)), 107     45.8 MiB      0.0 
                                           MiB          71                        list(map(lambda x: x.partition(
                                           '<Nominal>')[2].partition('</Nominal>')[0], data_cleaned)), 108     45.8 
                                           MiB      0.0 MiB          71                        list(map(lambda x: 
                                           x.partition('<Name>')[2].partition('</Name>')[0], data_cleaned)), 
                                           109     45.8 MiB      0.0 MiB          72                        list(map(
                                           lambda x: x.partition('<Value>')[2].partition('</Value>')[0].replace(',', 
                                           '.'), 110     45.8 MiB      0.0 MiB           1                            
                                                data_cleaned)))) 111     45.8 MiB      0.0 MiB           1       if 
                                                find_info(final, cur.upper()) is None: 112                            
                                                                     return None 113                                  
                                                                                else: 114     45.9 MiB      0.1 MiB   
                                                                                        1           return f'1 {
                                                                                        final[find_info(final, 
                                                                                        cur.upper())][2]} = {(
                                                                                        Decimal(final[find_info(
                                                                                        final, cur.upper())][3]) / 
                                                                                        Decimal(final[find_info(
                                                                                        final, cur.upper())][
                                                                                        1])).quantize(Decimal(
                                                                                        "0.01"))} руб. ' """


# Потенциал для опитимизации совсем небольшой, попробуем убрать content, оставив только строку из ответа


@my_profile
def currency_rates_1(cur):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    data_cleaned = response.partition('ket">')[2].partition('</ValCurs>')[0].split('<Valute ID=')
    final = list(zip(list(map(lambda x: x.partition('<CharCode>')[2].partition('</CharCode>')[0], data_cleaned)),
                     list(map(lambda x: x.partition('<Nominal>')[2].partition('</Nominal>')[0], data_cleaned)),
                     list(map(lambda x: x.partition('<Name>')[2].partition('</Name>')[0], data_cleaned)),
                     list(map(lambda x: x.partition('<Value>')[2].partition('</Value>')[0].replace(',', '.'),
                              data_cleaned))))
    if find_info(final, cur.upper()) is None:
        return None
    else:
        return f'1 {final[find_info(final, cur.upper())][2]} = {(Decimal(final[find_info(final, cur.upper())][3]) / Decimal(final[find_info(final, cur.upper())][1])).quantize(Decimal("0.01"))} руб. '


# Profiling:   <currency_rates_1>  RSS:       0B | VMS:       0B | time: 227.64ms
"""Line #    Mem usage    Increment  Occurences   Line Contents 
============================================================ 117     45.9 MiB     45.9 MiB           1   @profile 118 
def currency_rates_1(cur): 119     45.9 MiB      0.0 MiB           1 response = requests.get(
'http://www.cbr.ru/scripts/XML_daily.asp').text 120 # encodings = requests.utils.get_encoding_from_headers(
response.headers) 121                                             # data = response.content.decode(
encoding=encodings) 122     45.9 MiB      0.0 MiB           1       data_cleaned = response.partition('ket">')[
2].partition('</ValCurs>')[0].split('<Valute ID=') 123     45.9 MiB      0.0 MiB          72       final = list(zip(
list(map(lambda x: x.partition('<CharCode>')[2].partition('</CharCode>')[0], data_cleaned)), 124     45.9 MiB      
0.0 MiB          71                        list(map(lambda x: x.partition('<Nominal>')[2].partition('</Nominal>')[0], 
data_cleaned)), 125     45.9 MiB      0.0 MiB          71                        list(map(lambda x: x.partition(
'<Name>')[2].partition('</Name>')[0], data_cleaned)), 126     45.9 MiB      0.0 MiB          72                       
 list(map(lambda x: x.partition('<Value>')[2].partition('</Value>')[0].replace(',', '.'), 127     45.9 MiB      0.0 
 MiB           1                                 data_cleaned)))) 128     45.9 MiB      0.0 MiB           1       if 
 find_info(final, cur.upper()) is None: 129                                                 return None 130           
                                   else: 131     45.9 MiB      0.0 MiB           1           return f'1 {final[
                                   find_info(final, cur.upper())][2]} = {(Decimal(final[find_info(final, 
                                   cur.upper())][3]) / Decimal(final[find_info(final, cur.upper())][1])).quantize(
                                   Decimal("0.01"))} руб. ' """
# Итого, слегка ускорили, а также убрали почти полностью икремент на разборе content от requests

########################################################################################################################
"""
Задача из данного курса. Вывести индексы четных чисел массива
"""


@my_profile
def evens_ind(arr):
    evens = []
    for e, m in enumerate(arr):
        if not m % 2:
            evens.append(e)
    return evens


# Profiling:          <evens_ind>  RSS: 282.62kB | VMS: 536.58kB | time:   0.82ms
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   185     85.5 MiB     85.5 MiB           1   @profile
   186                                         def evens_ind(arr):
   187     85.5 MiB      0.0 MiB           1       evens = []
   188     85.6 MiB      0.0 MiB       10001       for e, m in enumerate(arr):
   189     85.6 MiB      0.1 MiB       10000           if not m % 2:
   190     85.6 MiB      0.0 MiB        5101               evens.append(e)
   191     85.6 MiB      0.0 MiB           1       return evens
"""


# тут есть несколько потенциальных улучшений. Заменим массив на массив numpy, грохнем изначальный лист, превратив его
# в генератор, уберем вычисления, заменив на побитовые
@profile
def evens_ind_1(arr):
    evens = array([])
    for e, m in enumerate(arr):
        if not m & 1:
            append(evens, e)
    return evens


# Profiling:        <evens_ind_1>  RSS:       0B | VMS:       0B | time:    0.0ms
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   212     69.0 MiB     69.0 MiB           1   @profile
   213                                         def evens_ind_1(arr):
   214     69.0 MiB      0.0 MiB           1       evens = array([])
   215     69.0 MiB      0.0 MiB           1       for e, m in enumerate(arr):
   216                                                 if not m & 1:
   217                                                     append(evens, e)
   218     69.0 MiB      0.0 MiB           1       return evens
"""


# Ну тут все, больше оптимизировать нечего. Выполнение мгновенное, использование памяти срезано до предела

#####################################################################################################################
# Осталось попробовать слоты


class HexNumber:
    def __init__(self, num):
        self.num = int(num, 16)

    def __add__(self, other):
        return format(self.num + other.num, 'X')

    @profile
    def __mul__(self, other):
        return format(self.num * other.num, 'X')


# Profiling:            <__mul__>  RSS:   8.19kB | VMS:       0B | time:   0.01ms
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   254     88.8 MiB     88.8 MiB           1       @profile
   255                                             def __mul__(self, other):
   256     88.8 MiB      0.0 MiB           1           return format(self.num * other.num, 'X')
"""


# Тут очень маленький объем и все же попробуем slots
class HexNumber1:
    __slots__ = 'num'

    def __init__(self, num):
        self.num = int(num, 16)

    def __add__(self, other):
        return format(self.num + other.num, 'X')

    @profile
    def __mul__(self, other):
        return format(self.num * other.num, 'X')
# Profiling:            <__mul__>  RSS:       0B | VMS:       0B | time:    0.0ms
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   280     68.6 MiB     68.6 MiB           1       @profile
   281                                             def __mul__(self, other):
   282     68.6 MiB      0.0 MiB           1           return format(self.num * other.num, 'X')
"""

# Хороший способ, я о нем не знал! буду пользоваться обязательно
# Мы рассмотрели почти все способы оптимизации памяти и несколько других, менее значимых, написали декоратор
if __name__ == '__main__':
    data = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
    data_seek(data)
    data_seek_1(data)
    print(currency_rates('uSD'))
    print(currency_rates_1('uSD'))
    _array = (randint(0, 100000) for i in range(10000))
    evens_ind(_array)
    evens_ind_1(_array)
    m = HexNumber('7D0') * HexNumber('186A0')
    v = HexNumber1('7D0') * HexNumber1('186A0')
