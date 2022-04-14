"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""


import random

from timeit import default_timer

import memory_profiler

from recordclass import recordclass


#  Функция декоратор для замера времени и памяти
def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_profiler.memory_usage()
        res = func(*args)
        m2 = memory_profiler.memory_usage()
        mem_result = m2[0] - m1[0]
        time_result = default_timer() - start_time
        # Устанавливаем на тестовом режиме 30 цифр для вывода результатов.
        # После увеличения массива до 1000 - ставим ограничитель на вывод рузельтатов
        return res, mem_result, time_result
    return wrapper


# Создаем массив случафных цифр от -100 до 100
num_lst = list(random.randrange(-100, 101) for el in range(1000))
# Тестово выводим получившийся массив (число цифр - 30) -->
# [44, 58, 58, -77, -28, 86, 75, -43, -100, -56, 42, -2, 82, 2, -17, 60, 47, 78, -11, -73,-24, 2, -81, 60, 87, 18, -32,
# -39, -54, 11]
print(f'Исходный список {num_lst[0:10]}')


# Функция пузырьковой сортировки (с урока)
@decorator
def bubble_sort(lst):
    num_lst = lst.copy()
    n = 1
    while n < len(num_lst):
        for i in range(len(num_lst) - n):
            if num_lst[i] > num_lst[i + 1]:
                num_lst[i], num_lst[i + 1] = num_lst[i + 1], num_lst[i]
        n += 1
    return num_lst


# Функция пузырьковой сортировки с флагом
@decorator
def sort_bubble(num_lst):
    nums = num_lst.copy()
    # Устанавливаем flag в True, чтобы цикл запустился хотя бы один раз
    flag = True
    while flag:
        flag = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем flag в True для следующей итерации
                flag = True
    return nums


# Функция пузырьковой сортировки с флагом и использованием recordclass
@decorator
def sort_bubble_rc(num_lst):
    rc = recordclass('sorted', 'lst')
    nums = rc(num_lst.copy())
    # Устанавливаем flag в True, чтобы цикл запустился хотя бы один раз
    flag = True
    while flag:
        flag = False
        for i in range(len(nums.lst) - 1):
            if nums.lst[i] < nums.lst[i + 1]:
                # Меняем элементы
                nums.lst[i], nums.lst[i + 1] = nums.lst[i + 1], nums.lst[i]
                # Устанавливаем flag в True для следующей итерации
                flag = True
    return nums


# Результаты работы функций
if __name__ == '__main__':

    print(f"{'-' * 20}")
    res, mem_result, time_result = bubble_sort(num_lst)
    print(f"Выполнение bubble_sort(num_lst) заняло {mem_result} Mib и {time_result} секунд.\n Результат работы: {res[:10]}")
    res, mem_result, time_result = sort_bubble(num_lst)
    print(f"Выполнение sort_bubble(num_lst) заняло {mem_result} Mib и {time_result} секунд.\n Результат работы: {res[:10]}")
    res, mem_result, time_result = sort_bubble_rc(num_lst)
    print(f"Выполнение sort_bubble_rc(num_lst) заняло {mem_result} Mib и {time_result} секунд.\n Результат работы: {res.lst[:10]}")


"""
Выполнена функция сортировки (пузырьковая). Произведены замеры.
Исходный список [-13, 46, 70, -1, -52, 56, 21, -6, -100, 54] - всего 1000 элементов.
--------------------
Выполнение bubble_sort(num_lst) заняло 0.0078125 Mib и 0.26422389999999996 секунд.
 Результат работы: [-100, -100, -100, -100, -100, -100, -99, -99, -99, -98]
Выполнение sort_bubble(num_lst) заняло 0.0 Mib и 0.3095112 секунд.
 Результат работы: [100, 100, 100, 99, 99, 99, 99, 99, 99, 99]
Выполнение sort_bubble_rc(num_lst) заняло 0.0234375 Mib и 0.3699968000000001 секунд.
 Результат работы: [100, 100, 100, 99, 99, 99, 99, 99, 99, 99]

Сортировка выполнена. 
Применение флага ведет к освобождению памяти и замедлению времени работы функции.
Использование в функции sort_bubble_rc() recordclass дало увеличение объема используемой памяти и замедление работы 
функции (на 0,5 сек)
Замер произведен на 1000 записей.
Пытался реализовать собственный алгоритм на основе того, что индексы последовательности целых чисел известны - 
получилось совсем долго и много по памяти. Удалил функцию.

Особенностью алгоритмов сортировки должно быть, по возможности, исключение запоминания массивов данных 

Функция с флагом эффективнее с точки зрения использования ресурсов памяти, но медленнее на 8 %.
"""
