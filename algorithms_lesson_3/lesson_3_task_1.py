from time import time

test_dict = {}
test_list = []
n = 10000


def time_decor(func):
    def count(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'execution time for function {func.__name__}'
              f' equals {end - start}')
        return result

    return count


@time_decor
def list_insert(lst, num): # сложность O(N)
    for i in range(num):
        lst.insert(0, i)


list_insert(test_list, n)
print()


@time_decor
def list_append(lst, num): # сложность O(1)
    for i in range(num):
        lst.append(i)


list_append(test_list, n)
print()

'''
execution time for function list_insert equals 0.04999971389770508

execution time for function list_append equals 0.0010008811950683594

Вывод: операция вставки в конец списка выполняется быстрее, чем в начало
'''


@time_decor
def fill_dict(dct, num): # сложность O(1)
    for i in range(num):
        dct[i] = 'val'


fill_dict(test_dict, n)
print()

'''
execution time for function fill_dict equals 0.000995635986328125
Вывод: скорость вставки элемента в словарь примерно равна скорости 
добавления в конец списка
'''


@time_decor
def list_edit(lst):
    for i in range(10000):
        lst.pop(i)
    for i in range(1000):
        lst[i] = lst[i + 1]


list_edit(test_list)
print()


@time_decor
def dict_edit(dct):
    for i in range(10000):
        dct.pop(i)
    for i in range(10000, 20000):
        dct[i] = 'new'


dict_edit(test_dict)
print()

'''
execution time for function list_edit equals 0.04499387741088867
execution time for function dict_edit equals 0.003999948501586914
Вывод: операции изменения словаря происходят быстрее, чем изменения списка 
'''
