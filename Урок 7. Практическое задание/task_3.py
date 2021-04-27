"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""

from random import randint
from statistics import median


def custom_median(array):
    return array[len(array) % 2]


def make_shuffled_odd_array(number=10):
    return [randint(10, 100) for _ in range(2 * number + 1)]


shuffled_odd_array_1 = make_shuffled_odd_array(1)
shuffled_odd_array_10 = make_shuffled_odd_array(10)
shuffled_odd_array_100 = make_shuffled_odd_array(100)
shuffled_odd_array_500 = make_shuffled_odd_array(500)

test_cases = [
    {
        'props': shuffled_odd_array_1,
        'result': median(shuffled_odd_array_1),
    },
    {
        'props': shuffled_odd_array_10,
        'result': median(shuffled_odd_array_10),
    },
    {
        'props': shuffled_odd_array_100,
        'result': median(shuffled_odd_array_100),
        'is_detailed': False,
    },
    {
        'props': shuffled_odd_array_500,
        'result': median(shuffled_odd_array_500),
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


test_fns = [
    median,
    custom_median,
]

for test_fn in test_fns:
    unit_test_fn(test_fn)
