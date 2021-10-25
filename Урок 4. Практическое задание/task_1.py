"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]    # массив
number_cycles = 1000000    # количество операций


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def test_lst_comp(nums):
    # enumerate - сработает как счётчик. i индекс, numb - принимает значение
    return [i for i, numb in enumerate(nums) if numb % 2 == 0]    # всё сокращено до одной строки


print(timeit("func_1(number_list)", globals=globals(), number=number_cycles),
      '\n', func_1(number_list))
print(timeit("test_lst_comp(number_list)", globals=globals(), number=number_cycles),
      '\n', test_lst_comp(number_list))

"""test_lst_comp сработает быстрее, так как упрощено (одна строка) и
использован метод enumerate: генерирует значения и индексы элементов в итерируемом объекте
(i - примет индекс, numb - принимает значение элемента).
данные из интернета и книги Лутц М. "Изучаем Python",
разница примерно 10% (в зависимости от железа и других факторов)"""
