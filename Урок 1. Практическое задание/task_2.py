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

# квадратичная сложность
def min_list1(lst):
    min_lst = lst[0]
    for i in lst:
        for j in lst:
            if i < min_lst:
                min_lst = i
    return min_lst

# линейная сложность
def min_list2(lst):
    min_lst = lst[0]        # O(1) - константная
    for i in lst:           # O(n) - линейная
        if i < min_lst:
            min_lst = i     # O(1) - константная
    return min_lst          # O(1) - константная

my_list = [35,18,2,23,105,-8,21]
print(min_list1(my_list))
print(min_list2(my_list))