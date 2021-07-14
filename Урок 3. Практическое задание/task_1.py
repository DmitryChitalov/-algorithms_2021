"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать,
   так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

import time
import random


def time_of_func(func):
    def wrapper(*args):
        start_time = time.perf_counter_ns()
        res = func(*args)
        print(f"Время выполнения вункции \"{func.__name__}\" = {time.perf_counter_ns() - start_time}")
        return res

    return wrapper


@time_of_func
def list_constructor(n: int):
    """
    Создание случайного списка из n значений через лист компрехеншен
    Сложность его не нашел, но получется процентов на 15% бучтрее чем через цикл
    :param n:
    :return:
    """
    return [random.random() for i in range(n)]


@time_of_func
def list_constructor_2(n: int):
    """
    Созданиие случайного списка из n значений со сложностью О(n)
    :param n:
    :return:
    """
    temp_list = []
    for i in range(n):
        temp_list.append(random.random())
    return temp_list


@time_of_func
def dict_constructor(n: int):
    """
    Созданиие случайного словарая из n значений со сложностью О(n)
    В качестве ключей используются натуральные числа - как индексы в списке
    Решается примерко за тоже время что и список, формируемый
    аналагичным способом
    :param n:
    :return:
    """
    temp_dict = {}
    for i in range(n):
        temp_dict[i] = random.random()
    return temp_dict


@time_of_func
def dict_constructor_2(n: int):
    """
    Созданиие случайного словарая из n значений со сложностью О(n)
    В качестве ключей используются случайные числа
    Решается в четверо дольше чем список
    :param n:
    :return:
    """
    temp_dict = {}
    for i in range(n):
        temp_dict[random.random()] = random.random()
    return temp_dict


@time_of_func
def dict_constructor_3(n: int):
    """
    Созданиие случайного словарая из n значений со сложностью О(n)
    В качестве ключей используются f строки - как индексы в списке
    Решается в четверо дольше чем список, но чуть быстрее чем вариант со случайными числами
    :param n:
    :return:
    """
    temp_dict = {}
    for i in range(n):
        temp_dict[f"key {i}"] = random.random()
    return temp_dict


@time_of_func
def dict_constructor_4(n: int):
    """
    Созданиие случайного словарая из n значений со сложностью О(n)
    В качестве ключей используются конкатинация строки строки
    Решается в четверо дольше чем список, но за тоже время что и с ключами - случайными числами
    :param n:
    :return:
    """
    temp_dict = {}
    for i in range(n):
        key = "key "
        key += str(i)
        temp_dict[key] = random.random()
    return temp_dict


@time_of_func
def add_list_begin(lst: list):
    lst.insert(0, random.random())


@time_of_func
def add_list_middle(lst: list):
    lst.insert(int(len(lst) / 2), random.random())


@time_of_func
def add_list_end(lst: list):
    lst.insert(int(len(lst)), random.random())


@time_of_func
def add_list_append(lst: list):
    lst.append(random.random())


@time_of_func
def pop_list_begin(lst: list):
    lst.pop(0)


@time_of_func
def pop_list_middle(lst: list):
    lst.pop(int(len(lst) / 2))


@time_of_func
def pop_list_end(lst: list):
    lst.pop()


@time_of_func
def add_dict(dct: dict):
    dct[random.random()] = random.random()


@time_of_func
def pop_dict_elem(dct: dict):
    dct.pop(0)


a = list_constructor(5_000_000)
b = list_constructor_2(5_000_000)
c = dict_constructor(5_000_000)
d = dict_constructor_2(5_000_000)
e = dict_constructor_3(5_000_000)
f = dict_constructor_4(5_000_000)

print("==================================")

add_list_begin(a)
add_list_middle(a)
add_list_end(a)
add_list_append(a)

print("==================================")

pop_list_begin(a)
pop_list_middle(a)
pop_list_end(a)

print("==================================")

add_dict(c)
pop_dict_elem(c)

"""
По второй части задания
По идее все сложности - константные

Очевидно, что когда вставляешь элемент в конец списка все это происходит почти моменталььно, но 
все меняется когда нужно вставить элемент в начало или в середину - так как
нужно изменять весь список... скорее всего он похож здесь на
ArrayList в Java

То же самое происходит и при извлечении элемента по индексу - логика та же

Со словорями все проще потому что они не упорядоченны, скорее всего скорость работы будет зависеть от
сложности хеширования конкретного ключа
"""
