"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.
"""

"""две вложенные O(n) - сложность квадратичная"""
def list_nn(lis):
    for i in lis:
        minim = True
        for x in lis:
            if i > x:
                minim = False
        if minim:
            return i

"""
Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.
"""
""" сложность линейная, потому что вложен один if """
def list_n(lis):
    minim = lis[0]
    for i in lis:
        if i < minim:
            minim = i
    return minim

"""
Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Постарайтесь не использовать ф-ции min() и sort() и другие ф-ции!
Подход должен быть максимально алгоритмическим.
"""
