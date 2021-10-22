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

# Первый скрипт

from memory_profiler import profile


@profile
def decorator_for_recursion(reverse_numb):
    def wrapper_for_recursion():
        reverse_numb()
    return wrapper_for_recursion


def reverse_numb(numb):
    rest_numb, numeral = divmod(numb, 10)
    if rest_numb == 0:
        return str(numeral)
    else:
        return str(numeral) + str(reverse_numb(rest_numb))


# number = int(input("Число для реверса: "))
number = 252896723489
# print(decorator_for_recursion(number))

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     23     19.1 MiB     19.1 MiB           1   @profile
#     24                                         def decorator_for_recursion(reverse_numb):
#     25     19.1 MiB      0.0 MiB           1       def wrapper_for_recursion():
#     26                                                 reverse_numb()
#     27     19.1 MiB      0.0 MiB           1       return wrapper_for_recursion

# Другой вариант решения:


@profile
def some_func_to_check(num):
    new_numb = ''
    num_count = len(str(num))
    numb = range(num_count)
    for f in numb:
        new_numb = new_numb + str(int(num) % 10)
        num = int(num) // 10
    return new_numb


print(some_func_to_check(number))

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     53     18.9 MiB     18.9 MiB           1   @profile
#     54                                         def some_func_to_check(num):
#     55     18.9 MiB      0.0 MiB           1       new_numb = ''
#     56     18.9 MiB      0.0 MiB           1       num_count = len(str(num))
#     57     18.9 MiB      0.0 MiB           1       numb = range(num_count)
#     58     18.9 MiB      0.0 MiB          13       for f in numb:
#     59     18.9 MiB      0.0 MiB          12           new_numb = new_numb + str(int(num) % 10)
#     60     18.9 MiB      0.0 MiB          12           num = int(num) // 10
#     61     18.9 MiB      0.0 MiB           1       return new_numb

# Очевидно, что вариант без рекурсии быстрее

# Второй скрипт

dict_fill = {}

n = 10 ** 5

@profile
def fill_dict(dct, num):
    for i in range(num):
        dct[i] = i


@profile
def fill_dict_change_to_list(dct, num):
    for i in range(num):
        dct[i] = i
    # list_of_tuple = collections.namedtuple('List', 'name value') - пытался сделать кортежи другим способом,
                                                                            # но не взлетело
    # lists = list(list_of_tuple(*item) for item in dict.items())
    list_dict = zip(dct.keys(), dct.values())
    del dct
    list_dict = list(list_dict)
    return list_dict


# fill_dict(dict_fill, n)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     62     19.0 MiB     19.0 MiB           1   @profile
#     63                                         def fill_dict(dct, num):
#     64     27.0 MiB      0.0 MiB      100001       for i in range(num):
#     65     27.0 MiB      8.0 MiB      100000           dct[i] = i

fill_dict_change_to_list(dict_fill, n)

# Вывод/размышления:
# !!! Вроде словарь переделывал в список кортежей, удалил словарь,
# !!! а памяти стало больше уходить, и даже del dct не помог

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     68     19.0 MiB     19.0 MiB           1   @profile
#     69                                         def fill_dict_change_to_list(dct, num):
#     70     27.1 MiB      0.0 MiB      100001       for i in range(num):
#     71     27.1 MiB      8.0 MiB      100000           dct[i] = i
#     72                                             # list_of_tuple = collections.namedtuple('List', 'name value')
#     73                                             # lists = list(list_of_tuple(*item) for item in dict.items())
#     74     27.1 MiB      0.0 MiB           1       list_dict = zip(dct.keys(), dct.values())
#     75     27.1 MiB      0.0 MiB           1       del dct
#     76     34.6 MiB      7.5 MiB           1       list_dict = list(list_dict)
#     77     34.6 MiB      0.0 MiB           1       return list_dict

# Третий скрипт

@profile
def decorator_for_recursion(revers_1):
    def wrapper_for_recursion():
        revers_1()
    return wrapper_for_recursion


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


@profile
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


@profile
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


@profile
def reverse_4(enter_num):
    rest_numb, numeral = divmod(enter_num, 10)
    if rest_numb == 0:
        return str(numeral)
    else:
        return str(numeral) + str(reverse_4(rest_numb))


@profile
def reverse_5(enter_num):
    return "".join(reversed(str(enter_num)))

# по итогам профилирования самые эффективные алгоритмы по времени, впрочем, по памяти тоже revers_3
# (через срез) и reverse_5 (через встроенный модуль),
# вариант выполнения через срез как по времени выполняется быстрее всех, так и с наименьшим количеством вызовов функции

# decorator_for_recursion(ENTER_NUM)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     19     19.3 MiB     19.3 MiB           1   @profile
#     20                                         def decorator_for_recursion(revers_1):
#     21     19.3 MiB      0.0 MiB           1       def wrapper_for_recursion():
#     22                                                 revers_1()
#     23     19.3 MiB      0.0 MiB           1       return wrapper_for_recursion

# revers_2(ENTER_NUM)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     36     19.2 MiB     19.2 MiB           1   @profile
#     37                                         def revers_2(enter_num, revers_num=0):
#     38     19.2 MiB      0.0 MiB           7       while enter_num != 0:
#     39     19.2 MiB      0.0 MiB           6           num = enter_num % 10
#     40     19.2 MiB      0.0 MiB           6           revers_num = (revers_num + num / 10) * 10
#     41     19.2 MiB      0.0 MiB           6           enter_num //= 10
#     42     19.2 MiB      0.0 MiB           1       return revers_num

# revers_3(ENTER_NUM)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     45     19.1 MiB     19.1 MiB           1   @profile
#     46                                         def revers_3(enter_num):
#     47     19.1 MiB      0.0 MiB           1       enter_num = str(enter_num)
#     48     19.1 MiB      0.0 MiB           1       revers_num = enter_num[::-1]
#     49     19.1 MiB      0.0 MiB           1       return revers_num

# reverse_4(ENTER_NUM)  # тут профилирование рекурсии без обёртки

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     52     19.3 MiB     19.3 MiB           6   @profile
#     53                                         def reverse_4(enter_num):
#     54     19.3 MiB      0.0 MiB           6       rest_numb, numeral = divmod(enter_num, 10)
#     55     19.3 MiB      0.0 MiB           6       if rest_numb == 0:
#     56     19.3 MiB      0.0 MiB           1           return str(numeral)
#     57                                             else:
#     58     19.3 MiB      0.0 MiB           5           return str(numeral) + str(reverse_4(rest_numb))

# reverse_5(ENTER_NUM)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     61     19.1 MiB     19.1 MiB           1   @profile
#     62                                         def reverse_5(enter_num):
#     63     19.1 MiB      0.0 MiB           1       return "".join(reversed(str(enter_num)))

# Четвёртый скрипт (копипаста с урока на посмотреть), ну тут тоже цикл отработал с меньшими затратами

length = 900

@profile
def for_in(length_val):
    elem = 1
    amount = 0
    for i in range(length_val):
        amount += elem
        elem = -elem / 2
    print(f' Сумма последовательности из {length_val} равна {amount}')


# for_in(length)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#      5     19.1 MiB     19.1 MiB           1   @profile
#      6                                         def for_in(length_val):
#      7     19.1 MiB      0.0 MiB           1       elem = 1
#      8     19.1 MiB      0.0 MiB           1       amount = 0
#      9     19.1 MiB      0.0 MiB         901       for i in range(length_val):
#     10     19.1 MiB      0.0 MiB         900           amount += elem
#     11     19.1 MiB      0.0 MiB         900           elem = -elem / 2
#     12     19.1 MiB      0.0 MiB           1       print(f' Сумма последовательности из {length_val} равна {amount}')

@profile
def recursion(length):
    def sum_series_numbers(n, elem=1):
        if n <= 0:
            return 0
        return elem + sum_series_numbers(n - 1, -elem / 2)
    print(f' Сумма последовательности из {length} равна {sum_series_numbers(length)}')


recursion(length)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     28     19.0 MiB     19.0 MiB           1   @profile
#     29                                         def recursion(length):
#     30     20.9 MiB      1.8 MiB         902       def sum_series_numbers(n, elem=1):
#     31     20.9 MiB      0.0 MiB         901           if n <= 0:
#     32     20.9 MiB      0.0 MiB           1               return 0
#     33     20.9 MiB      0.0 MiB         900           return elem + sum_series_numbers(n - 1, -elem / 2)
#     34     20.9 MiB      0.0 MiB           1       print(f' Сумма последовательности из {length} равна
#                                                       {sum_series_numbers(length)}')

