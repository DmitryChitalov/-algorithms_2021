from random import randint
from timeit import timeit

array = [randint(-100, 100) for x in range(100)]


def bubble_sort(lst):
    n = 0

    while n < len(lst):
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


def opt_bubble_sort(lst):
    n = 0

    while n < len(lst):
        end_flag = True
        for i in range(len(lst) - n - 1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                end_flag = False
        if end_flag:
            break
        n += 1
    return lst


if __name__ == '__main__':
    print(f"Исходный массив: \n{array}")
    print(f"Отсортированные массивы:")
    print(bubble_sort(array[:]))
    print(opt_bubble_sort(array[:]))
    print(timeit('bubble_sort(array[:])', globals=globals(), number=10000))
    print(timeit('opt_bubble_sort(array[:])', globals=globals(), number=10000))

    """
    bubble_sort: 21.736
    opt_bubble_sort: 14.944
    Благодаря прерыванию циклу после завершения постановки числа в конец, мы получили оптимизацию по скорости.
    """
