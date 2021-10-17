"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""
from collections import deque
from timeit import timeit


def filling_list(list_len):
    """
    Заполнение списка.
    Сложность: O(N)
    :param list_len:
    :return:
    """
    test_list = list([i + 1 for i in range(0, list_len)])  # O(N).
    return test_list


def filling_deque(list_len):
    """
    Заполнение деки.
    Сложность: O(N)
    :param list_len:
    :return:
    """
    test_deque = deque([i + 1 for i in range(0, list_len)])  # O(N).
    return test_deque


# Будем работать со 100 тысячями элементов.
el_count = 100000


# region List operation
def get_val_from_list(test_list, index):
    """
    Returns the index of the element in the list.
    Сложность: O(N).
    """
    return test_list.index(index)


def insert_list(list_len):
    """
    Заполнение списка через insert.
    Сложность # O(N).
    Скорость работы: 0.007906436920166016
    :param list_len:
    :return:
    """
    test_list = list()
    test_list.insert(0, [i + 1 for i in range(0, list_len)])  # O(N).
    return test_list


def append_list(list_len):
    """
    Заполнение списка через append.
    Сложность: O(N).
    Скорость работы: 0.00709223747253418
    :param list_len:
    :return:
    """
    test_list = list()
    test_list.append([i + 1 for i in range(0, list_len)])  # O(1).
    return test_list


def list_pop(test_list):
    """
    Removes element at the given index.
    Сложность: O(1).
    """
    return test_list.pop()


def list_popleft(test_list):
    """
    Removes first element at the given index.
    Сложность: O(1).
    """
    return test_list.pop(0)


def list_extend(donor_list, recipient_test_list):
    """
    Adds iterable elements to the end of the list.
    Сложность: O(N).
    """
    return recipient_test_list.extend(donor_list)


# endregion


# region Deque operation
def get_val_from_deque(test_deque, index):
    """
    Returns the index of the element in the deque.
    Сложность: O(N).
    """
    return test_deque.index(index)


def insert_deque(list_len):
    """
    Заполнение деки через insert.
    Сложность # O(N).
    :return:
    """
    test_deque = deque()
    test_deque.insert(0, [i + 1 for i in range(0, list_len)])  # O(N).
    return test_deque


def append_deque(list_len):
    """
    Заполнение списка через append.
    Сложность: O(N).
    Скорость работы: 0.00709223747253418
    :param list_len:
    :return:
    """
    test_deque = deque()
    test_deque.append([i + 1 for i in range(0, list_len)])  # O(1).
    return test_deque


def append_left_deque(list_len):
    """
    Заполнение списка через append.
    Сложность: O(N).
    Скорость работы: 0.00709223747253418
    :param list_len:
    :return:
    """
    test_deque = deque()
    test_deque.appendleft([i + 1 for i in range(0, list_len)])  # O(1).
    return test_deque


def deque_pop(test_deque):
    """
    Removes element at the given index.
    Сложность: O(N).
    """
    return test_deque.pop()


def deque_popleft(test_deque):
    """
    Removes first element at the given index.
    Сложность: O(N).
    """
    return test_deque.popleft()


def deque_extend(donor_deque, recipient_test_deque):
    """
    Adds iterable elements to the end of the deque.
    Сложность: O(N).
    """
    return recipient_test_deque.extend(donor_deque)


def deque_extend_left(donor_deque, recipient_test_deque):
    """
    Adds iterable elements to the end of the deque.
    Сложность: O(N).
    """
    return recipient_test_deque.extendleft(donor_deque)


# endregion


def get_new_list(elements_count):
    return [i + 1 for i in range(0, elements_count)]


def get_new_deque(elements_count):
    return deque([i + 1 for i in range(0, elements_count)])


print("filling_list: ", timeit(stmt="filling_list(el_count)", globals=globals(), number=10000))
print("filling_deque: ", timeit(stmt="filling_deque(el_count)", globals=globals(), number=10000))

# List.
print("get_val_from_list: ", timeit(stmt="get_val_from_list(get_new_list(el_count), 37)", globals=globals(),
                                    number=1000))
print("insert_list: ", timeit(stmt="insert_list(el_count)", globals=globals(), number=1000))
print("append_list: ", timeit(stmt="append_list(el_count)", globals=globals(), number=1000))
print("list_pop: ", timeit(stmt="list_pop(get_new_list(el_count))", globals=globals(), number=1000))
print("list_popleft: ", timeit(stmt="list_popleft(get_new_list(el_count))", globals=globals(), number=1000))
print("list_extend: ", timeit(stmt="list_extend(get_new_list(el_count), get_new_list(el_count))",
                              globals=globals(), number=1000))

# Deque.
print("get_val_from_deque: ", timeit(stmt="get_val_from_deque(get_new_deque(el_count), 58)",
                                     globals=globals(), number=1000))
print("insert_deque: ", timeit(stmt="insert_deque(el_count)", globals=globals(), number=1000))
print("append_deque: ", timeit(stmt="append_deque(el_count)", globals=globals(), number=1000))
print("append_left_deque: ", timeit(stmt="append_left_deque(el_count)", globals=globals(), number=1000))
print("deque_pop: ", timeit(stmt="deque_pop(get_new_deque(el_count))", globals=globals(), number=1000))
print("deque_popleft: ", timeit(stmt="deque_popleft(get_new_deque(el_count))", globals=globals(), number=1000))
print("deque_extend: ", timeit(stmt="deque_extend(get_new_deque(el_count), get_new_deque(el_count))",
                               globals=globals(), number=1000))
print("deque_extend_left: ", timeit(stmt="deque_extend_left(get_new_deque(el_count), get_new_deque(el_count))",
                                    globals=globals(), number=1000))

"""
> 1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
filling_list:  69.8880202
filling_deque:  75.425073
Время с учётом генерации элементов для списка и очереди. Тестировалось на 10000 повторениях.
Заполнение очереди происходит медленнее, чем списка.

> 2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.
1. Получение элемента по индексу:
get_val_from_list:  7.0271761999999995
get_val_from_deque:  7.739389100000004
С увеличение количества элементов list опережает deque.

2. Вставка в начало.
insert_list:  6.728709800000001
insert_deque:  6.569135000000003
С увеличением элементов, deque опережает list.

3. Добавление элементов в конец списка.
append_list:  6.613134200000001
append_deque:  6.568204900000005
Почти равны, но с увеличением элементов, deque опережает list.

4. append_left_deque, вероятно, лучше сравнивать с insert_list
insert_list:  6.728709800000001
append_left_deque:  6.581903899999993
Deque опережает list.

5. Pop. Удаление элемента справа.
list_pop:  6.781898300000002
deque_pop:  7.540163499999991
list выигрывает по скоорости.

6. Pop. Удаление элемента слева.
list_popleft:  7.018758999999999
deque_popleft:  7.362741100000008
Странно, но list опять выигрывает по скоорости.

7. Расширение словаря и очереди.
list_extend:  14.734861800000001
deque_extend:  16.180441799999997
list выигрывает по скоорости. 

Словарь не имеет встроенной функции расширения слева.
deque_extend_left:  16.111045500000003
"""
