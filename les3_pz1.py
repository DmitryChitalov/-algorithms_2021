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


def check_time(func):
    def wrapper(*args, **kwargs):
        start_val = time.time()
        res = func(*args, **kwargs)
        print(f'Время выполнения: {time.time() - start_val}')
        return res

    return wrapper


@check_time
def fill_list(n):
    my_list = []
    for i in range(n):  # O(n)
        my_list.append(i)  # O(1
    return my_list


@check_time
def fill_dict(n):
    my_dict = {}
    for i in range(n):  # O(n)
        my_dict[i] = i  # # O(1)
    return my_dict


@check_time
def dict_change(my_dict):
    my_dict[0] = 12  # O(1)


@check_time
def list_change(my_list):
    my_list.insert(0, 12)  # O(N)


@check_time
def list_append(my_list):
    my_list.append(12)  # O(N)


@check_time
def dict_pop(my_dict):
    my_dict.pop(44)  # O(N)


@check_time
def list_pop(my_list):
    my_list.pop(48)  # O(1)


print('Заполнение списка:')
temp_list = fill_list(10000000)
print('Заполнение словаря:')
temp_dict = fill_dict(10000000)
# Заполнение словаря происходит чуть медленнее чем списка
dict_change(temp_dict)
list_change(temp_list)
list_append(temp_list)
dict_pop(temp_dict)
list_pop(temp_list)
# Выполнение операций со словарем происходит быстрее, чем со списком
