"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная."""

def min_value():
    min_value = int(list_1[0])

    for el in range(int(len(list_1) - 1)):
        if list_1[el] < min_value:
            return min_value


"""
Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.
"""
from random import randint

n = 10
a = [0] * n
for i in range (n):
    a[i] = randint(1,100)
    print (a[i])
print()

minimum = 101
maximum = -1
for i in a:
    if i < minimum:
        minimum = i
print('Mimimum', minimum)


            
"""
Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
