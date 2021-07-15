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


def calc_timing(func):
    """
    Обёртка для измерения времен выполнения функций.
    :param func:
    :return:
    """

    def wrapper(*arg, **kw):
        t1 = time.time()
        func(*arg, **kw)
        t2 = time.time()
        return (t2 - t1), func.__name__

    return wrapper


@calc_timing
def filling_list(list_len, step):
    """
    Заполнение списка.
    Скорость работы: 0.006106853485107422
    Сложность: O(N)
    :param list_len:
    :param step:
    :return:
    """
    test_list = [i + step for i in range(0, list_len, step)]  # O(N).
    return test_list


@calc_timing
def filling_dict(list_len, step):
    """
    Заполненеие словаря.
    Скорость работы: 0.011882305145263672
    Сложность: O(N)
    :param list_len:
    :param step:
    :return:
    """
    test_dict = {i + step: i for i in range(0, list_len, step)}  # O(N)
    return test_dict


print(filling_list(100000, 1))
print(filling_dict(100000, 1))

"""
Вывод: Генерация list быстрее генерации dict при одинаковой сложности O(N) и 
одинаковом количестве генерируемых элементов.
"""


@calc_timing
def append_list(list_len, step):
    """
    Заполнение списка через append.
    Генерация 0(N), append 0(1). В целом сложность функции O(N).
    Скорость работы: 0.00709223747253418
    :param list_len:
    :param step:
    :return:
    """
    test_list = list()
    test_list.append([i + step for i in range(0, list_len, step)])  # O(1).
    return test_list


@calc_timing
def insert_list(list_len, step):
    """
    Заполнение списка через insert.
    Сложность # O(N).
    Скорость работы: 0.007906436920166016
    :param list_len:
    :param step:
    :return:
    """
    test_list = list()
    test_list.insert(0, [i + step for i in range(0, list_len, step)])  # O(N).
    return test_list


print(append_list(100000, 1))
print(insert_list(100000, 1))

""" Вывод: Генерация list через append в конец списка, быстрее чем через insert в нулевую позицию."""


@calc_timing
def list_clear(test_list):
    """
    Removes all Items from the List.
    """
    return test_list.clear()


@calc_timing
def list_copy(test_list):
    """
    Returns a shallow copy of the list
    """
    test_list_copy = test_list.copy()
    return test_list_copy


@calc_timing
def list_count(test_list, element):
    """
    Returns count of the element in the list
    """
    return test_list.count(element)


@calc_timing
def list_extend(donor_list, recipient_test_list):
    """
    Adds iterable elements to the end of the list.
    """
    return recipient_test_list.extend(donor_list)


@calc_timing
def list_index(test_list, index):
    """
    Returns the index of the element in the list.
    """
    return test_list.index(index)


@calc_timing
def list_pop(test_list, index):
    """
    Removes element at the given index.
    """
    return test_list.pop(index)


@calc_timing
def list_remove(test_list, item):
    """
    Removes item from the list
    """
    return test_list.remove(item)


@calc_timing
def list_reverse(test_list):
    """
    Reverses the list
    """
    return test_list.reverse()


@calc_timing
def list_sort(test_list, reverse):
    """
    Sort list.
    """
    return test_list.sort(reverse=reverse)


# List.
tst_lst = [i + 1 for i in range(0, 100000, 1)]  # O(N).
print(list_clear(tst_lst))

tst_lst = [i + 1 for i in range(0, 100000, 1)]  # O(N).
print(list_copy(tst_lst))

tst_lst = [i + 1 for i in range(0, 100000, 1)]  # O(N).
print(list_count(tst_lst, 100))

new_list = tst_lst.copy()
print(list_extend(new_list, tst_lst))

tst_lst = [i + 1 for i in range(0, 100000, 1)]  # O(N).
print(list_index(tst_lst, 2000))

print(list_pop(tst_lst, 3000))

tst_lst = [i + 1 for i in range(0, 100000, 1)]  # O(N).
print(list_remove(tst_lst, 350))

tst_lst = [i + 1 for i in range(0, 100000, 1)]  # O(N).
print(list_reverse(tst_lst))

tst_lst = [i + 1 for i in range(0, 100000, 1)]  # O(N).
print(list_sort(tst_lst, True))


# Dict.

@calc_timing
def dict_clear(test_dict):
    """
    Removes all the elements from the dictionary.
    """
    return test_dict.clear()


@calc_timing
def dict_copy(test_dict):
    """
    Returns a copy of the dictionary.
    """
    test_dict_copy = test_dict.copy()
    return test_dict_copy




"""
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""
