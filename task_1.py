"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import random
import timeit


orig_list = [random.randint(-100, 100) for i in range(1000)]
print('исходный массив:', orig_list)

def func_1(orig_list):
    length=len(orig_list)
    for i in range (length-1):
        for j in range (i+1,length):
            if (orig_list[i]<orig_list[j]):
                orig_list[i],orig_list[j]=orig_list[j],orig_list[i]
    return orig_list


def func_2(orig_list):
    count = 0
    length=len(orig_list)
    for i in range (length-1-count):
        for j in range (i+1,length):
            if (orig_list[i]<orig_list[j]):
                orig_list[i],orig_list[j]=orig_list[j],orig_list[i]
        count += 1
    return orig_list


print('1- массив отсортированный:',func_1(orig_list))
print('2- массив отсортированный:',func_2(orig_list))

print('1---  проверка на 100 запусков --', timeit.timeit("func_1(orig_list)",
                    setup="from __main__ import func_1, orig_list", number=100))

print('2---  проверка на 100 запусков --', timeit.timeit("func_2(orig_list)",
                    setup="from __main__ import func_2, orig_list", number=100))

print('1---  проверка на 1000 запусков --', timeit.timeit("func_1(orig_list)",
                    setup="from __main__ import func_1, orig_list", number=1000))

print('2---  проверка на 1000 запусков --', timeit.timeit("func_2(orig_list)",
                    setup="from __main__ import func_2, orig_list", number=1000))

print('1---  проверка на 10000 запусков --', timeit.timeit("func_1(orig_list)",
                    setup="from __main__ import func_1, orig_list", number=10000))

print('2---  проверка на 10000 запусков --', timeit.timeit("func_2(orig_list)",
                    setup="from __main__ import func_2, orig_list", number=10000))

# оптимизация состояло в том, что после первой сортировки минимальный элемент встал в конце
# и его во второй сортировки уже не нужно сравнивать с препоследним элементов и так далее с другими n сортировками
# после каждой сортировки мы отсеиваем последние минимальные элементы, которые уже стоят на своем месте
# по замерам  показывает что второй вариант работает немного быстрее, в случае большой длинны массива это будет эффективно
#1---  проверка на 100 запусков -- 3.3876122
#2---  проверка на 100 запусков -- 3.2740298000000005
#1---  проверка на 1000 запусков -- 32.8036332
#2---  проверка на 1000 запусков -- 36.238001999999994
#1---  проверка на 10000 запусков -- 339.7281729
#2---  проверка на 10000 запусков -- 333.4683127