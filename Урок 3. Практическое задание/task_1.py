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

NUM_COUNT = 1000000 # десять миллионов

def time_measurement(func):
    def timer(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        print(f'Времени затрачено: {time() - start_time}')
        return res
    return timer

@time_measurement
def list_fill(num):
    print('Заполнение списка. ', end='')
    return [i for i in range(num)] # 0.04003596305847168

test_list = list_fill(NUM_COUNT)


@time_measurement
def dict_fill(num):
    print('Заполнение словаря. ', end='')
    return {i: i for i in range(num)} # 0.07506847381591797

test_dict = dict_fill(NUM_COUNT)


@time_measurement
def list_find(num):
    print('Поиск в списке. ', end='') # 0.008007287979125977
    num.index(NUM_COUNT - 1)

list_find(test_list)


@time_measurement
def dict_find(num):
    print('Поиск в словаре. ', end='') # 0.0010008811950683594
    num.get(NUM_COUNT - 1)

dict_find(test_dict)


@time_measurement
def list_pop(my_list):
    print('Метод .pop для списка. ', end='') # 24.326077699661255
    pop_start = NUM_COUNT // 2
    pop_end = NUM_COUNT // 2 + NUM_COUNT // 4
    for i in range (pop_start, pop_end):
        my_list.pop(i)
    return my_list

list_pop(test_list)


@time_measurement
def dict_pop(my_dict):
    print('Метод .pop для словаря. ', end='') # 0.01801609992980957
    pop_start = NUM_COUNT // 2
    pop_end = NUM_COUNT // 2 + NUM_COUNT // 4
    for i in range (pop_start, pop_end):
        my_dict.pop(i)
    return my_dict

dict_pop(test_dict)

# Комментарии:
# Словарь заполняется медленней, т-к попутно генерирует хэш
# Поиск/удаление в словаре намного быстрее, потому что ищет по хэшу,
# а поиск/удаление в списке имеет сложность O(n)
#