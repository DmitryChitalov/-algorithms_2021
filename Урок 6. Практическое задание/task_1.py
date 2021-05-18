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

from memory_profiler import profile, memory_usage
from random import randint
from collections import namedtuple
from sys import getsizeof
from recordclass import recordclass
from pympler.asizeof import asizeof
from numpy import array

def my_decor(func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        m1 = memory_usage()
        m2 = memory_usage()
        end = default_timer()
        my_time = end - start
        mem_diff = m2[0] - m1[0]
        print(f"Было потрачено памяти {mem_diff}, Было потрачено времени {my_time}")
        return my_time, mem_diff
    return wrapper

'''
#1ый пример с заменами элементов   -------------------------->
#@my_decor
@profile
def first_function(my_list):
    y = 0                                                           # Mem usage 47.0 MiB Increment 0.0 MiB
    for el in range(int(len(my_list)) // 2):                        # Mem usage 47.0 MiB Increment 0.0 MiB
        my_list[y], my_list[y + 1] = my_list[y + 1], my_list[y]     # Mem usage 47.0 MiB Increment 0.0 MiB
        y += 2                                                      # Mem usage 47.0 MiB Increment 0.0 MiB
    return my_list                                                  # Mem usage 47.0 MiB Increment 0.0 MiB

first_function(list(range(100500)))

#@my_decor
@profile
def firstdotone_function(my_list):
    y = 0                                                        # Mem usage 43.8 MiB Increment 0.0 MiB
    for el in range(int(len(my_list)) // 2):                     # Mem usage 43.8 MiB Increment 0.0 MiB
        my_list[y], my_list[y + 1] = my_list[y + 1], my_list[y]  # Mem usage 43.8 MiB Increment 0.0 MiB
        y += 2                                                   # Mem usage 43.8 MiB Increment 0.0 MiB
    return my_list

firstdotone_function(array(list(range(100500))))
"""
Вывод: в первом варианте был передан генератор списка, после профилирования выдавало 47.0 MiB, после серии экспериментов
было решено произвести отимизацию с использованием numpy и встроенной функции array, c помощью которой смог сократить
кол-во задействованной памяти до 43.8 MiB (скажем спасибо сжатию массива). Декоратор по затраченной памяти показал
следующие значения :
Было потрачено памяти 0.00390625, Было потрачено времени 0.21677509999999994
Было потрачено памяти 0.0, Было потрачено времени 0.21276630000000007
По итогу для 2го варианта и памяти было потрачено меньше + небольшое сокращение времени обработки
"""

# 2ой пример с выводом элементов исходного списка                  ---------------------------->
#@my_decor
@profile
def second_function(my_list):
    second_list = [my_list[el + 1] for el in range(len(my_list) - 1)
                if my_list[el] < my_list[el + 1]]                      # Mem usage 47.8 MiB Increment 0.5 MiB
    return second_list

second_function([randint(100, 10000) for i in range(100000)])

#@my_decor
@profile
def seconddotone_function(my_list):
    second_list = array([my_list[el + 1] for el in range(len(my_list) - 1)
                      if my_list[el] < my_list[el + 1]])                  # Mem usage 46.3 MiB Increment 0.0 MiB
    return second_list                                                       # Mem usage 45.3 MiB Increment -1.0 MiB

seconddotone_function(array([randint(100, 10000) for i in range(100000)]))

"""
Вывод: провел анализ и понял, что numpy продолжает все также хорошо отрабатывать. Заметил, что появились цифры в 
энкрименте, т.к. внутри списка есть списковое включение, было также оптимизировано с numpy. 
в первом варианте инкремент равен 0.5, в оптимизированном -1.0 .
Декоратор по затраченной памяти показал следующие значения :
Было потрачено памяти 0.0, Было потрачено времени 0.21273300000000006
Было потрачено памяти 0.0, Было потрачено времени 0.2104275000000002
"""
'''


#3ий пример с заменой namedtuple на recordclass   -------------------->

#скрипт до оптимизации
#@my_decor
#@profile
def func_max(comp_dict, aver_forsyst):
    comp_lst = []
    for i in range(len(comp_dict)):
        amt_ofquats = int(comp_dict[i+1].profit_q1) + int(comp_dict[i+1].profit_q2) +\
                      int(comp_dict[i+1].profit_q3) + int(comp_dict[i+1].profit_q4)
        if amt_ofquats > aver_forsyst:
            comp_lst.append(comp_dict[i+1].company)
    return comp_lst

#@my_decor
#@profile
def func_min(comp_dict, aver_forsyst):
    comp_lst = []
    for i in range(len(comp_dict)):
        amt_ofquats = int(comp_dict[i+1].profit_q1) + int(comp_dict[i+1].profit_q2) +\
                      int(comp_dict[i+1].profit_q3) + int(comp_dict[i+1].profit_q4)
        if amt_ofquats < aver_forsyst:
            comp_lst.append(comp_dict[i+1].company)
    return comp_lst

#@my_decor
#@profile
def firm_func():
    n = int(input("Введите количество компаний: "))
    i = 1
    comp_dict = {}
    comp_avprofit = 0
    while i != n + 1:
        company_tmplate = namedtuple(f"Company_{i}", "company profit_q1 profit_q2 profit_q3 profit_q4")
        user_cmpname = input(f"Введите название предприятия №{i}: ")
        user_cmpprofit = input(f"Через пробел введите прибыль предприятия №{i} "
                               f"за каждый квартал (всего 4 квартала): ").split()
        company_tpl = company_tmplate(
            company=user_cmpname,
            profit_q1=user_cmpprofit[0],
            profit_q2=user_cmpprofit[1],
            profit_q3=user_cmpprofit[2],
            profit_q4=user_cmpprofit[3]
        )
        comp_dict[i] = company_tpl
        i += 1
        comp_avprofit += int(company_tpl.profit_q1) + int(company_tpl.profit_q2) \
                         + int(company_tpl.profit_q3) + int(company_tpl.profit_q4)
    aver_forsyst = comp_avprofit / (i-1)
    print(f'Средняя годовая прибыль всех предприятий: {aver_forsyst}')
    print(f"Предприятия, с прибылью выше среднего значения: {', '.join(func_max(comp_dict, aver_forsyst))}")
    print(f"Предприятия, с прибылью ниже среднего значения: {', '.join(func_min(comp_dict, aver_forsyst))}")
    print(f'Объём занимаемой объектом namedtuple памяти с использованием getsizeof: {getsizeof(company_tpl)} байт(а)')
    print(f'Объём занимаемой объектом namedtuple памяти с использованием asizeof: {asizeof(company_tpl)} байт(а)')

firm_func()

#после оптимизации
#@my_decor
#@profile
def func_max(comp_dict, aver_forsyst):
    comp_lst = []
    for i in range(len(comp_dict)):
        amt_ofquats = int(comp_dict[i+1].profit_q1) + int(comp_dict[i+1].profit_q2) +\
                      int(comp_dict[i+1].profit_q3) + int(comp_dict[i+1].profit_q4)
        if amt_ofquats > aver_forsyst:
            comp_lst.append(comp_dict[i+1].company)
    del i
    del amt_ofquats
    del aver_forsyst
    del comp_dict
    return comp_lst

#@my_decor
#@profile
def func_min(comp_dict, aver_forsyst):
    comp_lst = []
    for i in range(len(comp_dict)):
        amt_ofquats = int(comp_dict[i+1].profit_q1) + int(comp_dict[i+1].profit_q2) +\
                      int(comp_dict[i+1].profit_q3) + int(comp_dict[i+1].profit_q4)
        if amt_ofquats < aver_forsyst:
            comp_lst.append(comp_dict[i+1].company)
    del i
    del comp_dict
    del aver_forsyst
    del amt_ofquats
    return comp_lst

#@my_decor
#@profile
def firm_func():
    n = int(input("Введите количество компаний: "))
    i = 1
    comp_dict = {}
    comp_avprofit = 0
    while i != n + 1:
        company_tmplate = recordclass(f"Company_{i}", "company profit_q1 profit_q2 profit_q3 profit_q4")
        user_cmpname = input(f"Введите название предприятия №{i}: ")
        user_cmpprofit = input(f"Через пробел введите прибыль предприятия №{i} "
                               f"за каждый квартал (всего 4 квартала): ").split()
        company_tpl = company_tmplate(
            company=user_cmpname,
            profit_q1=user_cmpprofit[0],
            profit_q2=user_cmpprofit[1],
            profit_q3=user_cmpprofit[2],
            profit_q4=user_cmpprofit[3]
        )
        comp_dict[i] = company_tpl
        i += 1
        comp_avprofit += int(company_tpl.profit_q1) + int(company_tpl.profit_q2) \
                         + int(company_tpl.profit_q3) + int(company_tpl.profit_q4)
    aver_forsyst = comp_avprofit / (i-1)
    del user_cmpprofit
    del user_cmpname
    print(f'Средняя годовая прибыль всех предприятий: {aver_forsyst}')
    print(f"Предприятия, с прибылью выше среднего значения: {', '.join(func_max(comp_dict, aver_forsyst))}")
    print(f"Предприятия, с прибылью ниже среднего значения: {', '.join(func_min(comp_dict, aver_forsyst))}")
    print(f'Объём занимаемой объектом recordclass памяти с использованием getsizeof: {getsizeof(company_tpl)} байт(а)')
    print(f'Объём занимаемой объектом recordclass памяти с использованием asizeof: {asizeof(company_tpl)} байт(а)')

firm_func()

"""
Объём занимаемой объектом namedtuple памяти с использованием getsizeof: 80 байт(а)
Объём занимаемой объектом namedtuple памяти с использованием asizeof: 360 байт(а)
Объём занимаемой объектом recordclass памяти с использованием getsizeof: 64 байт(а)
Объём занимаемой объектом recordclass памяти с использованием asizeof: 1176 байт(а)

Вывод:
Не смотря на то, что getsizeof показывает небольшой профит по использованию памяти у recordclass относительно namedtuple,
однако измерение размера полной структуры объектов с помощью asizeof в связи с тем, что объект recordclass более сложный,
namedtuple занимает меньший объём памяти. Получается, что в данном случае использование recordclass не эффективно.
Recordclass остаётся хорошим вариантом в случае, если необходимо изменять атрибуты класса в процессе выполнения программы.

+ удаление доп. ссылок в ходе оптимизации функции не является видимым, т.к. освобождаемый объем памяти очень мал

Данные по профайлу:
1ый - использование namedtuple
2ой - использование recordclass

1 ------------------------------------------
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   113     43.4 MiB     43.4 MiB           1   @profile
   114                                         def func_max(comp_dict, aver_forsyst):
   115     43.4 MiB      0.0 MiB           1       comp_lst = []
   116     43.4 MiB      0.0 MiB           3       for i in range(len(comp_dict)):
   117     43.4 MiB      0.0 MiB           6           amt_ofquats = int(comp_dict[i+1].profit_q1) + int(comp_dict[i+1].profit_q2) +\
   118     43.4 MiB      0.0 MiB           4                         int(comp_dict[i+1].profit_q3) + int(comp_dict[i+1].profit_q4)
   119     43.4 MiB      0.0 MiB           2           if amt_ofquats > aver_forsyst:
   120                                                     comp_lst.append(comp_dict[i+1].company)
   121     43.4 MiB      0.0 MiB           1       return comp_lst
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   124     43.4 MiB     43.4 MiB           1   @profile
   125                                         def func_min(comp_dict, aver_forsyst):
   126     43.4 MiB      0.0 MiB           1       comp_lst = []
   127     43.4 MiB      0.0 MiB           3       for i in range(len(comp_dict)):
   128     43.4 MiB      0.0 MiB           6           amt_ofquats = int(comp_dict[i+1].profit_q1) + int(comp_dict[i+1].profit_q2) +\
   129     43.4 MiB      0.0 MiB           4                         int(comp_dict[i+1].profit_q3) + int(comp_dict[i+1].profit_q4)
   130     43.4 MiB      0.0 MiB           2           if amt_ofquats < aver_forsyst:
   131                                                     comp_lst.append(comp_dict[i+1].company)
   132     43.4 MiB      0.0 MiB           1       return comp_lst
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   135     43.4 MiB     43.4 MiB           1   @profile
   136                                         def firm_func():
   137     43.4 MiB      0.0 MiB           1       n = int(input("Введите количество компаний: "))
   138     43.4 MiB      0.0 MiB           1       i = 1
   139     43.4 MiB      0.0 MiB           1       comp_dict = {}
   140     43.4 MiB      0.0 MiB           1       comp_avprofit = 0
   141     43.4 MiB      0.0 MiB           3       while i != n + 1:
   142     43.4 MiB      0.0 MiB           2           company_tmplate = namedtuple(f"Company_{i}", "company profit_q1 profit_q2 profit_q3 profit_q4")
   143     43.4 MiB      0.0 MiB           2           user_cmpname = input(f"Введите название предприятия №{i}: ")
   144     43.4 MiB      0.0 MiB           2           user_cmpprofit = input(f"Через пробел введите прибыль предприятия №{i} "
   145                                                                        f"за каждый квартал (всего 4 квартала): ").split()
   146     43.4 MiB      0.0 MiB           4           company_tpl = company_tmplate(
   147     43.4 MiB      0.0 MiB           2               company=user_cmpname,
   148     43.4 MiB      0.0 MiB           2               profit_q1=user_cmpprofit[0],
   149     43.4 MiB      0.0 MiB           2               profit_q2=user_cmpprofit[1],
   150     43.4 MiB      0.0 MiB           2               profit_q3=user_cmpprofit[2],
   151     43.4 MiB      0.0 MiB           2               profit_q4=user_cmpprofit[3]
   152                                                 )
   153     43.4 MiB      0.0 MiB           2           comp_dict[i] = company_tpl
   154     43.4 MiB      0.0 MiB           2           i += 1
   155     43.4 MiB      0.0 MiB           6           comp_avprofit += int(company_tpl.profit_q1) + int(company_tpl.profit_q2) \
   156     43.4 MiB      0.0 MiB           4                            + int(company_tpl.profit_q3) + int(company_tpl.profit_q4)
   157     43.4 MiB      0.0 MiB           1       aver_forsyst = comp_avprofit / (i-1)
   158     43.4 MiB      0.0 MiB           1       print(f'Средняя годовая прибыль всех предприятий: {aver_forsyst}')
   159     43.4 MiB      0.0 MiB           1       print(f"Предприятия, с прибылью выше среднего значения: {', '.join(func_max(comp_dict, aver_forsyst))}")
   160     43.4 MiB      0.0 MiB           1       print(f"Предприятия, с прибылью ниже среднего значения: {', '.join(func_min(comp_dict, aver_forsyst))}")



2 -----------------------------------------------------
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   166     43.5 MiB     43.5 MiB           1   @profile
   167                                         def func_max(comp_dict, aver_forsyst):
   168     43.5 MiB      0.0 MiB           1       comp_lst = []
   169     43.5 MiB      0.0 MiB           3       for i in range(len(comp_dict)):
   170     43.5 MiB      0.0 MiB           6           amt_ofquats = int(comp_dict[i+1].profit_q1) + int(comp_dict[i+1].profit_q2) +\
   171     43.5 MiB      0.0 MiB           4                         int(comp_dict[i+1].profit_q3) + int(comp_dict[i+1].profit_q4)
   172     43.5 MiB      0.0 MiB           2           if amt_ofquats > aver_forsyst:
   173                                                     comp_lst.append(comp_dict[i+1].company)
   174     43.5 MiB      0.0 MiB           1       del i
   175     43.5 MiB      0.0 MiB           1       del amt_ofquats
   176     43.5 MiB      0.0 MiB           1       del aver_forsyst
   177     43.5 MiB      0.0 MiB           1       del comp_dict
   178     43.5 MiB      0.0 MiB           1       return comp_lst
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   181     43.5 MiB     43.5 MiB           1   @profile
   182                                         def func_min(comp_dict, aver_forsyst):
   183     43.5 MiB      0.0 MiB           1       comp_lst = []
   184     43.5 MiB      0.0 MiB           3       for i in range(len(comp_dict)):
   185     43.5 MiB      0.0 MiB           6           amt_ofquats = int(comp_dict[i+1].profit_q1) + int(comp_dict[i+1].profit_q2) +\
   186     43.5 MiB      0.0 MiB           4                         int(comp_dict[i+1].profit_q3) + int(comp_dict[i+1].profit_q4)
   187     43.5 MiB      0.0 MiB           2           if amt_ofquats < aver_forsyst:
   188                                                     comp_lst.append(comp_dict[i+1].company)
   189     43.5 MiB      0.0 MiB           1       del i
   190     43.5 MiB      0.0 MiB           1       del comp_dict
   191     43.5 MiB      0.0 MiB           1       del aver_forsyst
   192     43.5 MiB      0.0 MiB           1       del amt_ofquats
   193     43.5 MiB      0.0 MiB           1       return comp_lst
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   196     43.4 MiB     43.4 MiB           1   @profile
   197                                         def firm_func():
   198     43.4 MiB      0.0 MiB           1       n = int(input("Введите количество компаний: "))
   199     43.4 MiB      0.0 MiB           1       i = 1
   200     43.4 MiB      0.0 MiB           1       comp_dict = {}
   201     43.4 MiB      0.0 MiB           1       comp_avprofit = 0
   202     43.5 MiB      0.0 MiB           3       while i != n + 1:
   203     43.5 MiB      0.0 MiB           2           company_tmplate = recordclass(f"Company_{i}", "company profit_q1 profit_q2 profit_q3 profit_q4")
   204     43.5 MiB      0.0 MiB           2           user_cmpname = input(f"Введите название предприятия №{i}: ")
   205     43.5 MiB      0.0 MiB           2           user_cmpprofit = input(f"Через пробел введите прибыль предприятия №{i} "
   206                                                                        f"за каждый квартал (всего 4 квартала): ").split()
   207     43.5 MiB      0.0 MiB           4           company_tpl = company_tmplate(
   208     43.5 MiB      0.0 MiB           2               company=user_cmpname,
   209     43.5 MiB      0.0 MiB           2               profit_q1=user_cmpprofit[0],
   210     43.5 MiB      0.0 MiB           2               profit_q2=user_cmpprofit[1],
   211     43.5 MiB      0.0 MiB           2               profit_q3=user_cmpprofit[2],
   212     43.5 MiB      0.0 MiB           2               profit_q4=user_cmpprofit[3]
   213                                                 )
   214     43.5 MiB      0.0 MiB           2           comp_dict[i] = company_tpl
   215     43.5 MiB      0.0 MiB           2           i += 1
   216     43.5 MiB      0.0 MiB           6           comp_avprofit += int(company_tpl.profit_q1) + int(company_tpl.profit_q2) \
   217     43.5 MiB      0.0 MiB           4                            + int(company_tpl.profit_q3) + int(company_tpl.profit_q4)
   218     43.5 MiB      0.0 MiB           1       aver_forsyst = comp_avprofit / (i-1)
   219     43.5 MiB      0.0 MiB           1       del user_cmpprofit
   220     43.5 MiB      0.0 MiB           1       del user_cmpname
   221     43.5 MiB      0.0 MiB           1       print(f'Средняя годовая прибыль всех предприятий: {aver_forsyst}')
   222     43.5 MiB      0.0 MiB           1       print(f"Предприятия, с прибылью выше среднего значения: {', '.join(func_max(comp_dict, aver_forsyst))}")
   223     43.5 MiB      0.0 MiB           1       print(f"Предприятия, с прибылью ниже среднего значения: {', '.join(func_min(comp_dict, aver_forsyst))}")

"""