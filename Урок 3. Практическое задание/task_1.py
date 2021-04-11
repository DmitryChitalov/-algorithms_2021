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
    my_lst = [el for el in range(999999)]


@timing
def new_dict():
    my_dct = {el: f'{el}' for el in range(999999)}


@timing
def update_list():
    lst_1 = [el for el in range(999999)]
    lst_2 = [el for el in range(999999)]
    lst_1.extend(lst_2)


@timing
def update_dict():
    dct_1 = {el: f'{el}' for el in range(999999)}
    dct_2 = {el: f'{el}' for el in range(999999)}
    dct_1.update(dct_2)

@timing
def clear_list():
    lst_3 = [el for el in range(999999)]
    lst_3.clear()


@timing
def clear_dict():
    dct_3 = {el: f'{el}' for el in range(999999)}
    dct_3.clear()


print('Создание списка : ')
timing(new_list())
print('Создание словаря :')
timing(new_dict())
print('Добавление элементов другого списка :')
timing(update_list())
print('Добавление элементов другого словаря :')
timing(update_dict())
print('Удаление элементов списка :')
timing(clear_list())
print('Удаление элементов словаря :')
timing(clear_dict())

'''
Создание  списка быстрее, т.к. элементы просто добавляются в конец списка и не надо вычислять хеши ключей. 

Обновление списка быстрее, чем словаря.
'''
