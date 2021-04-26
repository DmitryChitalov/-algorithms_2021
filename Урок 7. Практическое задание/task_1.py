"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100]. Выведите на экран
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

from random import shuffle
import timeit


def sorted_reverse(array):
    return sorted(array, reverse=True)


def bubble_sort_plain(array):
    array_copy = array[:]
    n = 1
    while n < len(array_copy):
        for i in range(len(array_copy) - n):
            if array_copy[i] < array_copy[i + 1]:
                array_copy[i], array_copy[i + 1] = array_copy[i + 1], array_copy[i]
        n += 1
    return array_copy


def bubble_sort_optimized(array):
    array_copy = array[:]
    n = 1
    while n < len(array_copy):
        is_changed = False
        for i in range(len(array_copy) - n):
            if array_copy[i] < array_copy[i + 1]:
                is_changed = True
                array_copy[i], array_copy[i + 1] = array_copy[i + 1], array_copy[i]
        if not is_changed:
            break
        n += 1
    return array_copy


test_array_names = ['10', '100', '201']
test_fns = [sorted_reverse, bubble_sort_plain, bubble_sort_optimized]

test_array_10 = [10 - i for i in range(10)]
shuffled_test_array_10 = test_array_10[:]
shuffle(shuffled_test_array_10)

test_array_100 = [100 - i for i in range(100)]
shuffled_test_array_100 = test_array_100[:]
shuffle(shuffled_test_array_100)

test_array_201 = [100 - i for i in range(201)]
shuffled_test_array_201 = test_array_201[:]
shuffle(shuffled_test_array_201)

for test_array_name in test_array_names:
    print(f'test_array_{test_array_name}')
    for test_fn in test_fns:
        print(test_fn.__name__)
        print(
            timeit.timeit(
                f'{test_fn.__name__}(shuffled_test_array_{test_array_name}[:])',
                globals=globals(),
                number=1000,
            )
        )
    print()

test_cases = [
    {
        'props': shuffled_test_array_10,
        'result': test_array_10,
    },
    {
        'props': shuffled_test_array_100,
        'result': test_array_100,
    },
    {
        'props': shuffled_test_array_201,
        'result': test_array_201,
    },
]


def unit_test_fn(fn):
    passed_tests = 0
    print(sorted.__name__)
    for test_case in test_cases:
        props = test_case["props"]
        expected_result = test_case["result"]
        is_detailed = test_case.get("is_detailed") != False
        real_result = fn(props)
        is_ok = real_result == expected_result
        if is_ok:
            passed_tests += 1
        output = f'{is_ok} {fn.__name__}'
        if is_detailed:
            output += f'({props}) => {real_result}{(f", but {expected_result} expected", "")[is_ok]}'
        print(output)
    print(f'passed tests: {passed_tests}/{len(test_cases)}\n')


for test_fn in test_fns:
    unit_test_fn(test_fn)

"""
Результаты замеров скорости:
test_array_10
sorted_reverse
0.0006026140000000013
bubble_sort_plain
0.012117010999999997
bubble_sort_optimized
0.011706633000000001

test_array_100
sorted_reverse
0.004201337999999999
bubble_sort_plain
0.67413488
bubble_sort_optimized
0.644094771

test_array_201
sorted_reverse
0.008047460000000006
bubble_sort_plain
2.5250704070000003
bubble_sort_optimized
2.5063744939999997

Самый быстрый - встроенная функция sorted.
Затем идет оптимизированная сортировка пузырьком
(когда нету перестановок во внутреннем цикле - мы выходим из цикла)
Затем идет сортировка пузырьком без оптимизации
"""
