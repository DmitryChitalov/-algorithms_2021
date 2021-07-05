from time import time


def timer(function):  # создадим декоратор таймер, сложность зависит от функции
    def func(value):
        start_timer = time()
        result = function(value)
        print(f'Выполнено за: {time() - start_timer} сек.')
        return result
    return func


@timer                      # заполняем список O(1)
def list_fill(num):
    print('Заполняем список: ')
    fill = [el for el in range(num)]
    return fill


@timer                      # заполняем словарь O(1)
def dict_fill(num):
    print('Заполняем словарь: ')
    fill = {el: el for el in range(num)}
    return fill


@timer                      # добавляем в список O(n)
def add_to_list(lst):
    count = len(lst)
    i = 1
    while i < volume:
        lst.append(count + 1)
        i += 1
    print('Добавляем элементы в список: ')
    return


@timer                      # добавляем в словарь O(n)
def add_to_dict(dct):
    count = len(dct)
    i = 1
    while i < volume:
        dict.update({count: count})
        count += 1
        i += 1
    print('Добавляем элементы в словарь: ')
    return


@timer                      # удаляем из списка O(n)
def list_pop(lst):
    i = 0
    while i < volume:
        lst.pop()
        i += 1
    print('Удаляем из списка: ')
    return


@timer                      # Удаляем из словаря O(n)
def dict_pop(dct):
    i = 0
    while i < volume:
        dct.popitem()
        i += 1
    print('Удаляем из словаря: ')
    return


@timer                      # очищаем список O(1)
def list_clear(lst):
    print('Очищаем список')
    return lst.clear()


@timer                      # очищаем словарь O(1)
def dict_clear(dct):
    print('Очищаем словарь')
    return dct.clear()


volume = 10000000

list_model = list_fill(volume)
dict_model = dict_fill(volume)
print('&'*50, '\n')

add_to_list(list_model)
add_to_dict(dict_model)
print('&'*50, '\n')

list_pop(list_model)
dict_pop(dict_model)
print('&'*50, '\n')

list_clear(list_model)
dict_clear(dict_model)

"""
Результаты работы программы для 10 миллионов элементов:
Заполняем список:
Выполнено за: 0.5114560127258301 сек.
Заполняем словарь:
Выполнено за: 0.8740930557250977 сек.
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Добавляем элементы в список:
Выполнено за: 1.3955559730529785 сек.
Добавляем элементы в словарь:
Выполнено за: 2.4265806674957275 сек.
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Удаляем из списка:
Выполнено за: 1.0099501609802246 сек.
Удаляем из словаря:
Выполнено за: 1.2177402973175049 сек.
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Очищаем список
Выполнено за: 0.10389375686645508 сек.
Очищаем словарь
Выполнено за: 0.010987043380737305 сек.
--------------------------------------------------
Выводы:
при заполнении и добавлении выигрывает список,
при удалении практически на равных,
а вот при очистке так вообще кратно выиграл словарь
Итог:
Если необходима работа непосредственно с данными внутри списка и словаря
то словарь однозначно лучше.
Но если речь идет о самой структуре (создание, добавление, удаление)
не касаясь самих данных, то список в приоритете.
"""