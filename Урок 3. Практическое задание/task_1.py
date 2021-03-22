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


def stopwatch(func):
    def wrapped(quantity):
        start = time.time()
        func(quantity)
        end = time.time()
        print(f'Время выполнения: {end - start}')

    return wrapped


def extract_val(func):
    def wrapped(obj, ind):
        start = time.time()
        list_func = func(obj, ind)
        end = time.time()
        print(f'Время выполнения: {end - start}')

    return wrapped


@stopwatch
def create_list(quantity):
    print('-' * 50)
    print('Создание списка. ')
    func_list = [x ** x for x in range(quantity)]
    return func_list


@stopwatch
def create_dict(quantity):
    print('-' * 50)
    print('Создание словаря. ')
    return {k: v for (k, v) in zip([x * x for x in range(quantity)],
                                   [k ** k for k in range(quantity)])}


@extract_val
def search_list(func_list, ind):
    print('-' * 50)
    print('Поиск в списке по индексу. ')
    return [x ** 2 * func_list[ind] for x in func_list]


@extract_val
def get_dict(gen_dict, key):
    print('-' * 50)
    print('Поиск в списке по ключу с .get ')
    return [x ** 3 * gen_dict.get(key) for x in gen_dict]


@stopwatch
def iter_list(obj):
    print('-' * 50)
    print('Обход списка c вычислением.')
    for i in obj:
        val = i ** 3 * i ** 2
    return val


@stopwatch
def iter_dict(obj):
    print('-' * 50)
    print('Обход словаря по ключам c вычислением.')
    for i in obj:
        val = obj[i] ** 3 * obj[i] ** 2
    return val


@extract_val
def in_iter(obj, ind):
    print('-' * 50)
    print('Проверка на вхождение.')
    if ind in obj:
        print(True)
    else:
        print(False)


# Контрольные коллекции
task_list = [x for x in range(5000)]
task_dict = {k: v for (k, v) in zip([x for x in range(5000)],
                                    [k for k in range(5000)])}
while True:
    print('=' * 50)
    act = input('Для выхода введите       => 0\n'
                'Создание коллекций       => 1\n'
                'Поиск по индексу (ключу) => 2\n'
                'Обход коллекции          => 3\n'
                'Проверка на вхождение    => 4\n'
                '-----------------------------\n'
                'Введите значение: ')

    if act == '0':
        break
    elif act == '1':
        create_list(5000)
        create_dict(5000)
        continue
    elif act == '2':
        search_list(task_list, 4000)
        get_dict(task_dict, 4000)
        continue
    elif act == '3':
        iter_list(task_list)
        iter_dict(task_dict)
        continue
    elif act == '4':
        in_iter(task_list, 3000)
        in_iter(task_dict, 3000)
        continue

"""
Вывод.
а) Создание словаря происходит медленнее чем создание списка ввиду того, что генератору 
словаря приходится работать с двумя генераторами списков, что увеличивает количество 
операций, и создавать хеш-таблицу ключей.

б) Операции с коллекциями были арифметически усложнены в равных долях
для визуального понимания происходящего и проверены империческим способом:
    1. Проверка поиска по индексу (ключу) показал примерно одинаковые результаты
    с переменным успехом участвующих коллекций, так-как обе операции имеют 
    сложность O(1).
    2. Обход коллекций показал примерно одинаковые результаты с переменным 
    успехом участвующих коллекций. Оба алгоритма имеют сложность O(n). 
    3. Проверка значение на вхождение показывает одинаковые результаты,
    так-как обе операции имеют сложность O(1).

При использовании алгоритмов работы с коллекциями одной сложности, время выполнения операций
практически ОДИНАКОВОЕ.
"""