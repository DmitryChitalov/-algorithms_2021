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
import time


def timing(func):
    def new_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print({time.time() - start})
        return result

    return new_func


@timing
def new_list():
    my_list = [el for el in range(999999)]


@timing
def update_list():
    z = [el for el in range(999999)]
    f = [el for el in range(999999)]
    z.extend(f)


@timing
def clear_list():
    m = [el for el in range(999999)]
    m.clear()


@timing
def new_dict():
    my_dict = {el: f'{el}' for el in range(999999)}


@timing
def update_dict():
    x = {el: f'{el}' for el in range(999999)}
    y = {el: f'{el}' for el in range(999999)}
    x.update(y)


@timing
def clear_dict():
    n = {el: f'{el}' for el in range(999999)}
    n.clear()


print('Создание списка :')
timing(new_list())
print('Добавление элементов другого списка :')
timing(update_list())
print('Удаление элементов списка :')
timing(clear_list())
print('Создание словаря :')
timing(new_dict())
print('Обновление словаря :')
timing(update_dict())
print('Удаление элементов словаря :')
timing(clear_dict())

'''Cамая долгая операция из приведенных выше это обновление словаря, так как при update проиходит дополнение и перезаписывание 
(если элемент отсутсвует в исходном словаре то он добавиться в него
   Созданеие списка получается самым быстрым действием так как происходит простое добавление в конец списка. 
   В отличии от словаря в списке не происходит подсчёта хэша и затрагивания индексов
   '''
