"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from pympler import asizeof
import numpy as np
from memory_profiler import profile


@profile
def func_1():
    src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    result2 = []
    temp_num = 0

    for el in src:
        if not temp_num:
            temp_num = el
            continue
        if temp_num < el:
            result2.append(el)
        temp_num = el

    return f'Список: {asizeof.asizeof(src)}, {asizeof.asizeof(result2)}'


@profile
def func_2():
    src = np.array([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])
    result2 = np.array([])
    temp_num = 0

    for el in src:
        if not temp_num:
            temp_num = el
            continue
        if temp_num < el:
            result2 = np.append(result2, el)
        temp_num = el

    return f'NumPyArray: {asizeof.asizeof(src)}, {asizeof.asizeof(result2)}'


print(func_1())  # Список: 536, 312
print(func_2())  # NumPyArray: 176, 168

# Оптимизация памяти с помощью замены списка на numpy.array
# Снижение затрат памяти в 2-3 раза
# Для просмотра затрат памяти использовался asizeof
# @Profile из memory_profiler не показал изменений затрат памяти по ходу выполнения функции
