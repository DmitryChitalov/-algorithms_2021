from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


TEST_COUNT = 1_000
elems = range(100_000)
print("Выполнение функции func_1 занимает:", timeit("func_1(elems)", globals=globals(), number=TEST_COUNT), "сек.")
print("Выполнение функции func_2 занимает:", timeit("func_2(elems)", globals=globals(), number=TEST_COUNT), "сек.")

"""Вывод:
Время выполнения функций №1, №2
Выполнение функции func_1 занимает: 12.7043321 сек.
Выполнение функции func_2 занимает: 11.4336789 сек.
Вторая, модифицированная фунция стала быстрее. В данном случае я использовал
"List comprehension" так как он работает быстрее, при создании списков. 
"""
