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


def timer(func):
    def wrapper(*args):
        start_val = time.time()
        res = func(*args)
        end_val = time.time()
        print(f"func_time: {end_val - start_val}")
        return res

    return wrapper


@timer
def input_lst_1(n):  # Сложность O(n)
    lst1 = list()
    for i in range(n):
        lst1.append(i)
    return lst1


@timer
def input_lst_2():  # Сложность O(1), но общее время зависит от пользовательскаго ввода
    lst2 = [input('0: '), input('1: '), input('2: '), input('3: '), input('4: ')]
    return lst2


@timer
def input_lst_3(n1, n2):  # Сложность O(n)
    lst3 = [chr(i) for i in range(n1, n2)]
    return lst3


@timer
def input_lst_4():  # Сложность O(n^2)
    lst4 = list()
    for x in range(100):
        for i in lst3:
            for j in lst3:
                lst4.append(i + j)
    return lst4


@timer
def input_dct_1(n):  # Сложность O(n)
    dct1 = dict()
    for i in range(n):
        dct1[i] = i
    return dct1


@timer
def input_dct_2():  # Сложность O(1), но общее время зависит от пользовательскаго ввода
    dct2 = {'0': input('0: '), '1': input('1: '), '2': input('2: '), '3': input('3: '), '4': input('4: ')}
    return dct2


@timer
def input_dct_3(n1, n2):  # Сложность O(n)
    dct3 = {i: chr(i) for i in range(n1, n2)}
    return dct3


@timer
def input_dct_4():  # Сложность O(n^2)
    dct4 = dict()
    for x in range(100):
        for i in lst3:
            for j in lst3:
                dct4[str(x)+i+j] = i+j    # len(lst4) == len(dct4) == 9216000
    return dct4


lst1 = input_lst_1(10000000)
dct1 = input_dct_1(10000000)
# lst2 = input_lst_2()
# dct2 = input_dct_2()
lst3 = input_lst_3(32, 128)
dct3 = input_dct_3(32, 128)
lst4 = input_lst_4()
dct4 = input_dct_4()
# print(len(lst4), len(dct4)) # == 9216000, == 9216000
# Время заполнения списка выше, чем у словаря, при сложности O(n), т.к. влияет, в том числе, и то что поиск имени метода
# в экземпляре относительно дорог, например append (несмотря на дешевизну самого метода), по сравнению с алгоритмом
# заполнения словаря.

# Время заполнения словаря выше, чем у списка, при сложности O(n^2), ввиду уже более затратного алгоритма
# заполнения ключей (в том числе рассчет хешей) и значений словаря.


@timer
def lst4_insert(idx, val):    # Сложность O(1)
    lst4.insert(idx, val)
    return


@timer
def dct4_insert(key, val):     # Сложность O(1)
    dct4[key] = val
    return


@timer
def lst4_get(idx):              # Сложность O(1)
    return lst4[idx]


@timer
def lst4_get_index(val):        # Сложность O(n)
    return lst4.index(val)


@timer
def dct4_get(key):              # Сложность O(1)
    return dct4[key]


@timer
def dct4_get2(key):             # Сложность O(1)
    return dct4.get(key)


@timer
def dct4_get_key(val):          # Сложность O(n)
    for k, v in dct4.items():
        if val == v:
            return k


@timer
def lst4_remove(val):           # Сложность O(n)
    lst4.remove(val)
    return


@timer
def lst4_pop(idx):              # Сложность O(1)
    return lst4.pop(idx)


@timer
def dct4_pop(key):              # Сложность O(1)
    return dct4.pop(key)


lst4_insert(900000, 'qwerty')
dct4_insert('100  ', 'qwerty')
lst4_get(900000)
lst4_get_index('qwerty')
dct4_get('100  ')
dct4_get2('100  ')
dct4_get_key('qwerty')
lst4_remove('qwerty')
lst4_pop(900000)
dct4_pop('100  ')
# Время на операции сложности O(1) ничтожно малО. Это операции с добавлением, поиском, удалением элементов по индексу
# (/ключу в словарях) благодаря алгоритму поиска(/хеш-таблицам в словарях).
# Аналогичные операции, по значению, имеют сложность O(n) и время на их выполнение уже наглядно выше. Например,
# поиск индекса по значению в списке или удаление элемента по значению имеют абсолютно идентичную скорость. Ещё
# большую скорость имеет поиск по значению в словаре, в отличие от очень быстрых операций по ключу.
