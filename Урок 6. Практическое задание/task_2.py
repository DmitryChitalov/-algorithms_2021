"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика)
"""
import string
import random
from memory_profiler import profile, memory_usage
from timeit import default_timer


def decor(func):
    """Функция декортатор для замеров времени и памяти"""

    def wrapper(*args, **kwargs):
        t1 = default_timer()
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        t2 = default_timer()
        mem_diff = m2[0] - m1[0]
        time_dif = t2 - t1
        print(f'Функция - {func.__name__}\n Время заняло: {time_dif}\n Памяти заняло:{mem_diff}\n\n')
        return res

    return wrapper


"""Конкатенация"""


def generate_random_string(length):
    """генератор рандомного списка из букв заданной длинны length"""
    letters = string.ascii_lowercase
    rand_string = [random.choice(letters) for i in range(length)]
    return rand_string


my_list = generate_random_string(10000000)


# print(my_list)

@decor
def concate(my_list):
    """стоит избегать подобной реализации """
    st = ''
    for s in my_list:
        st += s
    return st


@decor
def concate_join(my_list):
    """лучше воспользоваться join"""
    return ''.join(my_list)


concate(my_list)
concate_join(my_list)

"""
Функция - concate
 Время заняло: 8.536880934
 Памяти заняло:10.3125

Функция - concate_join
 Время заняло: 0.3107637210000007
 Памяти заняло:9.5390625
 
 Использование join при конкатенации значительно увеличивает время выполнения и экономит память
"""

d = [i for i in range(10000000)]

"""Исключения"""


@decor
def exept_with_err(my_list):
    """со срабатывающим исключением"""
    for i in my_list:
        try:
            s = i / 0
        except ZeroDivisionError:
            pass


@decor
def exept_without_err(my_list):
    """исключение не срабатывает, но функционал присутствует"""
    for i in my_list:
        try:
            s = i / 2
        except ZeroDivisionError:
            pass


@decor
def exept_without_exept(my_list):
    """без исключений"""
    for i in my_list:
        s = i / 2


exept_with_err(d)
exept_without_err(d)
exept_without_exept(d)

"""
Функция - exept_with_err
 Время заняло: 3.1852066489999995
 Памяти заняло:0.0

Функция - exept_without_err
 Время заняло: 0.6885892489999996
 Памяти заняло:0.0

Функция - exept_without_exept
 Время заняло: 0.6395724469999999
 Памяти заняло:0.0
 
 Нашел старую информацию еще описывающую эту проблему для питона 2.4, решил проверить и для текущей версии (у меня 3.8)
 Далее цитата::
    "Отлов исключений в python-коде (в отличии от CPython) -- медленны, Не советую  писать  код,  которые  не защищает 
     сам себя, но лишь будь внимателен  насчет  того,  что делает  твой  код;  и обращай внимание,
    что исключения   в python-коде   весьма  накладны,  в силу  вызываемой
    ими "машинерии"."

При проверке действительно есть разница с нагруженным исклечениями коде и совсем без исключений, но незначительная
Вероятно в последних версиях вызов исключений оптимизировали по сравнению с версиями 2.x
"""

"""Сравнение типов"""

dd = [i for i in range(10000000)]   #  в листе хранятся int значения


@decor
def compare_int_int(my_list):
    s = int(1)
    for i in my_list:
        if s == i:
            pass


@decor
def compare_int_float(my_list):
    s = float(1)
    for i in my_list:
        if s == i:
            pass


compare_int_int(dd)
compare_int_float(dd)


"""

Функция - compare_int_int
 Время заняло: 0.4652618860000004
 Памяти заняло:0.0

Функция - compare_int_float
 Время заняло: 0.6872620269999992
 Памяти заняло:0.0
 
 При сравнении нужно учитывать, что сравнение разных типов данных занимает больше времени, вероятно время занимает 
 конвертация между типами данных

"""