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
def min_bad(in_lst): # Сложность O(N^2)
    new_lst = list(in_lst)
    n = len(new_lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if new_lst[j] > new_lst[j+1] :
                new_lst[j], new_lst[j+1] = new_lst[j+1], new_lst[j]
    return  new_lst[0]


def min_better(in_lst): # Сложность O(N)
    min = in_lst[0]
    for i in in_lst:
        if i < min:
            min = i
    return  min
