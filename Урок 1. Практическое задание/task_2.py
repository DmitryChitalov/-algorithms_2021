"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

my_list = [5, 6, 20, 99, 2, 8, 12]


#Сложность: квадратичная
def minimum_1(my_list):
    for i in range(len(my_list)):                                               # О(N) - линейная
        for el in range(len(my_list) - 1):                                      # О(N) - линейная
            if my_list[el] > my_list[el + 1]:                                   # О(1) - константная
                my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]     # О(1) - константная
    return my_list[0]                                                           # О(1) - константная


# Сложность: линейная
def minimum_2(my_list):
    min = my_list[0]        # О(1) - константная
    for el in my_list:      # О(N) - линейная
        if el < min:        # О(1) - константная
            min = el        # О(1) - константная
    return min              # О(1) - константная


print(minimum_1(my_list))
print(minimum_2(my_list))

print(range(len(my_list) - 1))