"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
import timeit
import random

r_list = [random.randint(-100, 100) for _ in range(10)]
r_list_2 = r_list[:]


def bubble_s(lst_obj):
    r_list_copy = lst_obj[:]
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return f'Исходный массив: {r_list_copy}\nOтсортированный массив: {lst_obj}'


print('Время работы функции без доработки 10, 100 и 1000 повторов:\n')
# замеры 10
print(timeit.timeit("bubble_s(r_list[:])",
                    setup="from __main__ import bubble_s, r_list", number=10))

# замеры 100
print(timeit.timeit("bubble_s(r_list[:])",
                    setup="from __main__ import bubble_s, r_list", number=100))

# замеры 1000
print(timeit.timeit("bubble_s(r_list[:])",
                    setup="from __main__ import bubble_s, r_list", number=1000))


def bubble_s_2(lst_obj):
    r_list_copy = lst_obj[:]
    n = 1
    while n < len(lst_obj):
        number_of_passes = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                number_of_passes += 1
        if number_of_passes == 0:
            break
        n += 1
    return f'Исходный массив: {r_list_copy}\nOтсортированный массив: {lst_obj}'


print('\nВремя работы функции c доработкой 10, 100 и 1000 повторов:\n')
# замеры 10
print(timeit.timeit("bubble_s_2(r_list_2[:])",
                    setup="from __main__ import bubble_s_2, r_list_2", number=10))

# замеры 100
print(timeit.timeit("bubble_s_2(r_list_2[:])",
                    setup="from __main__ import bubble_s_2, r_list_2", number=100))

# замеры 1000
print(timeit.timeit("bubble_s_2(r_list_2[:])",
                    setup="from __main__ import bubble_s_2, r_list_2", number=1000))
print()

if __name__ == "__main__":
    print(bubble_s(r_list))
    print(bubble_s_2(r_list_2))

"""
Время работы функции без доработки 10, 100 и 1000 повторов:
0.00011150000000000049
0.0012706999999999996
0.015437000000000003
Время работы функции c доработкой 10, 100 и 1000 повторов:
0.00010469999999999924
0.0016098999999999974
0.012944999999999998
Исходный массив: [63, -19, -75, 21, 15, 98, -34, 52, -27, -42]
Oтсортированный массив: [98, 63, 52, 21, 15, -19, -27, -34, -42, -75]
Исходный массив: [63, -19, -75, 21, 15, 98, -34, 52, -27, -42]
Oтсортированный массив: [98, 63, 52, 21, 15, -19, -27, -34, -42, -75]
Итогом внесенных изменений явилось незначительное ускорение работы сортировки на 10 и 1000 повторах.
На 100 повторах наблюдаем иную картину, сортировка сработала медленнее. Поэтому особого смысла в оптимизации 
не вижу.
"""
