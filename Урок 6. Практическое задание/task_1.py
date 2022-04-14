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
from timeit import default_timer
from memory_profiler import profile
from random import randint


def probe_time(func):
    def wrapper(*args):
        start = default_timer()
        func(*args)
        end = default_timer()
        print('Exec time:', (end-start))
    return wrapper


@probe_time
@profile
def script_1():
    ip_list = []

    with open('nginx_logs.txt', 'r') as file:
        for line in file:
            request = line.split(' ')   # узкое место, почему-то занимает >3 MiB, хотя весь файл весит 6 MiB ???
            ip_list.append(request[0])  # можно предположить что из-за 51000 повторений,
                                        # но по-идее каждую итерацию переменная формируется заново
    ip_dict = {}
    for item in ip_list:
        if item in ip_dict:
            ip_dict[item] += 1
        else:
            ip_dict[item] = 0

    stats = sorted(ip_dict, key=ip_dict.__getitem__)
    print(f'Спамер с IP {stats[-1]}: {ip_dict[stats[-1]]} запросов')


@probe_time
@profile
def script_1_opt():
    ip_list = []

    with open('nginx_logs.txt', 'r') as file:
        for line in file:
            end = line.find(' ')
            request = line[0:end]  # удалось добиться небольшого снижения затрат памяти
            ip_list.append(request)

    ip_dict = {}
    for item in ip_list:
        if item in ip_dict:
            ip_dict[item] += 1
        else:
            ip_dict[item] = 0

    stats = sorted(ip_dict, key=ip_dict.__getitem__)
    print(f'Спамер с IP {stats[-1]}: {ip_dict[stats[-1]]} запросов')


@probe_time
@profile
def script_2(string: str):
    substr_list = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substr_list.append(string[i:j])
    substr_list.remove(string)
    return substr_list


@probe_time
@profile
def script_3():
    array = [randint(0, 9) for i in range(10000)]
    cache = {}
    for num in array:
        if num in cache:
            cache[num] += 1
        else:
            cache[num] = 1
    keys = list(cache.keys())
    values = list(cache.values())
    max_count = values.index(max(values))
    max_num = keys[max_count]
    return f'Чаще всего встречается число {max_num}, ' \
            f'оно появилось в массиве {values[max_count]} раз(а)'


@probe_time
@profile
def script_4():
    lst = [1, 2, 3, 4, 5, 6, 0, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2]
    min = lst[0]
    localmin = lst[0]
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] <= lst[j]:
                localmin = lst[i]
            if localmin < min:
                min = localmin
    return min


script_1()
script_1_opt()
script_2('sdfjkgaoerogaidfgjicvllfklgdkfkffkgjdlgklasdfl;ga;gjaidfgjdflgkdkgkjskdjfgjk')
script_3()
script_4()

'''
Спамер с IP 216.46.173.126: 2349 запросов
Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    38     19.3 MiB     19.3 MiB           1   @probe_time
    39                                         @profile
    40                                         def script_1():
    41     19.3 MiB      0.0 MiB           1       ip_list = []
    42                                         
    43     19.3 MiB      0.0 MiB           1       with open('nginx_logs.txt', 'r') as file:
    44     23.1 MiB      0.2 MiB       51463           for line in file:
    45     23.1 MiB      3.2 MiB       51462               request = line.split(' ')  # узкое место, почему-то занимает >3 MiB, хотя весь файл весит 6 MiB ???
    46     23.1 MiB      0.4 MiB       51462               ip_list.append(request[0])
    47                                         
    48     23.1 MiB      0.0 MiB           1       ip_dict = {}
    49     23.1 MiB      0.0 MiB       51463       for item in ip_list:
    50     23.1 MiB      0.0 MiB       51462           if item in ip_dict:
    51     23.1 MiB      0.0 MiB       48802               ip_dict[item] += 1
    52                                                 else:
    53     23.1 MiB      0.0 MiB        2660               ip_dict[item] = 0
    54                                         
    55     23.1 MiB      0.0 MiB           1       stats = sorted(ip_dict, key=ip_dict.__getitem__)
    56     23.1 MiB      0.0 MiB           1       print(f'Спамер с IP {stats[-1]}: {ip_dict[stats[-1]]} запросов')


Exec time: 9.80684
Спамер с IP 216.46.173.126: 2349 запросов
Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    59     19.8 MiB     19.8 MiB           1   @probe_time
    60                                         @profile
    61                                         def script_1_opt():
    62     19.8 MiB      0.0 MiB           1       ip_list = []
    63                                         
    64     19.8 MiB      0.0 MiB           1       with open('nginx_logs.txt', 'r') as file:
    65     23.0 MiB      0.3 MiB       51463           for line in file:
    66     23.0 MiB      0.0 MiB       51462               end = line.find(' ')
    67     23.0 MiB      2.8 MiB       51462               request = line[0:end]
    68     23.0 MiB      0.1 MiB       51462               ip_list.append(request)
    69                                         
    70     23.0 MiB      0.0 MiB           1       ip_dict = {}
    71     23.1 MiB      0.0 MiB       51463       for item in ip_list:
    72     23.1 MiB      0.0 MiB       51462           if item in ip_dict:
    73     23.1 MiB      0.0 MiB       48802               ip_dict[item] += 1
    74                                                 else:
    75     23.1 MiB      0.1 MiB        2660               ip_dict[item] = 0
    76                                         
    77     23.1 MiB      0.0 MiB           1       stats = sorted(ip_dict, key=ip_dict.__getitem__)
    78     23.1 MiB      0.0 MiB           1       print(f'Спамер с IP {stats[-1]}: {ip_dict[stats[-1]]} запросов')


Exec time: 11.2864549
Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    81     20.1 MiB     20.1 MiB           1   @probe_time
    82                                         @profile
    83                                         def script_2(string: str):
    84     20.1 MiB      0.0 MiB           1       substr_list = []
    85     20.1 MiB      0.0 MiB          77       for i in range(len(string)):
    86     20.1 MiB      0.0 MiB        3002           for j in range(i + 1, len(string) + 1):
    87     20.1 MiB      0.0 MiB        2926               substr_list.append(string[i:j])
    88     20.1 MiB      0.0 MiB           1       substr_list.remove(string)
    89     20.1 MiB      0.0 MiB           1       return substr_list


Exec time: 0.1838758000000027
Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    92     20.1 MiB     20.1 MiB           1   @probe_time
    93                                         @profile
    94                                         def script_3():
    95     20.2 MiB      0.1 MiB       10003       array = [randint(0, 9) for i in range(10000)]
    96     20.2 MiB      0.0 MiB           1       cache = {}
    97     20.2 MiB      0.0 MiB       10001       for num in array:
    98     20.2 MiB      0.0 MiB       10000           if num in cache:
    99     20.2 MiB      0.0 MiB        9990               cache[num] += 1
   100                                                 else:
   101     20.2 MiB      0.0 MiB          10               cache[num] = 1
   102     20.2 MiB      0.0 MiB           1       keys = list(cache.keys())
   103     20.2 MiB      0.0 MiB           1       values = list(cache.values())
   104     20.2 MiB      0.0 MiB           1       max_count = values.index(max(values))
   105     20.2 MiB      0.0 MiB           1       max_num = keys[max_count]
   106     20.2 MiB      0.0 MiB           2       return f'Чаще всего встречается число {max_num}, ' \
   107     20.2 MiB      0.0 MiB           1               f'оно появилось в массиве {values[max_count]} раз(а)'


Exec time: 1.4269680000000022
Filename: D:\IT\!Study Projects\-algorithms_2021\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   110     20.2 MiB     20.2 MiB           1   @probe_time
   111                                         @profile
   112                                         def script_4():
   113     20.2 MiB      0.0 MiB           1       lst = [1, 2, 3, 4, 5, 6, 0, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2]
   114     20.2 MiB      0.0 MiB           1       min = lst[0]
   115     20.2 MiB      0.0 MiB           1       localmin = lst[0]
   116     20.2 MiB      0.0 MiB          18       for i in range(len(lst)):
   117     20.2 MiB      0.0 MiB         306           for j in range(len(lst)):
   118     20.2 MiB      0.0 MiB         289               if lst[i] <= lst[j]:
   119     20.2 MiB      0.0 MiB         160                   localmin = lst[i]
   120     20.2 MiB      0.0 MiB         289               if localmin < min:
   121     20.2 MiB      0.0 MiB           1                   min = localmin
   122     20.2 MiB      0.0 MiB           1       return min


Exec time: 0.03353870000000114
'''