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
15
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from timeit import default_timer
from memory_profiler import memory_usage
import re



def super_decor(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        start_memory = memory_usage()
        result = func(*args, **kwargs)
        print(f'Затраченное время: {default_timer() - start_time}')
        print(f'Затраченная память: {memory_usage()[0] - start_memory[0]}')
    return wrapper


"""
Код с codewars
IP Validation
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. 
IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.
Input to the function is guaranteed to be a single string.
Мой первый вариант рещения
"""

def is_valid_IP(string):
    res = 0
    for i in string:
        if i == ".":
            res += 1
    string1 = string.split('.')
    ip_range = list(map(str, (list(range(0, 256)))))
    c = [item for item in string1 if item in ip_range]
    if len(c) == 4:
        if res == 3:
            return True
        else:
            return False
    else:
        return False

"""
Уход от цикла переход и спискового включению к решению в одну строку через регулярку
"""
def is_valid_IP1(string):
    return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)', string))

""""
Код с codewars
Format a string of names like 'Bart, Lisa & Maggie'.
Return: a string formatted as a list of names separated
by commas except for the last two names, which should be separated by an ampersand.
Мой вариант рещения
"""

def namelist(names):
    a = [d['name'] for d in names]
    if len(a) > 1:
        b = ', '.join(map(str, a[0:-1]))
        d = a[-1]
        return (f"{b} & {d}")
    else:
        a = ''.join(a)
        return (f"{a}")

"""
Решение в одну строку, также переход к генератору от спискового включения
"""
def namelist1(names):
    return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), names[-1]['name'])

""""
Код с codewars
Create Phone Number
Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.
Мой вариант рещения
"""

def create_phone_number(n):
    d = '('
    for i in range(len(n)):
        if i < 3:
            d = d + str(n[i])
            if i == 2:
                d = d + ') '
        elif i >= 3 and i < 6:
            d = d + str(n[i])
            if i == 5:
                d = d + '-'
        elif i >= 6 and i < 10:
            d = d + str(n[i])
    return d

"""
Ушли от цикла и срезов к прямой распоковке через format 
"""
def create_phone_number1(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

@super_decor
def loop(func, arg, n):
    for i in range(n):
        func(arg)


# print(loop(is_valid_IP, "123.234.210.243", 100000))
# print(loop(is_valid_IP1, "123.234.210.243", 100000))

# print(loop(namelist, [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}], 10000000))
# print(loop(namelist1, [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}], 10000000))

print(loop(create_phone_number, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 10000000))
print(loop(create_phone_number1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 10000000))

