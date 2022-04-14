from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in nums:
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [el for el in range(len(nums)) if nums[el] % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = list(filter(lambda i: nums[i] % 2 == 0, nums))
    return new_arr


def func_4(nums):
    new_arr = [idx for idx, val in enumerate(nums) if val % 2 == 0]
    return new_arr


origin_list = [i for i in range(500)]
print(timeit("func_1(origin_list)", globals=globals(), number=100000))
print(timeit("func_2(origin_list)", globals=globals(), number=100000))
print(timeit("func_3(origin_list)", globals=globals(), number=100000))
print(timeit("func_4(origin_list)", globals=globals(), number=100000))

# Результаты замеров:
# 1) 33.7915688 - Обычный цикл работает медленее всего.
# 2) 28.2240587 - Генератор списков работает быстрее.
# 3) №1 45.2584598 | №2 0.022071799999999087 - Для решения с filter() + lambda разные результаты, в первом случае чтобы
# получить список индексов я применил функцию list(), из-за чего это решение показало самый худший результат, хотя без
# нее результат практически мгновенный, но тогда решение не совсем соответстует затребованному.
# 4) 26.480545000000006 - и быстрее всего отработал генератор списков с применением функции enumerate().

# Выводы: встроенная функция enumerate() замедляет работу меньше всего, затем по сложности range(), и на последнем
# месте list()
