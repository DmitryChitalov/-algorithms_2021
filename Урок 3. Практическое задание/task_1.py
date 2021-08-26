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


def time_decorator(func):
    def time_check(*args):
        start_time = time.perf_counter_ns()
        result = func(*args)
        end_time = time.perf_counter_ns()
        print(f'Время выполнения: {end_time - start_time}')
        return result

    return time_check


my_list = []
my_dict = {}


@time_decorator
def list_fill(*args):
    """Сложность функции O(N)"""
    for el in args:  # O(N)
        my_list.append(el)  # O(1)
    return my_list


@time_decorator
def dict_fill(*args):
    """Сложность функции O(N)"""
    k = 1  # O(1)
    for v in args:  # O(N)
        my_dict[k] = v  # O(1)
        k += 1  # O(1)
    return my_dict


print(list_fill(
    'Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur',
    'adipisicing', 'elit', 'Eligendi', 'non'
))
print(dict_fill(
    'Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur',
    'adipisicing', 'elit', 'Eligendi', 'non'
))


# В среднем время выполнения функций одинаково так как они имеют одинаковую сложность

@time_decorator
def el_remove_list(idx):
    my_list.pop(idx)  # O(N)


@time_decorator
def el_remove_dict(key):
    my_dict.pop(key)  # O(1)


print(el_remove_list(1))
print(el_remove_dict(1))

# Функиция удаления элемента из словаря работает быстрее, так как имеет константную сложность
