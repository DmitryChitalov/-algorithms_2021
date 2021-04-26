"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import uniform
import timeit


def insertion_sort(array):
    array_copy = array[:]
    for i in range(len(array_copy) - 1):
        j = i + 1
        while array_copy[j - 1] > array_copy[j] and j > 0:
            array_copy[j - 1], array_copy[j] = array_copy[j], array_copy[j - 1]
            j -= 1
    return array_copy


test_array_names = [
    '10',
    '100',
    '201',
]
test_fns = [
    sorted,
    insertion_sort,
]

test_array_10 = [uniform(0, 50) for _ in range(10)]
shuffled_test_array_10 = test_array_10[:]
test_array_10.sort()

test_array_100 = [uniform(0, 50) for _ in range(100)]
shuffled_test_array_100 = test_array_100[:]
test_array_100.sort()

test_array_201 = [uniform(0, 50) for _ in range(201)]
shuffled_test_array_201 = test_array_201[:]
test_array_201.sort()

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
        'is_detailed': False,
    },
    {
        'props': shuffled_test_array_201,
        'result': test_array_201,
        'is_detailed': False,
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
test_array_10
sorted
0.00038480800000000037
insertion_sort
0.007951375000000004

test_array_100
sorted
0.003227971000000003
insertion_sort
0.516548554

test_array_201
sorted
0.006088834000000043
insertion_sort
2.022988422
"""