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

def decor(func):
    def wrapper(*args):
        start_time = time.time()
        ret = func(*args)
        end_time = time.time()
        print(f'Для {str(func).split(" ")[1]} ожидание составило: {end_time - start_time} сек.')
        return ret
    return wrapper


@decor
def fill_dict(d={}, count=11 ** 6 + 1000):  # O(1)
    for i in range(count):
        d[i] = i  # O(1)
    return d


@decor
def fill_list(l=[], count=11 ** 6 + 1000):  # O(1)
    for i in range(count):
        # справедливо будет заполнять пару - ключ, значение. Но это крайне медленно.
        l.append(i)  # O(1)
    return l


@decor
def find_dict(dct, k):  # O(n)
    if k in dct:  # O(n)
        return True
    else:
        return False


@decor
def find_list(lst, k):  # O(n)
    if k in lst:  # O(n)
        return True
    else:
        return False


@decor
def rm_dict(dct, k):
    if dict(dct).pop(k, None) != None:  # O(1)
        return True
    else:
        return False


@decor
def rm_list(lst, k):
    try:
        list(lst).remove(k) # O(n)
        return True
    except:
        return False


@decor
def upd_dict(dct, k, new_k):  # O(1)
    try:
        # Просто пробуем записать новое значение.
        dict(dct)[k] = new_k  # O(1)
        return True
    except:
        return False


@decor
def upd_list(lst, k, new_k):  # O(1)
    try:
        # Ничего не ищем, так будет справедливо, иначе тут будет совсем другая сложность и время выполнения.
        list(lst)[k] = new_k  # O(1)
        return True
    except:
        return False


# Словарь заполняется медленнее - причина в том, что внутри логики заполнения идет хеширование ключей..
d1 = fill_dict()
# Список заполняется быстрее
l1 = fill_list()
# Однако ищется элемент в словаре - очень быстро.
print(f'Элемент словаря найден: {find_dict(d1, 11 ** 6)}')
# В списке же - куда дольше.
print(f'Элемент списка найден: {find_list(l1, 11 ** 6)}')
# Удаление из словаря
print(f'Элемент словаря удален: {rm_dict(d1, 11 ** 6)}')
# Удаление из списка
print(f'Элемент списка удален: {rm_list(d1, 11 ** 6)}')
# Обновление словаря
print(f'Элемент словаря обновлен: {upd_dict(d1, 11 ** 6, 1000)}')
# Обновление списка
print(f'Элемент списка обновлен: {upd_list(d1, 11 ** 6, 1000)}')
'''
     + Для fill_dict ожидание составило: 0.15300822257995605 сек. - словарь заполняется медленнее.
     + Для fill_list ожидание составило: 0.13399720191955566 сек.
     
     + Для find_dict ожидание составило: 0.0 сек. - поиск в словаре быстрее чем в списке.
     + Для find_list ожидание составило: 0.02400064468383789 сек.
     
     - Для rm_dict ожидание составило: 0.06699991226196289 сек. - удаление из словаря медленнее чем из списка.
     !!!!!! Но при этом сложность алгоритма удаления у списка - ВЫШЕ. Почему так?
     - Для rm_list ожидание составило: 0.05000448226928711 сек.
     
     + Для upd_dict ожидание составило: 0.06599783897399902 сек. -- обновление элемента словаря медленнее чем у списка.
     + Для upd_list ожидание составило: 0.030002593994140625 сек.
    
    Строки "+" означают одинаковую сложность.
    Строки "-" означают разную сложность алгоритмов.

'''
