"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import random
import time

def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        res = func(*args, **kwargs)
        end = time.time_ns()
        print(f'[*] Время выполнения функции <{func.__name__}>: {(end -start)} нс.')
        return res
    return wrapper

@benchmark
def fill_dict(range_start, range_end):
    my_dict = {x: random.randint(1, 100) for x in range(range_start, range_end)}
    return my_dict

@benchmark
def fill_list(range_num):
    my_list = [random.randint(1, 100) for i in range(range_num)]
    return my_list

@benchmark
def extend_list(my_list, ext_list):
    my_list.extend(ext_list)
    return my_list

@benchmark
def extend_dict(my_dict, ext_dict):
    my_dict.update(ext_dict)
    return my_dict

@benchmark
def del_from_list(my_list, num):
    print(my_list.pop(num))
    return my_list

@benchmark
def del_from_dict(my_dict, key):
    print(my_dict.pop(key))
    return my_dict


print("Создаем словарь и список")
first_dict = fill_dict(1, 1000000)
first_list = fill_list(1000000)

print("Создаем словарь и список для добавления")
ext_dict = fill_dict(1000001, 2000000)
ext_list = fill_list(1000000)

print("Апдейтим словарь")
first_dict = extend_dict(first_dict, ext_dict)

print("Апдейтим список")
first_list = extend_list(first_list, ext_list)

print("Удаление из словаря/списка элемента с ключом 230/индексом 230")
first_dict = del_from_dict(first_dict, 230)
first_list = del_from_list(first_list, 230)

"""
Добавление в словарь - это вычисление хеша для каждого добавляемого ключа и проверка его наличия в словаре.
Ожидал, что добавление в словарь будет чуть дольше. Но почему то наоборот. 
Не могу объяснить почему. Сложность вроде бы одинаковая.

Апдейт словаря ожидаемо дольше: надо проверять совпадение ключей по хешам и апдейтить в случае совпадения значения.
Апдейт списка: к одному просто прилепили другой без каких-то вычислений
Поиск и удаление элемента в обоих случаях очень быстрый: для словарей по идее должен быть чуть дольше,
но эксперимент этого не показал
---- 
Создаем словарь и список
[*] Время выполнения функции <fill_dict>: 630467300 нс.
[*] Время выполнения функции <fill_list>: 635306400 нс.
Создаем словарь и список для добавления
[*] Время выполнения функции <fill_dict>: 632101300 нс.
[*] Время выполнения функции <fill_list>: 656016100 нс.
Апдейтим словарь
[*] Время выполнения функции <extend_dict>: 31240100 нс.
Апдейтим список
[*] Время выполнения функции <extend_list>: 0 нс.
Удаление из словаря/списка элемента с ключом 230/индексом 230
50
[*] Время выполнения функции <del_from_dict>: 0 нс.
30
[*] Время выполнения функции <del_from_list>: 0 нс.
"""