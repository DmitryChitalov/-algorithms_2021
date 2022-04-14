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

Постарайтесь не использовать ф-ции min() и sort() и другие ф-ции!
Подход должен быть максимально алгоритмическим.
"""


def find_min_1(lst_obj):
    """Функция должная вернуть минимальное значение из списка.

       Алгоритм 1:
       Выбираем по порядку каждый элемент списка и сравниваем поочередно с каждым элементом списка

       Сложность: O(n^2)
       """

    min_num = lst_obj[0]                   # O(1)
    for el in lst_obj:                     # O(n)
        for i in lst_obj:                  # O(n)
            if el < i and el < min_num:    # O(1)
                min_num = el               # O(1)
    return min_num                         # O(1)


def find_min_2(lst_obj):
    """Функция должная вернуть минимальное значение из списка.

    Алгоритм 1:
    Присваиваем переменной min_num первое значение списка, а затем сравниваем с каждым последующим элементом списка,
    если находится меньшее значение, то оно присваивается переменной min_num

    Сложность: O(n)
    """

    min_num = lst_obj[0]      # O(1)
    for el in lst_obj[1:]:    # O(n)
        if el < min_num:      # O(1)
            min_num = el      # O(1)
    return min_num            # O(1)


a = [1, 5, 8, -3, 6, 0, 5]
print(find_min_1(a))
print(find_min_2(a))
