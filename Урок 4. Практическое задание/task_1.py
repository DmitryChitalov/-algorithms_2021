"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается

И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""
import timeit


def func_1(nums):
    # new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            yield i
    #         new_arr.append(i)
    # return new_arr


test_tuple = (5, 3, 4, 5, 7, 8, 13, 16, 19, 20)
print(list(func_1(test_tuple)))
print(timeit.timeit('func_1(test_tuple)', globals=globals(), number=100000))
print(min(timeit.repeat("func_1(test_tuple)", globals=globals(), timer=timeit.default_timer, repeat=5, number=100000)))

""" Теперь функция не возвращает список, а генирирует значение, что означает что код стал эффективнее
с точки зрения памяти, что существенно повлияло на скорость, теперь функция в разы быстрее, примерно в 10 раз по моим 
наблюдениям
"""