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
import numpy as np
from memory_profiler import profile

companies = {
    'Роснефть': 708,
    'Газпром': 1203,
    'Лукойл': 640,
    'Сбербанк России': 845,
    'Российские железные дороги': 156,
    'Ростех': 179
}

@profile
def richCompany1():
    values_list = list(companies.values())
    companis_list = list(companies.items())
    keys_list = list(companies.keys())
    revers_companies={}
    for i in range(len(values_list) - 1):           
        revers_companies[values_list[i]] = keys_list[i]
        keys_companies = sorted(revers_companies, reverse=True)[:3]
    for company in keys_companies:                   
        print(revers_companies[company])


@profile
def richCompany2():
    companis_list = list(companies.items())
    values_list = list(companies.values())
    for i in range(len(values_list) - 1):
        firstTree = 0
        for j in range(len(values_list) - 1): 
            if (values_list[i] < values_list[j]): 
                firstTree += 1
        if(firstTree < 3):
            print(companis_list[i])

richCompany1()  
richCompany2()  
# Нет расхождений по памяти, хоть и зависимостей больше во 2ом варианте

##########################################################################
from collections import Counter 

@profile
def inter_fabric1(count_f,i = 0, fabrisc = Counter({})): 
    if i == count_f:
        min_fab = []
        max_fab = []
        print(fabrisc)
        mid = sum(fabrisc.values())/count_f
        print(f"Среднегодовая прибыль всех предприятий: {mid}")
        for key, vals in list(fabrisc.items()): 
            if vals > mid:
                max_fab.append(key)
            else:
                min_fab.append(key)
        print(f"Предприятия, с прибылью выше среднего значения {max_fab}")
        print(f"Предприятия, с прибылью ниже среднего значения {min_fab}")
    else:
        fabric_name = input('Введите название предприятия: ')
        fabric_frofit = input('через пробел введите прибыль данного предприятия: ')
        year_profit = sum(list(map(lambda x: int(x), fabric_frofit.split())))
        fabrisc.update({fabric_frofit:year_profit})
        i = i+1
        inter_fabric1(count_f, i, fabrisc)      

@profile
def inter_fabric2(count_f,i = 0, fabrisc = Counter({})): 
    if i == count_f:
        max_fab = []
        mid = sum(fabrisc.values())/count_f
        print(f"Среднегодовая прибыль всех предприятий: {mid}")
        for key, vals in list(fabrisc.items()): 
            if vals > mid:
                fabrisc.pop(key)
                max_fab.append(key)
        print(f"Предприятия, с прибылью выше среднего значения {max_fab}")
        print(f"Предприятия, с прибылью ниже среднего значения {fabrisc}")
    else:
        fabric_name = input('Введите название предприятия: ')
        fabric_frofit = input('через пробел введите прибыль данного предприятия: ')
        year_profit = sum(list(map(lambda x: int(x), fabric_frofit.split())))
        fabrisc.update({fabric_frofit:year_profit})
        i = i+ 1
        inter_fabric2(count_f, i, fabrisc)       

inter_fabric1(int(input('Введите количество предприятий: ')))
inter_fabric2(int(input('Введите количество предприятий: ')))
# во второй функции убрал одну переменную и else, стало меньше зависимостей, но по памяти нет различий
#################################################################################
import secrets
import hashlib

salt = secrets.token_hex(8)
dict_url1 = {}
dict_url2 = {}

@profile
def unique_url1(uri):
  if uri not in dict_url1:
    dict_url1[uri] = hashlib.md5(salt.encode() + uri.encode()).hexdigest()
    
unique_url1('https://github.com/korshunov418' )
unique_url1('https://github.com/korshunov418' )

@profile
def unique_url2(uri):
    dict_url2[uri] = hashlib.md5(salt.encode() + uri.encode()).hexdigest()
    
unique_url2('https://github.com/korshunov418' )
unique_url2('https://github.com/korshunov418' )

# Так как ключ уникальный, то я вообще убрал условие добавления. По памяти разницы не видно. Но куда ещё оптимизировать?


#print(dict_url1)
#print(dict_url2)
