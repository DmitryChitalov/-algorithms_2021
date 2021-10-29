"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import uniform
from timeit import timeit

n = int(input('Введите число элементов: '))
not_sorted_list = [uniform(0, 50) for i in range(n)]
not_sorted_list_10 = [uniform(0, 50) for i in range(10)]
not_sorted_list_100 = [uniform(0, 50) for i in range(100)]
not_sorted_list_1000 = [uniform(0, 50) for i in range(1000)]

# взял сортировку слиянием с википедии
def merge_sort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    L, R = A[:len(A) // 2], A[len(A) // 2:]
    merge_sort(L)
    merge_sort(R)
    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    for i in range(len(A)):
        A[i] = C[i]
    return A

print(f'Исходный - {not_sorted_list}')
print(f'Отсортированный - {merge_sort(not_sorted_list)}')
print(
    timeit("merge_sort(not_sorted_list_10)", globals=globals(), number=10),
    timeit("merge_sort(not_sorted_list_100)", globals=globals(), number=10),
    timeit("merge_sort(not_sorted_list_1000)", globals=globals(), number=10), sep='\n'
)

"""
Скорости соответственно:
0.00045634400157723576
0.00517852499615401
0.04191398699185811
"""