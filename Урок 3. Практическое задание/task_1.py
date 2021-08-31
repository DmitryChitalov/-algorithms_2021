"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
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
import requests
import json
import random
from functools import wraps

"""
Генерируем 500 рандомных элементов для вставки в интересующие структуры данных.
"""
random_words = requests.get('https://random-word-api.herokuapp.com/word', params={'number': 15000})
random_words = list(set(json.loads(random_words.text)))
random_words = [(word, random_words[random.randrange(0, len(random_words) - 1)]) for word in random_words]


def time_check_deco(func):
    @wraps(func)
    def time_check_wrap(*args):
        start = time.time( )
        func_to_check = func(*args)
        end = time.time( )
        final_time = end - start
        return func_to_check, final_time

    return time_check_wrap


@time_check_deco
def dict_fill(values):
    """
     O(n)
    """
    return {value[0]: value[1] for value in values}


@time_check_deco
def list_fill(values):
    """
    O(n)
    """
    return [value for value in values]


dict_won = 0
list_won = 0
for i in range(100):
    my_list = list_fill(random_words)
    my_dict = dict_fill(random_words)
    if my_dict[1] > my_list[1]:
        list_won += 1
    else:
        dict_won += 1
print(f'Заполнение словаря было быстрее {dict_won}, заполнение списка было быстрее {list_won}')
"""
Создание словаря подразумевает создание хэш-таблицы, вычисление хэшей и её заполнение, в то время как,
чтобы добавить значение В КОНЕЦ списка дополнительные расчеты производить не нужно, однако, если бы нам потребовалось
вставить значение по индексу это бы привело к увеличению времени наполнения.
"""


@time_check_deco
def update_dict(dct, values):
    """
    O(n)
    """
    dct.update({value[0]: value[1] for value in values})
    return dct


@time_check_deco
def update_list(lst, values):
    """
    O(n)
    """
    lst.extend([value for value in values])
    return lst


@time_check_deco
def remove_from_list(lst, item):
    """
    O(n)
    """
    lst.remove(item[0])
    return lst


@time_check_deco
def remove_from_dict(dct, item=None):
    """
    O(1)
    """
    dct.popitem( )
    return dct


random_words = requests.get('https://random-word-api.herokuapp.com/word', params={'number': 100})
random_words = list(set(json.loads(random_words.text)))
random_words = [(word + '1', random_words[random.randrange(0, len(random_words) - 1)]) for word in random_words]


def time_test(lst, dct, operation_list, operation_dict):
    dict_won, list_won = 0, 0
    for i in range(100):
        my_list = operation_list(lst[0], random_words)
        my_dict = operation_dict(dct[0], random_words)
        if my_dict[1] > my_list[1]:
            list_won += 1
        else:
            dict_won += 1
    print(f'{operation_dict.__name__} словаря был быстрее {dict_won}, '
          f'{operation_list.__name__} списка был быстрее {list_won}')


time_test(my_list, my_dict, update_list, update_dict)
time_test(my_list, my_dict, remove_from_list, remove_from_dict)
"""
Операции, связанные с расширением структуры и удаления из неё элементов практически всегда быстрее выполняются у
словаря.
"""
