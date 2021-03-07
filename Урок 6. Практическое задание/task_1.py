"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import memory_usage
from timeit import default_timer
import json

print(f"Память при запуске: {memory_usage()} MiB\n")


def my_dec(func):
    def wrapper(*args, **kwargs):
        mem = memory_usage()
        time = default_timer()
        res = func(*args, **kwargs)
        print(f"Функция {func.__name__}\nВремя: {default_timer() - time}\nПамять: {memory_usage()[0] - mem[0]} MiB\n")
        return res

    return wrapper


@my_dec
def create_lst(num):
    arr = []
    for i in range(num):
        arr.append(i)
    return arr


@my_dec
def create_lst_gen(num):
    return (i for i in range(num))


create_lst(50000)
create_lst_gen(50000)
print(f"Память после первых примеров: {memory_usage()} MiB\n")

"""
Аналитика:
Генератор сильно экономит ресурсы, так как вычисления в нем выполняются только при его вызове.
"""


@my_dec
def convert_data():
    arr = [i for i in range(50000)]
    return [str(i) for i in arr]


@my_dec
def convert_data_map():
    arr = [i for i in range(50000)]
    return map(str, arr)


convert_data()
convert_data_map()

print(f"Память после вторых примеров: {memory_usage()} MiB\n")

"""
Аналитика:
map позволяет значительно снизить затраты ресурсов.
"""


@my_dec
def create_dict():
    return {i: i for i in range(50000)}


@my_dec
def create_dict_json():
    return json.dumps({i: i for i in range(50000)})


create_dict()
create_dict_json()

print(f"Память после третьих примеров: {memory_usage()} MiB")

"""
Аналитика:
JSON является хорошим способом хранения коллекций.
Но стоит помнить, что сериализация также занимает время. 
"""
