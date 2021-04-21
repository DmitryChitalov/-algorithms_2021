"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в
виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
from random import randint
from timeit import timeit
from memory_profiler import profile


# итоговая сложность O(n^2)
def rev_buble_sort(list_to_sort):
    i = 1
    while i < len(list_to_sort):
        for j in range(len(list_to_sort) - i):
            if list_to_sort[j] < list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]

        i += 1
    return list_to_sort


# итоговая сложность O(n^2)
def upgrade_rev_buble_sort(list_to_sort):
    i = 1
    counter = 0
    while i < len(list_to_sort):
        for j in range(len(list_to_sort) - i):
            if list_to_sort[j] < list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
                counter += 1
        if not counter:
            break
        else:
            i += 1
    return list_to_sort


@profile
def buble_mem_profile(list_obj):
    rev_buble_sort(list_obj)


@profile
def upgrade_buble_mem_profile(list_obj):
    upgrade_rev_buble_sort(list_obj)


nums = [randint(-100, 99) for _ in range(1000)]
print(f'исходный массив: {nums}')
print(f'отсортированный массив: {rev_buble_sort(nums[:])}')
print(f'еще раз отсортированный массив: {upgrade_rev_buble_sort(nums[:])}\n')

# время - 0.84 с, память - 19.8 MiB
print(f"время выполнения rev_buble_sort: {timeit('rev_buble_sort(nums[:])', number=10, globals=globals())}")
print('занимаемая память:\n')
buble_mem_profile(nums[:])

# время - 0.95 с, память - 19.8 MiB
print(
    f"время выполнения upgrade_rev_buble_sort: {timeit('upgrade_rev_buble_sort(nums[:])', number=10, globals=globals())}")
print(f'занимаемая память:\n')
upgrade_buble_mem_profile(nums[:])

# время - 8.33 с, память - 19.8 MiB
print(f"время выполнения rev_buble_sort: {timeit('rev_buble_sort(nums[:])', number=100, globals=globals())}")
print('занимаемая память:\n')
buble_mem_profile(nums[:])

# время - 9.1 с, память - 19.8 MiB
print(
    f"время выполнения upgrade_rev_buble_sort: {timeit('upgrade_rev_buble_sort(nums[:])', number=100, globals=globals())}")
print(f'занимаемая память:\n')
upgrade_buble_mem_profile(nums[:])

# время - 82.87 с, память - 19.8 MiB
print(f"время выполнения rev_buble_sort: {timeit('rev_buble_sort(nums[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
buble_mem_profile(nums[:])

# время - 93.95 с, память - 19.8 MiB
print(
    f"время выполнения upgrade_rev_buble_sort: {timeit('upgrade_rev_buble_sort(nums[:])', number=1000, globals=globals())}")
print(f'занимаемая память:\n')
upgrade_buble_mem_profile(nums[:])

'''
доработка в плане добавления механизма завершения сортировки в случае, если не было произведено ни одной 
сортировки, не принесла существенных  улучшений. данный механизм ускоряет процесс сортировки в лишь в случае, 
если было необходимо отсортировать уже изначально отсортированный массив чисел. в этом случае работа 
усовершенствованного алгоритма занимала всего 1 проход по входному массиву, в то время как алгоритму без доработки на 
это требовалось len(list_to_sort) проходов. однако если на вход алгоритмов подавать массив, числа в котором 
выбираются случайно из заданного диапазона, то оба алгоритма отрабатывают одинаково. введенное улучшение не дает 
результата, поскольку P{входные данные отсортированы} = 1 / len(list_to_sort)!. 

результаты проведенных замеров показывают, что во всех случаях затрачивается один и тот же объем памяти, это связано с 
тем, что во всех приведенных случаях на вход алгоритмов подаются копии одного и того же массива чисел.

результаты замеров времени показывают, что улучшенная версия алгоритма требует большего времени на выполнение. это 
связано с тем, что в реализации улучшенной версии вводится счтчик counter, а в теле цикла while вводится конструкция 
if else для проверки возможности досрочного завершения сортировки. проверка условия выхода на каждой итерации цикла 
while требует дополнительных временных затрат => в конечном результате upgrade_reb_buble_sort выполняется дольше, 
что становится существенно заметнее при передаче number=1000 в timeit()
'''
