from random import uniform
from timeit import timeit

q = int(input("Введите число элементов: "))


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        right = lst_obj[center:]
        left = lst_obj[:center]

        merge_sort(right)
        merge_sort(left)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1

        return lst_obj


real_list = [uniform(1, 50) for _ in range(q)]
print(f"Исходный -        {real_list}")
print(f"Отсортированный - {merge_sort(real_list)}")

print(f'Массив длиной 10: ',
      timeit(
          "merge_sort(real_list[:])",
          globals=globals(),
          number=10000))

real_list = [uniform(1, 50) for _ in range(100)]

print(f'Массив длиной 100: ',
      timeit(
          "merge_sort(real_list[:])",
          globals=globals(),
          number=10000))

real_list = [uniform(1, 50) for _ in range(1000)]

print(f'Массив длиной 1000: ',
      timeit(
          "merge_sort(real_list[:])",
          globals=globals(),
          number=10000))

'''
Введите число элементов: 5
Исходный -        [15.921782660688628, 8.32244309188204, 49.55217330158756, 44.130151667275975, 25.497541515621798]
Отсортированный - [8.32244309188204, 15.921782660688628, 25.497541515621798, 44.130151667275975, 49.55217330158756]
Массив длиной 10:  0.03072140000000001
Массив длиной 100:  1.2960346999999999
Массив длиной 1000:  18.3262722
'''