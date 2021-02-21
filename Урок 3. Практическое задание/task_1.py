import time

"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""


def time_taken(function):
    def timer(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        finish_time = time.time()
        print(f"Выполнение функции заняло {finish_time - start_time}")
        return result

    return timer


@time_taken
def fill_list(length):
    print('Заполнение списка')
    final_list = []
    for elem in range(length):
        final_list.append(elem)
    return final_list


@time_taken
def fill_dict(length):
    print('Заполнение словаря')
    final_dict = {}
    for elem in range(length):
        final_dict[elem] = f'{elem}'
    return final_dict


test_list = (fill_list(1000000))
test_dict = (fill_dict(1000000))
"""
a) Быстрее заполняется список, примерно в 3 раза на 1000000 элементах.
   Причина: Заполнение списка происходит в конец, что занимает меньше времени, чем добавление элемента в словарь
"""


@time_taken
def list_search_el(my_list, a):
    print("Поиск эелемента в спике")
    for el in my_list:
        if el == a:
            return el


@time_taken
def dict_search_key(my_dict, key):
    print("Поиск эелемента в словаре по ключу")
    return my_dict[key]


@time_taken
def dict_search_val(my_dict, a):
    print("Поиск эелемента в словаре по значению")
    for val in my_dict.values():
        if val == a:
            return val


print(list_search_el(test_list, 423434))
print(dict_search_key(test_dict, 1356))
print(dict_search_val(test_dict, '1264433'))
"""
Поиск элементов по ключу в словаре выполняется быстрее, чем поиска элемента в списке(не по индексу).
Причина: Словарь является хеш таблицей. 
Поиск элемента по значению в словаре выполняется дольше, так как проверяются все значения до нужного.
"""


@time_taken
def add_to_list(my_list, val, position):
    print("Добавление элемента в список")
    test_list.insert(position, val)
    return "Функция закончена"


@time_taken
def add_to_dict(my_dict, key, val):
    print("Добавление элемента в словарь")
    my_dict.update({key: val})
    return "Функция закончена"


print(add_to_list(test_list, 12314, 33))
print(add_to_dict(test_dict, 'lol', 231))


"""
Добавление элемента в список выполняется медленнее чем в словаре, если вставка идет в определенное место.
Добавление элементов в конец списка выполняется быстрее, чем у словаря.
Причина: Добавление элементов в словарь выполняется за констатное время, а список не упорядочен,
значит время будет зависеть от места элемента в списке.( Удаление определенных элементов также быстрее у словаря) 
"""

