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
from numpy import array


def profiler(func):
    def wrapper(*args, **kwargs):
        memory = memory_usage()
        time = default_timer()
        result = func(*args, **kwargs)
        print(f'Время - {default_timer() - time} Память - {memory_usage()[0] - memory[0]} MiB')
        return result

    return wrapper


print('Память по умолчанию ', memory_usage())
print('1', '*' * 150)


@profiler
def my_func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profiler
def my_func_2(nums):
    return (i for i in range(len(nums)) if nums[i] % 2 == 0)


a = my_func_1([g for g in range(1000000)])
b = my_func_2([g for g in range(1000000)])
print('Память после выполнения ', memory_usage())
print('Генератор имеет преимущество так как не затрачивает память, но затрачивает больше времени')
print('2', '*' * 150)


@profiler
def array_():
    test_2 = list(el for el in range(1000000))
    return test_2


@profiler
def numpy():
    test_1 = array([el for el in range(1000000)])
    return test_1


f = array_()
e = numpy()

print('Память после выполнения ', memory_usage())
print(
    'Numpy показывает лучший вариант. Создание списка занимает на много больше памяти чем через библиотеку numpy, но при этом немного быстрее')

print('3', '*' * 150)


@profiler
def my_dict():
    return {i: i for i in range(100000)}


@profiler
def json_dict():
    result = {i: i for i in range(100000)}
    result = json.dumps(result)
    return result


c = my_dict()
d = json_dict()

print('Память после выполнения ', memory_usage())
print(
    'При приведении словаря в json наблюдается понижение затрат памяти в несолько раз, при этом дополнительно затрачивается больше времени. Отдам предпочтение в пользу экономии памяти')
