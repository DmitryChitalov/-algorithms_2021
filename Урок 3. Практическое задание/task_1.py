"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

from time import time
from random import randint


num = 10000000


def decor_timer(function):                  # Создаем декоратор - таймер
    def timer(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        print(f'Время, на операцию: {round(time() - start_time, 5)} сек.')
        return result
    return timer


@decor_timer
def main_list(n):
    print('Заполнение списка:')
    result = [i for i in range(n)]
    return result


main_list_list = main_list(num)


@decor_timer
def main_dict(n):
    print('Заполнение словаря:')
    result = {i: i for i in range(n)}
    return result


main_dict_dict = main_dict(num)

# Время, на заполнение списка: 0.59339 сек.
# Время, на заполнение словаря: 0.89708 сек.
# список заполняется быстрее, т.к. при генерации словаря создаются хеши


@decor_timer
def list_find(n):
    print('Поиск в листе:')
    n.index(randint(0, num))


list_find(main_list_list)


@decor_timer
def dict_find(n):
    print('Поиск в словаре:')
    n.get(randint(0, num))


dict_find(main_dict_dict)

# Время, на поиск в списке: 0.00901 сек.
# Время, на поиск в  словаре: 0.0 сек.
# Словарь это хеш-таблица, поэтому поиск в нём быстрее. Поиск в списке линейный.


@decor_timer
def clear_list(n):
    print('Очищение списка:')
    n.clear()


clear_list(main_list_list)


@decor_timer
def clear_dict(n):
    print('Очищение словаря:')
    n.clear()


clear_dict(main_dict_dict)

# Время, на очищение списка: 0.13788 сек.
# Время, на очищение словаря: 0.21177 сек.
# Очистка словаря происходит медленее из за строения ключ - значение и наличия хеш.
