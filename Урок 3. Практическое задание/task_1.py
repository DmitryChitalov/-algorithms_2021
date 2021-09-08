import time

num = 100000


def time_check(action):
    def wrapper(*args):
        start = time.time()
        result = action(*args)
        finish = time.time()
        print(f'Время выполнения: {finish - start}\n')
        return result

    return wrapper


@time_check
def list_new(num):
    result = []
    for item in range(num):
        result.append(item)
    return result


@time_check
def list_new_2(num):
    result = []
    for item in range(num):
        result.insert(0, item)
    return result


@time_check
def dict_new(num):
    result = dict()
    for item in range(num):
        result[item] = item
    return result


print('Cписок: ')
test_list = list_new(num)

print('Cписок_2: ')
test_list_2 = list_new_2(num)

print('Cловарь: ')
test_dict = dict_new(num)

"""
Cписок: 
Время выполнения: 0.017485618591308594
Cписок_2: 
Время выполнения: 1.9108164310455322
Cловарь: 
Время выполнения: 0.010120630264282227

Список с помощью append и словарь заполняются практически одинаково быстро. Заполнение списка с помощью
insert занимает намного больше времени. 
"""


@time_check
def sch_idx(lst, num):
    for item in range(num):
        lst.index(item)
    return lst


print('Ищем индексы по значениям в списке: ')
sch_idx(test_list, num)


"""
Ищем индексы по значениям в списке: 
Время выполнения: 44.28890633583069
Поиск индексов по значениям элементов в словаре происходит очень долго(перебор всех элементов), поэтому если
нужно быстро получить значение какого-либо элемента, лучше использовать словарь (поиск по ключу) -
константная сложность.

"""


@time_check
def del_list():
    for i in range(num):
        del test_list[0]


@time_check
def del_dict():
    for i in range(num):
        del test_dict[i]


print('Cписок: ')
del_list()

print('Словарь: ')
del_dict()


"""
Cписок: 
Время выполнения: 11.95374870300293
Словарь: 
Время выполнения: 0.008268594741821289

Удаление элементов из словаря происходит быстрее, чем из списка. 

"""

