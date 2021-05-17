"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random

def merge_sort(arr):
    def merge(frst, snd):
        res = []
        x, z = 0, 0
        while x < len(frst) and z < len(snd):
            if frst[x] < snd[z]:
                res.append(frst[x])
                x += 1
            else:
                res.append(snd[z])
                z += 1
        res.extend(frst[x:] if x < len(frst) else snd[z:])
        return res
    def div_half(lst):
        if len(lst) == 1:
            return lst
        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]
        else:
            return merge(div_half(lst[:len(lst)//2]), div_half(lst[len(lst)//2:]))

    return div_half(arr)

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Массив:', array, sep='\n')
print('Он же, но после сортировки:', merge_sort(array), sep='\n')
