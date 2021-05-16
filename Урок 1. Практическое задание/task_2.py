"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import random
import time

N = 10  # длина списка


def search_min_n2(ls: list):
    """Функция поиска минимального значения для списка.
    В основе алгоритма сравнение каждого числа со всеми другими элементами списка.

    Сложность: O(n**2)
    """
    min_el = ls[0]                                # O(1)
    for element in ls:                            # O(n)
        index = True                              # O(1)
        for compare_element in ls:                # O(n)
            if compare_element < element:
                index = False                     # O(1)
        if index:                                 # O(1)
            min_el = element                      # O(1)
    return min_el                                 # O(1)


def search_min_n(ls: list):
    """Функция поиска минимального значения для списка.

    Сложность: O(n)
    """
    min_el = ls[0]                                # O(1)
    for element in ls:                            # O(n)
        if element < min_el:                      # O(1)
            min_el = element                      # O(1)
    return min_el                                 # O(1)


my_list = []  # задаем список
for i in range(N):
    my_list.append(random.randint(0, 100))
print(my_list)

start_time = time.time()
for i in range(1000000):
    search_min_n2(my_list)
print(f"Время, затраченное на выполение поиска первой функцией: {time.time() - start_time}\n Результат поиска: {search_min_n2(my_list)}")

start_time = time.time()
for i in range(1000000):
    search_min_n(my_list)
print(f"Время, затраченное на выполение поиска второй функцией: {time.time() - start_time}\n Результат поиска: {search_min_n(my_list)}")


