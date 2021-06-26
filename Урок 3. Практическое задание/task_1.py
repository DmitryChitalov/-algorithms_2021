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

from time import time


def time_decorator(func):
    def wrapped(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        stop = time()
        print(stop - start)
        return result

    return wrapped


@time_decorator
def generate_list():
    return [i for i in range(elems)]        # O(1)


@time_decorator
def generate_dict():
    return {i: i for i in range(elems)}     # O(1)


@time_decorator
def change_list(my_lst, nums):
    for i in range(nums):
        my_lst[i] = my_lst[i] + 123         # O(1)


@time_decorator
def change_dict(my_dct, nums):
    for i in range(nums):
        my_dct[i] = '123'                   # O(1)


@time_decorator
def pop_list(my_lst, nums):                 # O(n)
    for i in range(nums):
        my_lst.pop(0)


@time_decorator
def pop_dict(my_dct, nums):                 # O(1)
    for i in range(nums):
        my_dct.pop(i)


elems = 200000

print('Заполняю список:', end=' ')
my_list = generate_list()
print('Заполняю словарь:', end=' ')
my_dict = generate_dict()
print('Изменяю элементы списка:', end=' ')
change_list(my_list, elems)
print('Изменяю элементы словаря:', end=' ')
change_dict(my_dict, elems)
print('Удаляю элементы списка (pop) поэлементно:', end=' ')
pop_list(my_list, elems)
print('Удаляю элементы словаря (pop) поэлементно:', end=' ')
pop_dict(my_dict, elems)

# Для заданном значении elems (200000) список заполняется чуть быстрее, чем словарь (вычисление хеша),
# изменение целых значений 123, 124 .. списка и изменение значений "123" словаря также происходит в одном порядке,
# а вот удаление значений списка происходит значительно медленнее, чем удаление пар ключ-значение.
# В моем примере все операции происходят со сложностью O(1), кроме pop_list, которая использует сложность O(n).
