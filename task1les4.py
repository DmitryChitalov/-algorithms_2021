import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
""" Сложность этой функции О(n) - линейная """


def f2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]
""" Сложность этой функции О(n) - линейная """


""" Первая проверка на диапазоне 100"""
n = [i for i in range(100)]
t1 = timeit.timeit("func_1(n)", globals=globals(),number=100)
t2 = timeit.timeit("f2(n)", globals=globals(),number=100)
print(t1)
print(t2)

""" Вторая проверка на диапазоне 1000"""
n = [i for i in range(1000)]
t1 = timeit.timeit("func_1(n)", globals=globals(),number=1000)
t2 = timeit.timeit("f2(n)", globals=globals(),number=1000)
print(t1)
print(t2)



""" Результаты 2х измерений: 
-------- 1 ----------
0.0013897999999999966
0.0011176999999999992
-------- 2 ----------
0.1141441
0.08709149999999999

Вторая функция работает быстрее первой, так как не тратится лишнее время на создание дополнительных переменных
"""