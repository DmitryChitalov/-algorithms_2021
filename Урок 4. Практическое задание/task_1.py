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

def decor(func):
    def wrapper(*args):
        start_time = timeit.default_timer()
        ret = func(*args)
        print(f'Для {str(func).split(" ")[1]} ожидание составило: {int((timeit.default_timer() - start_time)*1000)} мс.')
        return ret
    return wrapper


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return True


# Оптимизированная нами функция.
def func_2(nums):
    new_arr = []
    # В 2 раза меньше итераций - отсюда и ускорение в 2+ раза. Ускорение линейно - т.е. меняется незначительно
    # от объема данных
    for i in range(0, len(nums), 2):
        new_arr.append(i)
    return True


# Timeit внутри декоратора.
[func([el for el in range(0,19999999)]) for func in (decor(func_1),decor(func_2))]
