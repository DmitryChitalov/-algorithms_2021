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
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
import time


def time_checker(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'Операция {func.__name__} заняла {end - start} времени')
        return return_value

    return wrapper


@time_checker
def append_to_list(elements, lst):
    for elem in range(elements):
        lst.append(elem)  # O(1)
    return lst


@time_checker
def insert_to_list(elements, lst):
    for elem in range(elements):
        lst.insert(0, elem)  # O(n)
    return lst


@time_checker
def add_to_dict(elements, dct):  # выполняется быстрее благодаря константной сложности
    for elem in range(elements):
        dct[elem] = elem  # O(1)
    return dct


a = []
b = dict()

print(append_to_list(10, a))
print(insert_to_list(10, a))
print(add_to_dict(10, b))


@time_checker
def pop_from_list(lst):
    lst.pop()  # O(1)
    return lst


@time_checker
<<<<<<< Updated upstream
def pop_from_dict(key, dct):  # работает быстрее, чем pop из списка, так как используется хеш-значение ключа
=======
def pop_from_dict(key, dct):
>>>>>>> Stashed changes
    dct.pop(key)  # O(1)
    return dct


@time_checker
def get_list_elem(index, lst):
    return lst[index]  # O(1)


@time_checker
<<<<<<< Updated upstream
def get_dict_elem(key, dct):  # работает быстрее, чем со списком, так как используется хеш-значение ключа
=======
def get_dict_elem(key, dct):
>>>>>>> Stashed changes
    return dct[key]  # O(1)


@time_checker
def change_list_elem(index, lst):
    lst[index] = lst[index + 1]  # O(1)
    return lst


@time_checker
<<<<<<< Updated upstream
def change_dict_elem(key, dct):  # работает быстрее, чем со списком, так как используется хеш-значение ключа
=======
def change_dict_elem(key, dct):
>>>>>>> Stashed changes
    dct[key] = key + 1  # O(1)
    return dct


print(pop_from_list(a))
print(pop_from_dict(3, b))
print(get_list_elem(1, a))
print(get_dict_elem(2, b))
print(change_list_elem(4, a))
print(change_dict_elem(5, b))
<<<<<<< Updated upstream
=======

'''
1) Заполнение списка и словаря:
Операция append_to_list заняла 3.0994415283203125e-06 времени
Операция insert_to_list заняла 3.0994415283203125e-06 времени
Операция add_to_dict заняла 1.9073486328125e-06 времени
Вывод: добавление элемента в словарь за счет константной сложности происходит быстрее, даже по сравнению с операцией 
append у списка, которая также имеет константую сложность, так как при заполнении словаря заполняется хэш-таблица;
2) операции удаления: 
Операция pop_from_list заняла 0.0 времени
Операция pop_from_dict заняла 0.0 времени
Вывод: операция pop происходит за одинаковое количество времени, так как сложность ее константная;
3) операции взятия по индексу/ключу:
Операция get_list_elem заняла 9.5367431640625e-07 времени
Операция get_dict_elem заняла 0.0 времени
Вывод: операция со словарем быстрее, так как при поиске используется хэш-таблица;
4) операции изменения элемента:
Операция change_list_elem заняла 9.5367431640625e-07 времени
Операция change_dict_elem заняла 7.152557373046875e-07 времени
Вывод: операция изменения элемента с поиском по индексу/ключу показала лучшие результаты у словаря, так как при поиске 
используется хэш-таблица;
5) общий итог:
операции со словарем происходят быстрее, так как почти все они константной сложности и словарь использует хэш таблицу 
для быстрого доступа к элементам. 
'''
>>>>>>> Stashed changes
