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
import random

def time_meter_decorator(fn):
    ''' декоратор времени выполнения функции'''
    def wrap(*args,**kwargs):
        st = time.perf_counter()
        ret = fn(*args,**kwargs)
        run_time = time.perf_counter() - st        
        return ret,run_time
    return wrap

@time_meter_decorator
def fill_list(cnt):
    ''' заполнение списка '''
    lst = [i for i in range(cnt)]
    return lst

@time_meter_decorator
def fill_dict(cnt):
    ''' заполнение словаря '''
    dct = {i:i for i in range(cnt)}
    return dct

@time_meter_decorator
def read_list(test_list,pos):
    '''чтение списка по индексу'''
    return test_list[pos]

@time_meter_decorator
def read_dict(test_dict,pos):
    '''чтение словаря по ключу'''
    return test_dict[pos]

def loop_read(test_list,test_dict,cnt):
    '''цикл чтения из случайной позиции на cnt иттераций'''
    time_counter_list = 0 # суммированное время чтения списка
    time_counter_dict = 0 # суммированное время чтения словаря
    for i in range(cnt):
        pos = random.randrange(0,cnt-1)
        time_counter_list += read_list(test_list,pos)[1]
        time_counter_dict += read_dict(test_dict,pos)[1]

    print(f"List read time: {time_counter_list:0.6f}")
    print(f"Dict read time: {time_counter_dict:0.6f}")


#заполнение
cnt = 100000 # кол-во итераций

print(f"\nВремя заполнения {cnt}  итераций:")

test_list,run_time_lst = fill_list(cnt)
test_dict,run_time_dict = fill_dict(cnt)

print(f"List fill time: {run_time_lst:0.6f}")
print(f"Dict fill time: {run_time_dict:0.6f}")


#чтение 
print(f"\nВремя чтения {cnt} объектов:")
loop_read(test_list,test_dict,cnt)

''' Заполнение Dict() происходит медленнее List()
    на 10000 элементов время заполнения для:
        Dict - 0.002625
        List - 0.000915
    на 1000000:
        Dict - 0.107252
        List - 0.089513
    на 10000000:
        Dict - 1.201959
        List - 0.860441

    Чтение Dict() происходит не на много медленнее List()
    на 10000 элементов время чтения для:
        Dict - 0.074165
        List - 0.060909
    на 1000000:
        Dict - 0.788608
        List - 0.632652
    на 10000000:
        Dict - 9.058141
        List - 7.099228

    Вроде бы словарь должен быть быстрее при чтении т.к. является hash таблицей
    O(n) - поиск в List()
    O(1) - поиск в Dict()
'''
