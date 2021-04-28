from random import randint

# Задание 2.

"""
Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.
"""


def min_value_N_2(lst_obj):  # O(n^2)
    result = lst_obj[0]  # O(1)
    for i in range(len(lst_obj) - 1):  # O(len(lst_obj)) ==> O(n)
        for j in range(1, len(lst_obj)):  # O(len(lst_obj)) ==> O(n)
            if result > lst_obj[j] < lst_obj[i]:  # O(1)    (Не уверен, мб О(1+1))
                result = lst_obj[j]  # O(1)
    return result  # O(1)


"""
Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.
"""


def min_value_N(lst_obj):  # O(n)
    result = lst_obj[0]  # O(1)
    for i in range(1, len(lst_obj)):  # O(len(lst_obj)) ==> O(n)
        if lst_obj[i] < result:  # O(1)
            result = lst_obj[i]  # O(1)
    return result  # O(1)


# usr_lst = [21, 9, 11, 69, 92, 85, 89, 29, 77, 72]
usr_lst = [randint(1, 100) for elem in range(10)]

print(usr_lst)
print(f'Проверка: {min(usr_lst)}\n'
      f'N^2: {min_value_N_2(usr_lst)}\n'
      f'N: {min_value_N(usr_lst)}')

