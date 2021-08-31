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


def time_check(some_func):
    def time_func(*args, **kwargs):
        start_time = time()
        func_result = some_func(*args, **kwargs)
        end_time = time()
        print(f'{end_time - start_time}')
        return func_result
    return time_func


@time_check
def full_list(some_list, num):
    for i in range(num):
        some_list.append(i)  # O(1)


@time_check
def full_dict(some_dict, num):
    for i in range(num):
        some_dict[i] = i  # O(1)


@time_check
def list_pop(some_list, num):
    some_list.pop(num)  # O(n)


@time_check
def list_clear(some_list):
    some_list.clear()  # O(1)


@time_check
def dict_pop(some_dict, num):
    some_dict.pop(num)  # O(1)


@time_check
def dict_clear(some_dict):
    some_dict.clear()  # O(1)


my_list = []
my_dict = {}

print('Заполнение списка')
full_list(my_list, 1000000)
print('Заполнение словаря')
full_dict(my_dict, 1000000)

"""
Вывод:
Для выбранных функций время заполнения практически не отличается.
"""

print('Удаление элемента списка')
list_pop(my_list, 10000)
print('Очистка списка')
list_clear(my_list)

print('Удаление элемента словаря')
dict_pop(my_dict, 10000)
print('Очистка словаря')
dict_clear(my_dict)

"""
Вывод:
Время очистки через функцию clear практически не отличается.
Время удаления элемента для словаря быстрее, так как сложность O(1) против O(n) у списка.
"""
