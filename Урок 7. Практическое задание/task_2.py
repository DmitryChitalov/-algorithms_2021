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
from mycollectionslib import sdeque
from random import random
from timeit import timeit

CNT_S = [pow(10,i) for i in range(2,6)]

def interunion_sort(l: list):
    if len(l) in (0, 1):
        return l
    L, R = l[:len(l) // 2], l[len(l) // 2:]
    interunion_sort(L)
    interunion_sort(R)
    down = up = result = 0
    C = [0] * (len(L) + len(R))
    while down < len(L) and up < len(R):
        if L[down] <= R[up]:
            C[result] = L[down]
            down += 1
        else:
            C[result] = R[up]
            up += 1
        result += 1
    while down < len(L):
        C[result] = L[down]
        down += 1
        result += 1
    while up < len(R):
        C[result] = R[up]
        up += 1
        result += 1
    for i in range(len(l)):
        l[i] = C[i]
    return l


def interunion_sort1(l: sdeque):
    if len(l) in (0, 1):
        return l
    L, R = l[:len(l) // 2], l[len(l) // 2:]
    L = interunion_sort1(L)
    R = interunion_sort1(R)
    C = sdeque()
    while L and R:
        if L[0:1] <= R[0:1]:
            C.append(L.popleft())
        else:
            C.append(R.popleft())
        pass
    while L:
        C.append(L.popleft())
    while R:
        C.append(R.popleft())
    return C


def standart_sort():
    length = int(input('Введите число элементов: '))
    while length:
        l = [round(random(), 2) * 50 for _ in range(length)]
        print(f'Исходник {l}')
        result = interunion_sort(l[:])
        print(f'Результат {result}')
        length = int(input('Введите число элементов: '))


def sdeque_sort():
    length = int(input('Введите число элементов: '))
    while length:
        l = sdeque([random() * 50 for _ in range(length)])
        print(f'Исходник {l}')
        result = interunion_sort1(l[:])
        print(f'Результат {result}')
        length = int(input('Введите число элементов: '))


if __name__ == '__main__':
    print('Сортировка по алгоритму https://ru.wikipedia.org/wiki/Сортировка_слиянием')
    standart_sort()
    print('Пробуем сделать код лаконичнее, добавляя модифицированный deque -> sdeque (sliced deque)')
    sdeque_sort()

    for tst in CNT_S:
        print(f'Тест для массивов {tst} элементов')
        l = [round(random(), 2) * 50 for _ in range(tst)]
        sl = sdeque(l)
        print(timeit(stmt='interunion_sort(l[:])', globals=globals(), number=1))
        print(timeit(stmt='interunion_sort1(sl[:])', globals=globals(), number=1))

    exit(0)

'''
Тест для массивов 100 элементов
0.0011689379753079265
0.0035460249928291887
Тест для массивов 1000 элементов
0.012742762017296627
0.08576724998420104
Тест для массивов 10000 элементов
0.20679893798660487
0.5751585369871464
Тест для массивов 100000 элементов
2.0012063249887433
6.8903617370233405

Выводы:
1. deque не поддерживает срезы, что затрудняет работу с ним, но его можно доработать,
переписав тип и дополнив его функцией itertools.islice(). Что и сделано в mycollectionslib
2. Модифицированный алгоритм несколько проигрывает по скорости за счет применения связанного списка вместо
массива. Для последовательнослей небольшого размера примерно 1000 элементов вполне себе пригоден.
3. Зато лаконичненько вышло)) Взял на вооружение.  
'''
