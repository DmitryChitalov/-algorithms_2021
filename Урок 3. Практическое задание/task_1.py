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


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start_val = time.time()
        value = func(*args, **kwargs)
        print(f' *** Время выполнения {func} - {time.time() - start_val} сек.')
        return value
    return wrapper


@benchmark
def get_list(n, f=2):
    return [x * f for x in range(n)]


@benchmark
def get_dict(n, f=1):
    return {x: x * f for x in range(n)}


@benchmark
def get_rand_list_values(_list, n):
    """ Функция получает список, извлекает из него n произвольных элементов и возвращает их в виде нового списка """
    import random
    temp_list = []
    for _ in range(n):
        temp_list.append(_list[random.randint(0, len(_list))])
    return temp_list


@benchmark
def get_rand_dict_values(_dict, n):
    """ Функция получает словарь, извлекает из него n произвольных элементов и возвращает их в виде списка """
    import random
    temp_list = []
    for _ in range(n):
        temp_list.append(_dict.get(random.randint(0, len(_dict))))
    return temp_list


print('\n=== GENERATE COLLECTIONS ===========\n')

my_list_1 = get_list(10000000)
my_list_2 = get_list(20000000, 3.5)
my_list_3 = get_list(30000000, -2)
my_dict_1 = get_dict(10000000)
my_dict_2 = get_dict(20000000, 3.5)
my_dict_3 = get_dict(30000000, -2)

# Для создания славоря требуется больше времени
# т.к. для моделирования связи между ключом и значением создаются хеш-таблицы

print('\n=== GET RANDOM VALUES ===========\n')

print('my_list_1', get_rand_list_values(my_list_1, 1000)[:5])
print('my_list_2', get_rand_list_values(my_list_2, 2055)[:5])
print('my_list_3', get_rand_list_values(my_list_3, 10000)[:5])
print('my_dict_1', get_rand_dict_values(my_dict_1, 1000)[:5])
print('my_dict_2', get_rand_dict_values(my_dict_2, 2055)[:5])
print('my_dict_3', get_rand_dict_values(my_dict_3, 10000)[:5])

# чтение произволных элементов в словаре происходит гораздо быстрее чем в списке, благодаря хеш-таблицам


