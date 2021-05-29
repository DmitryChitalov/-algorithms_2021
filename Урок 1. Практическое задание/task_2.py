""" Домашнее задание к уроку №1 курс Алгоритмы и структуры данных на Python
    студент: Максим Сапунов Jenny6199@yandex.ru
    26.05.2021
"""

# Задание 2.

# Реализуйте два алгоритма.
# Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
# В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
# Сложность такого алгоритма: O(n^2) - квадратичная.
# Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
# Сложность такого алгоритма: O(n) - линейная.
# Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
# можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.
# Примечание:
# Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

import random as rd         # необходимо для тестирующей функции.


def get_minimal_value_1(lst_obj: list):
    """ Функция осуществляет поиск минимального значения в полученном списке
    :param lst_obj - список.
    :return: minimal - минимальное значение в списке.
    Сложность алгоритма: N+N**2+1 квадратичная O(N**2)
    """
    lst_copy = lst_obj[:]                                               # Создаю копию списка O(N)
    for i in range(len(lst_copy)):
        for k in range(len(lst_copy)):
            if lst_copy[k] > lst_copy[i]:                               # Сортировка двумя вложенными циклами
                lst_copy[k], lst_copy[i] = lst_copy[i], lst_copy[k]     # O(N**2)
    return lst_copy[0]                                                  # возвращаю минимальное значение O(1)


def get_minimal_value_2(lst_obj: list):
    """ Функция осуществляет поиск минимального значения в полученном списке
    :param lst_obj - список.
    :return: minimal - минимальное значение в списке.
    Сложность алгоритма - линейная O(N).
    """
    minimal = lst_obj[0]                  # O(1)
    for i in range(0, len(lst_obj)):      # O(N)
        if lst_obj[i] < minimal:          # O(1)
            minimal = lst_obj[i]          # 0(1)
    return minimal                        # O(1)


def test_function_minimal():
    """ Тестирующая функция"""
    random_list = [rd.randint(1, 100) for el in range(11)]
    print(random_list, '\n', 'F1 - ', get_minimal_value_2(random_list), 'F2 - ', get_minimal_value_1(random_list))
    if get_minimal_value_2(random_list) == min(random_list):
        print('Функция №1 отработала без ошибок - Ok!')
    else:
        print('Обнаружена ошибка. Проверьте код!')
    if get_minimal_value_1(random_list) == min(random_list):
        print('Функция №2 отработала без ошибок - Ok!')
    else:
        print('Обнаружена ошибка. Проверьте код!')


if __name__ == '__main__':
    test_function_minimal()
