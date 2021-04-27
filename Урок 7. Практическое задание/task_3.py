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
from math import inf


def custom_median_1(array):
    for i in range(len(array) - 1):
        el = array[i]
        l = []
        m = []
        r = []
        for el2 in array:
            if el2 < el:
                l.append(el2)
            elif el2 > el:
                r.append(el2)
            else:
                m.append(el2)
        len_m = len(m)
        if abs((len(l) - len_m) - (len(r) - len_m)) < len_m:
            return el
    return array[len(array) - 1]


def custom_median(array):
    min_el = -inf
    max_el = inf
    i = 0
    while i < len(array):
        el = array[i]
        if (el > min_el) and (el < max_el):
            l = []
            m = []
            r = []
            for el2 in array:
                if el2 < el:
                    l.append(el2)
                elif el2 > el:
                    r.append(el2)
                else:
                    m.append(el2)
            len_l = len(l)
            len_m = len(m)
            len_r = len(r)
            if abs((len_l - len_m) - (len_r - len_m)) < len_m:
                return el
            if len_l - len_r < 0:
                min_el = el
            else:
                max_el = el
        i += 1

    return array[len(array) - 1]


def make_shuffled_odd_array(number=10):
    return [randint(10, 90) for _ in range(2 * number + 1)]


shuffled_odd_array_1 = make_shuffled_odd_array(1)
shuffled_odd_array_10 = make_shuffled_odd_array(10)
shuffled_odd_array_100 = make_shuffled_odd_array(100)
shuffled_odd_array_500 = make_shuffled_odd_array(500)

test_cases = [
    {
        'description': 'at the start',
        'props': [21, 11, 12, 13, 31, 32, 33],
        'result': 21,
    },
    {
        'description': 'at the end',
        'props': [11, 12, 13, 31, 32, 33, 21],
        'result': 21,
    },
    {
        'description': 'in the middle',
        'props': [13, 12, 11, 21, 33, 32, 31],
        'result': 21,
    },
    {
        'description': 'in the middle',
        'props': [41, 19, 40],
        'result': 40,
    },
    {
        'description': 'shuffled_odd_array_1',
        'props': shuffled_odd_array_1,
        'result': median(shuffled_odd_array_1),
    },
    {
        'description': 'shuffled_odd_array_10',
        'props': shuffled_odd_array_10,
        'result': median(shuffled_odd_array_10),
    },
    {
        'description': 'shuffled_odd_array_100',
        'props': shuffled_odd_array_100,
        'result': median(shuffled_odd_array_100),
        'is_detailed': False,
    },
    {
        'description': 'shuffled_odd_array_500',
        'props': shuffled_odd_array_500,
        'result': median(shuffled_odd_array_500),
        'is_detailed': False,
    },
]


def unit_test_fn(fn):
    passed_tests = 0
    print(fn.__name__)
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
        if test_case.get('description'):
            output += f' // {test_case.get("description")}'
        print(output)
    print(f'passed tests: {passed_tests}/{len(test_cases)}\n')


test_fns = [
    median,
    custom_median_1,
    custom_median,
]

for test_fn in test_fns:
    unit_test_fn(test_fn)
