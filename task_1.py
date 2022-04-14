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

def time_of_function(function):
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        end_time = time.time()
        print(end_time - start_time)
        return res
    return wrapped

@time_of_function
def new_dict(n):
    my_dict = {x: y for x in range(n) for y in range(n)}
    print('заполнение словаря ')
    return my_dict

new_dict(30000)


@time_of_function
def new_list(n):
    my_list = []
    for i in range(1, n):
        my_list.append(i)
    print('заполнение списка ')
    return my_list

new_list(30000)


# время выполнения заполнения ссписка заняло 0.0019989013671875
# время выполнения заполнения словаря заняло 43.213871717453
# выполняется дольше заполнение словаря т.к. помимо значений он еще столько же вставляет ключей


print('-------------------------------------------------')
my_dict = {x: y for x in range(30000) for y in range(30000)}

@time_of_function
def del_dict(my_dict, n):
    del my_dict [n]
    print('удаление из словаря')
    return my_dict

del_dict(my_dict, 1000)

my_list = []
for i in range(1, 30000):
    my_list.append(i)

@time_of_function
def del_list(my_list, n):
    my_list.remove(n)
    print('удаление из списка')
    return i

del_list(my_list, 1000)

# время удаления из списка 0.0
# время удаления из словаря 0.0

print('-------------------------------------------------')

@time_of_function
def add_dict(my_dict, my_dict_key):
    del my_dict[my_dict_key]
    print('добавление в словарь')
    return my_dict

add_dict(my_dict, 9999)


@time_of_function
def add_list(my_list, n):
    my_list.append(n)
    print('добавление в список')
    return my_list

add_list(my_list, 9999)


# #время добавление в список 0.0
# #время добавления в словарь 0.0




print('-------------------------------------------------')

@time_of_function
def find_dict(my_dict, my_dict_values):
    for n in my_dict.values():
        if n == my_dict_values:
            True
    print('поиск в словаре')
    return my_dict

find_dict(my_dict, 5000)


@time_of_function
def find_list(my_list, n):
    for i in my_list:
        if i == n:
            True
    print('поиск в списке')
    return my_list

find_list(my_list, 5000)

# #время поиск в списке 0.007996082305908203
# #время поиск в словаре 0.0010044574737548828
# #поиск в словаре по значению занимает чуть дольше времени чем в списке
