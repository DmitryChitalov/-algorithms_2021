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

import sys
import json
from random import randint
from pympler import asizeof
from numpy import array


# Урок 4 задание 1 из алгоритмов.
def func_lst(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_gen(nums):
    new_arr = (i for i in range(len(nums)) if nums[i] % 2 == 0)
    return new_arr

lst = list(range(1000))

new_lst = func_lst(lst)
gen = func_gen(lst)

print(f'Memory used by list: {sys.getsizeof(new_lst)} *getsizeof')
print(f'Memory used by generator: {sys.getsizeof(gen)} *getsizeof')

print(f'Memory used by list: {asizeof.asizeof(new_lst)} *asizeof')
print(f'Memory used by generator: {asizeof.asizeof(gen)} *asizeof')
"""
Использование генератора вместо списка явно экономит память (если верить getsizeof)
asizeof показывает другие значения, где генератор явно проигрывает в памяти. На Stackoverflow пишут, что
asizeof пытается собрать более обширные данные, что со сложными объектами не всегда получается.
# """
#---------------------------------------------------------------------------------------------------------------#

# Урок 5 задание 5 из основ, обучался не у вас.
src = [randint(0, 10) for _ in range(1000)]
tmp = set()
res = set()
for el in src:
    if el in tmp:
        res.discard(el)
        continue
    if not el in res:
        res.add(el)
    tmp.add(el)
# print(res)

result = [num for num in src if num in res]
# print(result)
print(f'Memory used by "src" list: {sys.getsizeof(src)} *getsizeof')
print(f'Memory used by "src" list: {asizeof.asizeof(src)} *asizeof')
print(f'Memory used by "result" list: {sys.getsizeof(result)} *getsizeof')
print(f'Memory used by "result" list: {asizeof.asizeof(result)} *asizeof')



src = array([randint(0, 100) for _ in range(1000)])
tmp = set()
res = set()
for el in src:
    if el in tmp:
        res.discard(el)
        continue
    if not el in res:
        res.add(el)
    tmp.add(el)
# print(res)

result = array([num for num in src if num in res])
# print(result)
print(f'Memory used by "src" numpy: {sys.getsizeof(src)} *getsizeof')
print(f'Memory used by "src" numpy: {asizeof.asizeof(src)} *asizeof')
print(f'Memory used by "result" numpy: {sys.getsizeof(result)} *getsizeof')
print(f'Memory used by "result" numpy: {asizeof.asizeof(result)} *asizeof')
"""
numpy для списка src дает явное приемущество по памяти, однако для списка result, наоборот увеличивает память
"""

#---------------------------------------------------------------------------------------------------------------#

# Урок 4 задание 5 из алгоритмов.
def pull_usual_dict():
    usual_dict = {}
    for i in range(10000):
        usual_dict[i] = i
    return usual_dict

usual_dict = pull_usual_dict()

print(f'Memory used by dict: {sys.getsizeof(usual_dict)} *getsizeof')
print(f'Memory used by dict: {asizeof.asizeof(usual_dict)} *asizeof')

dumped_dict = json.dumps(usual_dict)
load_dict = json.loads(dumped_dict)

print(f'Memory used by json-dict: {sys.getsizeof(dumped_dict)} *getsizeof')
print(f'Memory used by json-dict: {asizeof.asizeof(dumped_dict)} *asizeof')

"""
Использовали формат json, чтобы уменьшить затраты памяти, что явно видно при выводе.
"""


