from timeit import timeit
from random import randint, choice
from statistics import median



# Решение методом Тони Хоара
def quickselect_median(list_obj, pivot_fn=choice):
    if len(list_obj) % 2 == 1:
        return quickselect(list_obj, len(list_obj) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(list_obj, len(list_obj) / 2 - 1, pivot_fn) +
                      quickselect(list_obj, len(list_obj) / 2, pivot_fn))

def quickselect(list_obj, k, pivot_fn):
    """
    Выбираем k-тый элемент в списке list_obj (с нулевой базой)
    :param list_obj: список числовых данных
    :param k: индекс
    :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
    :return: k-тый элемент l
    """
    if len(list_obj) == 1:
        assert k != 0
        return list_obj[0]

    pivot = pivot_fn(list_obj)

    lows = [el for el in list_obj if el < pivot]
    highs = [el for el in list_obj if el > pivot]
    pivots = [el for el in list_obj if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # Нам повезло и мы угадали медиану
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)



# Решение без сортировки с помощью вложенного цикла


def find_median(list_obj):
    left_list = []
    right_list = []
    for i in range(len(list_obj)):
        for j in range(len(list_obj)):
            if list_obj[i] > list_obj[j]:
                left_list.append(list_obj[j])
            if list_obj[i] < list_obj[j]:
                right_list.append(list_obj[j])
            if list_obj[i] == list_obj[j] and i > j:
                left_list.append(list_obj[j])
            if list_obj[i] == list_obj[j] and i < j:
                right_list.append(list_obj[j])
        if len(left_list) == len(right_list):
            return list_obj[i]
        left_list.clear()
        right_list.clear()


if __name__ == '__main__':
    m = input('Введите m: ')
    try:
        m = int(m)
    except ValueError:
        print('Вы ввели не число! Исправьтесь.')

    some_list = [randint(0, 50) for i in range(2 * m + 1)]

    print(timeit('find_median(some_list)', globals=globals(), number=10))
    print(timeit('quickselect_median(some_list)', globals=globals(), number=10))
    print(timeit('median(some_list[:])', globals=globals(), number=10))
