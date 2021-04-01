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
import time
import memory_profiler


def test(func):
    def wrapper(*args):
        m1 = memory_profiler.memory_usage()
        start = time.time()
        result = func(args[0])
        end = time.time()
        m2 = memory_profiler.memory_usage()
        memory = m2[0] - m1[0]
        timer = end - start
        return result, memory, timer

    return wrapper


@test
def get_list(n):
    return [i for i in range(n)]


@test
def get_dict(n):
    return {i: i for i in range(n)}


create_list, mem_list, timer_list = get_list(1000000)
print(f'Создание списка: Память: {"%.2f" % mem_list} Mib, Время:{"%.2f" % timer_list} секунд.')
create_dict, mem_dict, timer_dict = get_dict(1000000)
print(f'Создание словаря: Память: {"%.2f" % mem_dict} Mib, Время: {"%.2f" % timer_dict} секунд.\n')

''' список быстрее заполняется, чем словарь, так как он генерирует хеши для ключей'''


@test
def list_del(a):
    for i in range(1, 100000, 100):
        a.pop(i)


@test
def dict_del(a):
    for i in range(1, 1000000, 100):
        a.pop(i)


del_list, mem_del_list, timer_del_list = list_del(create_list)
print(f'Удаление списка: Память: {"%.2f" % mem_del_list} Mib, Время: {"%.2f" % timer_del_list} секунд.')

del_dict, mem_del_dict, timer_del_dict = dict_del(create_dict)
print(f'Удаление словаря: Память: {"%.2f" % mem_del_dict} Mib, Время: {"%.2f" % timer_del_dict} секунд.')
''' Словарь быстрее удаляет, поиска ключа словаря равна O (1),
 поскольку он реализован в виде таблиц hash. Временная сложность поиска в списке в среднем составляет O(n). '''


@test
def get_list_for(n):
    return [i * i for i in n]


@test
def get_list_map(n):
    return list(map(lambda i: i * i, n))


create_list_for, mem_create_for, timer_create_for = get_list_for(list(range(10000000)))
print(f'Изменение списка через for. Память: {"%.2f" % mem_create_for} Mib, Время: {"%.2f" % timer_create_for} секунд.')

create_list_map, mem_create_map, timer_create_map = get_list_map(list(range(10000000)))
print(f'Изменение списка через map. Память: {"%.2f" % mem_create_map} Mib, Время: {"%.2f" % timer_create_map} секунд.')

'''встроенная функция map, позволяет обрабатывать и преобразовывать без использования явного цикла for
что сокращает время'''
