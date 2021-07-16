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
    Обёртка для измерения времени выполнения функций.
    """

    def wrapper(*arg, **kw):
        t1 = time.time()
        func(*arg, **kw)
        t2 = time.time()
        return (t2 - t1), func.__name__

    return wrapper


# Заполнение списка и словаря.

@calc_timing
def filling_list(list_len, step):
    """
    Заполнение списка.
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
    Сложность: O(N)
    :param list_len:
    :param step:
    :return:
    """
    test_dict = {i + step: i for i in range(0, list_len, step)}  # O(N)
    return test_dict


@calc_timing
def append_list(list_len, step):
    """
    Заполнение списка через append.
    Сложность: O(N).
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


# Далее list и dict operation.

# region List operation
@calc_timing
def list_clear(test_list):
    """
    Removes all Items from the List.
    Сложность: O(1).
    """
    return test_list.clear()


@calc_timing
def list_copy(test_list):
    """
    Returns a shallow copy of the list.
    Сложность: O(N).
    """
    test_list_copy = test_list.copy()
    return test_list_copy


@calc_timing
def list_count(test_list, element):
    """
    Returns count of the element in the list.
    Сложность: O(N).
    """
    return test_list.count(element)


@calc_timing
def list_extend(donor_list, recipient_test_list):
    """
    Adds iterable elements to the end of the list.
    Сложность: O(N).
    """
    return recipient_test_list.extend(donor_list)


@calc_timing
def list_index(test_list, index):
    """
    Returns the index of the element in the list.
    Сложность: O(N).
    """
    return test_list.index(index)


@calc_timing
def list_pop(test_list, index):
    """
    Removes element at the given index.
    Сложность: O(N).
    """
    return test_list.pop(index)


@calc_timing
def list_remove(test_list, item):
    """
    Removes item from the list.
    Сложность: O(N).
    """
    return test_list.remove(item)


@calc_timing
def list_reverse(test_list):
    """
    Reverses the list.
    Сложность: O(N).
    """
    return test_list.reverse()


@calc_timing
def list_sort(test_list, reverse):
    """
    Sort list.
    Сложность: O(N log N).
    """
    return test_list.sort(reverse=reverse)


# endregion


# region Dict operation
@calc_timing
def dict_clear(test_dict):
    """
    Removes all the elements from the dictionary.
    Сложность: O(1).
    """
    return test_dict.clear()


@calc_timing
def dict_copy(test_dict):
    """
    Returns a copy of the dictionary.
    Сложность: O(N).
    """
    test_dict_copy = test_dict.copy()
    return test_dict_copy


@calc_timing
def dict_fromkeys(keys, values):
    """
    Returns a dictionary with the specified keys and value.
    Сложность: O(N).
    """
    return dict.fromkeys(keys, values)


@calc_timing
def dict_get(test_dict, key):
    """
    Returns the value of the specified key.
    Сложность: O(1).
    """
    return test_dict.get(key)


@calc_timing
def dict_items(test_dict):
    """
    Returns a list containing a tuple for each key value pair.
    Сложность: O(N).
    """
    return test_dict.items()


@calc_timing
def dict_keys(test_dict):
    """
    Returns a list containing the dictionary's keys.
    Сложность: O(N).
    """
    return test_dict.keys()


@calc_timing
def dict_pop(test_dict, key):
    """
    Removes the element with the specified key.
    Сложность: O(1).
    """
    return test_dict.pop(key)


@calc_timing
def dict_popitem(test_dict):
    """
    Removes the last inserted key-value pair.
    Сложность: O(1).
    """
    return test_dict.popitem()


@calc_timing
def dict_setdefault(test_dict, key, value):
    """
    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value.
    Сложность: O(1).
    """
    return test_dict.setdefault(key, value)


@calc_timing
def dict_update(test_dict, key, value):
    """
    Updates the dictionary with the specified key-value pairs.
    Сложность: O(1).
    """
    return test_dict.update({key: value})


@calc_timing
def dict_values(test_dict):
    """
    Returns a list of all the values in the dictionary.
    Сложность: O(N).
    """
    return test_dict.values()


@calc_timing
def dict_sort(test_dict):
    """
    Sort dict by keys.
    Сложность O(N log N)
    """
    return dict(sorted(test_dict.items()))


# endregion


def get_new_list(elements_count):
    return [i + 1 for i in range(0, elements_count)]


def get_new_dict(elements_count):
    return {i + 1: i for i in range(0, elements_count)}


# БУдем работать с миллионом записей.
el_count = 1000000

# 1.a. Заполнение списка и словаря.
print(filling_list(el_count, 1))
print(filling_dict(el_count, 1))

# 1.b. Операции и со списком, и со словарем.

# List.
print(append_list(el_count, 1))

print(insert_list(el_count, 1))

print(list_clear(get_new_list(el_count)))

print(list_copy(get_new_list(el_count)))

print(list_count(get_new_list(el_count), 100))

print(list_extend(get_new_list(el_count), get_new_list(el_count)))

print(list_index(get_new_list(el_count), 2000))

print(list_pop(get_new_list(el_count), 3000))

print(list_remove(get_new_list(el_count), 350))

print(list_reverse(get_new_list(el_count)))

print(list_sort(get_new_list(el_count), True))

# Dict.
print(dict_clear(get_new_dict(el_count)))

print(dict_copy(get_new_dict(el_count)))

print(dict_fromkeys(get_new_dict(el_count).keys(), get_new_dict(el_count).values()))

print(dict_get(get_new_dict(el_count), 10000))

print(dict_items(get_new_dict(el_count)))

print(dict_keys(get_new_dict(el_count)))

print(dict_pop(get_new_dict(el_count), 14568))

print(dict_popitem(get_new_dict(el_count)))

print(dict_setdefault(get_new_dict(el_count), 1001, "test"))

print(dict_update(get_new_dict(el_count), 10000, "value_212121"))

print(dict_values(get_new_dict(el_count)))

print(dict_sort(get_new_dict(el_count)))

"""
Выводы:

1.a. Заполнение списка и словаря. Генерация list быстрее генерации dict при одинаковой сложности O(N) и 
одинаковом количестве генерируемых элементов, т.к. при заполнении словаря происходит заполнение хеш-таблицы.

Время выполнения:
(0.08512115478515625, 'filling_list')
(0.1157064437866211, 'filling_dict')

Но создание словаря из 2-х списков fromkeys, быстрее чем просто генерация. Но на создание списков тоже нужно время, 
которое тут не учитывается:
(0.04140901565551758, 'dict_fromkeys')

1.b. Операций и со списком, и со словарем.
1) Clear:
(0.002322673797607422, 'list_clear') 
(0.01041865348815918, 'dict_clear')
Очистка списка быстрее чем словаря.

2) Copy:
(0.008136987686157227, 'list_copy')
(0.02075648307800293, 'dict_copy')
Копирование списка быстрее чем словаря.

3) Pop:
(0.0, 'list_pop')
(0.0, 'dict_pop')
Оба по нулям. У обоих сложносто O(1).

4) Sort:
(0.008093118667602539, 'list_sort')
(0.11649441719055176, 'dict_sort')
При одинаковой сложности O(N log N), сортировака списка быстрее чем словаря.

Генерация list через append в конец списка, быстрее чем через insert в нулевую позицию:
(0.08246016502380371, 'append_list')
(0.08321833610534668, 'insert_list')

Операции, которое заняли нулевое время со списком:
(0.0, 'list_index')
(0.0, 'list_remove')
(0.0, 'list_reverse')

Остальные операции списка:
(0.0022134780883789062, 'list_count')
(0.008063316345214844, 'list_extend')

Операции, которое заняли нулевое время со словарём:
(0.0, 'dict_get')
(0.0, 'dict_items')
(0.0, 'dict_keys')
(0.0, 'dict_popitem')
(0.0, 'dict_setdefault')
(0.0, 'dict_update')
(0.0, 'dict_values')
"""
