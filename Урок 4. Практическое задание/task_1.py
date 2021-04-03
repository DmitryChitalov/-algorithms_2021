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
import timeit  # импортируем модуль для измерения времени

# доминанта O(n)
def func_1(simple_list):
    new_arr = []                       # O(1)
    for i in range(len(simple_list)):  # O(n)
        if simple_list[i] % 2 == 0:    # O(1)
            new_arr.append(i)          # O(1)
    return new_arr

# вариант решения из примера
def func_2(simple_list):
    return [i for i, el in enumerate(simple_list) if el % 2 == 0]

# функция для подсчета времени
def func_timeit(simple_list):
    time1 = timeit.timeit("func_1(simple_list)", globals=globals(), number=1000)  # передаем в timeit первое решение
    time2 = timeit.timeit("func_2(simple_list)", globals=globals(), number=1000)  # передаем в timeit второе решение
    print(time1)  # выводим результат работы timeit
    print(time2)  # выводим результат работы timeit
    if time1 > time2:  # делаем простую аналитику сравнением результатов
        return "второй вариант решения быстрее на: ", time1 - time2  # передаем результат для вывода в print
    else:
        return "первый вариант решения быстрее на: ", time2 - time1  # передаем результат для вывода в print


simple_list = [el for el in range(100)]  # заполняем простыми числами попорядку
print("simple_list:", simple_list)  # смотрим что получилось
print(func_timeit(simple_list))  # вызываем функцию измерения

simple_list = [el for el in range(1000)]  # заполняем еще простыми числами попорядку
print(func_timeit(simple_list))

simple_list = [el for el in range(10000)]  # и еще раз заполняем простыми числами попорядку
print(func_timeit(simple_list))

simple_list = [el for el in range(100000)]  # deja vu
print(func_timeit(simple_list))
