# Вебинар 12:30
"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
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

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# О памяти и времени при исп-ии  ИТЕРАТОРА и ГЕНЕРАТОРА все прокоментировано в Задание_1_1
# И этот и другой код ПИСАЛ для тренировки. Практики мало!

# Создпние списка случайных чисел.
from random import randint
from memory_profiler import profile
from timeit import timeit

# Применение ИТЕРАТОРА
@profile
def get_random_ints(count, begin, end):
    list_numbers = []
    for x in range(0, count):
        list_numbers.append(randint(begin, end))
    return list_numbers
nums = get_random_ints(10, 0, 1000000)
print(nums)
print(type(get_random_ints))


# Применение ГЕНЕРАТОРА
@profile
def get_random_ints_1(count, begin, end):
    for x in range(0, count):
        yield randint(begin, end)
nums_generator = get_random_ints_1(10, 0, 1000000)
for i in nums_generator:
    print(i)
print(type(nums_generator))

print(f'Время Итератора', timeit("get_random_ints", globals=globals(), number=1000))
print(f'Время Генератора', timeit("get_random_ints_1", globals=globals(), number=1000))

    





