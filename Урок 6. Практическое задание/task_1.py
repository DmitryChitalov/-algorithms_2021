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

from memory_profiler import profile
from numpy import array

"""найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры."""


# до
@profile()
def sum_line(n, result=0, count=0):
    if n == count:
        return print(result)
    else:
        result = (result + 1 / 2 ** count) if count % 2 == 0 else (result - 1 / 2 ** count)
        count += 1
    return sum_line(n, result, count)


# после
@profile()
def sum_line_2(n):
    result, count = 0, 0
    for i in range(n):
        result = (result + 1 / 2 ** count) if count % 2 == 0 else (result - 1 / 2 ** count)
        count += 1
    return result


@profile()
def sum_line_3(n):
    pass


if __name__ == '__main__':
    num = 200
    sum_line(num)
    sum_line_2(num)
    sum_line_3(num)

"""
Использование цикла значительно повышает скорость работы, а также отсутствует необходимость хранить результат 
предыдущий результат вызова функции, что видно из результата.

     7     21.6 MiB     21.0 MiB         201   @profile()
     8                                         def sum_line(n, result=0, count=0):
     9     21.6 MiB     -0.0 MiB         201       if n == count:
    10     21.6 MiB      0.0 MiB           1           return print(result)
    11                                             else:
    12     21.6 MiB      0.1 MiB         200           result = (result + 1 / 2 ** count) if count % 2 == 0 else (result - 1 / 2 ** count)
    13     21.6 MiB      0.0 MiB         200           count += 1
    14     21.6 MiB      0.2 MiB         200       return sum_line(n, result, count)
 ============================================================
    18     21.1 MiB     21.4 MiB           1   @profile()
    19                                         def sum_line_2(n):
    20     21.1 MiB      0.0 MiB           1       result, count = 0, 0
    21     21.1 MiB      0.0 MiB         201       for i in range(n):
    22     21.1 MiB      0.0 MiB         200           result = (result + 1 / 2 ** count) if count % 2 == 0 else (result - 1 / 2 ** count)
    23     21.1 MiB      0.0 MiB         200           count += 1
    24     21.1 MiB      0.0 MiB           1       print(result)
    
    
"""

"""2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
        a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
            Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
            делится нацело на 7. Внимание: использовать только арифметические операции!
            Задача из основ. 1 урок
            """

# до
@profile()
def get_number():
    number_list = []
    for number in range(1, 1000):
        if number % 2 != 0:
            number_list.append(number ** 3)
    new_number_list_a = []

    for number in number_list:
        sum_number = 0
        for element in str(number):
            sum_number += int(element)
        if sum_number % 7 == 0:
            new_number_list_a.append(number)


# после
# Вариант_1
@profile()
def get_number_2():
    number_gc = (number ** 3 for number in range(1, 1000) if number % 2 != 0)
    new_number_list = []

    for number in number_gc:
        sum_number = 0
        for element in str(number):
            sum_number += int(element)
        if sum_number % 7 == 0:
            new_number_list.append(number)

# Вариант_2
@profile()
def get_number_3():
    array_num = array([number ** 3 for number in range(1, 1000) if number % 2 != 0])
    new_number_list = []

    for number in array_num:
        sum_number = 0
        while number != 0:
            sum_number = sum_number + number % 10
            number = number // 10
            if sum_number % 7 == 0:
                new_number_list.append(number)


if __name__ == '__main__':
    get_number()
    get_number_2()
    get_number_3()

"""
 Использование генератора вместо формирования готового списка значительно экономит память (а также
 сжатия массива с помощью библиотеки numpy), т.к. генератор выдается значение по требованию. 
 (С увеличением кол-ва элементов в списке, разница более заметна)

До
============================================================
     4     19.1 MiB     18.9 MiB           1   @profile()
     5                                         def get_number():
     6     19.1 MiB      0.0 MiB           1       number_list = []
     7     19.1 MiB      0.0 MiB        1000       for number in range(1, 1000):
     8     19.1 MiB      0.0 MiB         999           if number % 2 != 0:
     9     19.1 MiB      0.0 MiB         500               number_list.append(number ** 3)
    10     19.1 MiB      0.0 MiB           1       new_number_list_a = []
    11                                         
    12     19.1 MiB      0.0 MiB         501       for number in number_list:
    13     19.1 MiB      0.0 MiB         500           sum_number = 0
    14     19.1 MiB      0.0 MiB        4568           for element in str(number):
    15     19.1 MiB      0.0 MiB        4068               sum_number += int(element)
    16     19.1 MiB      0.0 MiB         500           if sum_number % 7 == 0:
    17     19.1 MiB      0.0 MiB         106               new_number_list_a.append(number)

Вариант_1
============================================================
     4     18.7 MiB     18.7 MiB           1   @profile()
     5                                         def get_number_2():
     6     18.7 MiB      0.0 MiB        1502       number_gc = (number ** 3 for number in range(1, 1000) if number % 2 != 0)
     7     18.7 MiB      0.0 MiB           1       new_number_list = []
     8                                         
     9     18.7 MiB      0.0 MiB         501       for number in number_gc:
    10     18.7 MiB      0.0 MiB         500           sum_number = 0
    11     18.7 MiB      0.0 MiB        4568           for element in str(number):
    12     18.7 MiB      0.0 MiB        4068               sum_number += int(element)
    13     18.7 MiB      0.0 MiB         500           if sum_number % 7 == 0:
    14     18.7 MiB      0.0 MiB         106               new_number_list.append(number)

Вариант_2
============================================================
     6     18.9 MiB     18.9 MiB           1   @profile()
     7                                         def get_number_3():
     8     18.9 MiB      0.0 MiB        1002       array_num = array([number ** 3 for number in range(1, 1000) if number % 2 != 0])
     9     18.9 MiB      0.0 MiB           1       print(getsizeof(array_num))
    10     18.9 MiB      0.0 MiB           1       new_number_list = []
    11                                         
    12     18.9 MiB      0.0 MiB         501       for number in array_num:
    13     18.9 MiB      0.0 MiB         500           sum_number = 0
    14     18.9 MiB      0.0 MiB        4568           while number != 0:
    15     18.9 MiB      0.0 MiB        4068               sum_number = sum_number + number % 10
    16     18.9 MiB      0.0 MiB        4068               number = number // 10
    17     18.9 MiB      0.0 MiB        4068               if sum_number % 7 == 0:
    18     18.9 MiB      0.0 MiB         668                   new_number_list.append(number)
"""


"""3.Найти IP адрес спамера и количество отправленных им запросов по данным файла
    логов из предыдущего задания web-сервера nginx_logs.txt.

"""
#до
@profile()
def get_ip():
    with open('nginx_logs.txt') as f:
        ip_list = [line[0:line.find(' -')] for line in f]
        find_max_requests = max({ip_list.count(ip): ip for ip in ip_list})
        find_spam_ip = {ip_list.count(ip): ip for ip in ip_list}[find_max_requests]
    print(f'IP адрес спамера: {find_spam_ip}, кол-во отправленных запросов: {find_max_requests}')


#после
#Вариант_1
@profile()
def get_ip_2():
    with open('nginx_logs.txt') as f:
        ip_list_1 = [line[0:line.find(' -')] for line in f]
        ip = max(ip_list_1, key=ip_list_1.count)
    print(f'IP адрес спамера: {ip}, ' f'кол-во отправленных запросов: {ip_list_1.count(ip)}')


#Вариант_2
@profile()
def get_ip_3():
    with open('nginx_logs.txt') as f:
        ip_list_1 = {}
        for line in f:
            if line[0:line.find(' -')] not in ip_list_1:
                ip_list_1[line[0:line.find(' -')]] = 1
            else:
                ip_list_1[line[0:line.find(' -')]] += 1
        ip = max(ip_list_1, key=ip_list_1.get)
        print(f'IP адрес спамера: {ip}, ' f'кол-во отправленных запросов: {ip_list_1.get(ip)}')
"""
Самый быстрый вариант оказался со словарем, т.к отсутсвуют дублирующие записи, что экономит память,
а также с помощью встроенной ф-ии max, ускоряем работу скрипта

До
============================================================
     7     29.9 MiB     29.9 MiB           1   @profile()
     8                                         def get_ip():
     9     29.9 MiB      0.0 MiB           1       with open('nginx_logs.txt') as f:
    10     33.7 MiB      3.7 MiB       51465           ip_list = [line[0:line.find(' -')] for line in f]
    11     34.0 MiB      0.3 MiB       51465           find_max_requests = max({ip_list.count(ip): ip for ip in ip_list})
    12     34.0 MiB  -2310.8 MiB       51465           find_spam_ip = {ip_list.count(ip): ip for ip in ip_list}[find_max_requests]
    13                                         
    14     34.0 MiB     -0.1 MiB           1       print(f'IP адрес спамера: {find_spam_ip}, кол-во отправленных запросов: {find_max_requests}')


После
Вариант_1
============================================================
    17     29.9 MiB     30.1 MiB           1   @profile()
    18                                         def get_ip_2():
    19     29.9 MiB      0.0 MiB           1       with open('nginx_logs.txt') as f:
    20     33.7 MiB      3.7 MiB       51465           ip_list_1 = [line[0:line.find(' -')] for line in f]
    21     33.7 MiB     -0.0 MiB           1           ip = max(ip_list_1, key=ip_list_1.count)
    22     33.7 MiB      0.0 MiB           2       print(f'IP адрес спамера: {ip}, кол-во отправленных запросов: {ip_list_1.count(ip)}')          


Вариант_2
============================================================
     6     27.3 MiB     29.9 MiB           1   @profile()
     7                                         def get_ip_3():
     8     27.3 MiB      0.0 MiB           1       with open('nginx_logs.txt') as f:
     9     27.3 MiB      0.0 MiB           1           ip_list_1 = {}
    10     27.5 MiB      0.2 MiB       51463           for line in f:
    11     27.5 MiB      0.0 MiB       51462               if line[0:line.find(' -')] not in ip_list_1:
    12     27.6 MiB      0.1 MiB        2660                   ip_list_1[line[0:line.find(' -')]] = 1
    13                                                     else:
    14     27.6 MiB      0.0 MiB       48802                   ip_list_1[line[0:line.find(' -')]] += 1
    15     27.6 MiB      0.0 MiB           1           ip = max(ip_list_1, key=ip_list_1.get)
    16     27.6 MiB      0.0 MiB           1           print(f'IP адрес спамера: {ip}, ' f'кол-во отправленных запросов: {ip_list_1.get(ip)}')
"""