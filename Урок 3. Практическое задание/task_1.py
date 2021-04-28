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

from time import time


def exec_time(func):

    def wrapper(*args, **kwargs):

        execution_time = time()
        result = func(*args, **kwargs)
        execution_time = time() - execution_time

        print(f'Функция {func.__name__} выполнилась за {execution_time}')
        return result

    return wrapper


# заполняем список указанным количеством не значащих элементов
@exec_time
def fill_list(elem_count):
    return [None for _ in range(elem_count)]


# заполняем словарь указанным количеством не значащих элементов
@exec_time
def fill_dict(elem_count):
    return {i: None for i in range(elem_count)}


# получаем элементы по индексу
@exec_time
def get_list_elem(lst, elem_count):
    for i in range(elem_count):
        lst[i]


# получаем элементы по ключу
@exec_time
def get_dict_elem(dct, elem_count):
    for i in range(elem_count):
        dct[i]


# удаляем элементы c начала списка
@exec_time
def del_from_list_begin(lst, elem_count):
    for i in range(elem_count):
        del lst[i]


# удаляем элементы c конца списка
@exec_time
def del_from_list_end(lst, elem_count):
    for i in range(elem_count):
        lst.pop()


# удаляем элементы из словаря
@exec_time
def del_from_dict(dct, elem_count):
    for i in range(elem_count):
        del dct[i]


# добавляем элемент в середину списка
@exec_time
def insert_into_list(lst, item_num):
    lst.insert(item_num, None)


# добавляем элемент в словарь
@exec_time
def insert_into_dict(dct, key):
    dct[key] = None


if __name__ == '__main__':

    # Заполняем список и словарь 10 000 000 элементов
    test_list = fill_list(10000000)
    test_dict = fill_dict(10000000)
    '''
    Функция fill_list выполнилась за 0.5010907649993896
    Функция fill_dict выполнилась за 0.9651088714599609
    Заполнение списка и словаря имеет одинаковую сложность O(n),
    список заполняется быстрее, т.к при заполнении словаря тратится время на рассчёт хешей
    '''

    # поиск значений 1 000 000 элементов
    get_list_elem(test_list, 1000000)
    get_dict_elem(test_dict, 1000000)
    '''
    Функция get_list_elem выполнилась за 0.04797053337097168
    Функция get_dict_elem выполнилась за 0.046874284744262695
    Поиск элементов списка по индексу и элементов словаря по ключу
    имеют аналогичную сложность - O(1), константную
    и выполняются за примерно равное время
    '''

    # Удаление 1000 элементов
    del_from_list_begin(test_list, 1000)
    del_from_list_end(test_list, 1000)
    del_from_dict(test_dict, 1000)
    '''
    Функция del_from_list_begin выполнилась за 10.713992357254028
    Функция del_from_list_end выполнилась за 0.0
    Функция del_from_dict выполнилась за 0.0
    Удаление элементов из начала списка имеет сложность O(n) и
    происходит значительно дольше, чем удаление последних элементов скаска или
    удвление элементов из словаря, т.к. список каждый раз приходится перестраивать.
    Удаление элементов с конца списка методом pop() не влияет на его структуру
    и выполняется за константное время.
    Удаление элементов словаря всегда происходит очень быстро, т.к.
    элементы словаря не упорядочены и удаление одного не влияет на остальные.
    '''

    # Вставка элемента
    insert_into_list(test_list, 100000)
    insert_into_dict(test_dict, 20000000)
    '''
    Функция insert_into_list выполнилась за 0.015629053115844727
    Функция insert_into_dict выполнилась за 0.0
    Добавление элемента аналогично удалению.
    Для списка вызывает его перестраивание и выполняется за линейное O(n) время.
    Для словаря выполняется мгновенно.
    '''
