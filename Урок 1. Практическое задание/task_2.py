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
#O(n)
def func1(list_obj):
    min = list_obj[0]
    for i in range(len(list_obj)):
        if min > list_obj[i]:
            min = list_obj[i]
    return min

#O(n^2)
def func2(list_obj):
    real_min = list_obj[0]
    min = list_obj[0]
    for i in range(len(list_obj)):
        for j in range(len(list_obj)):
            if list_obj[i] < list_obj[j]:
                min = list_obj[j]
        if real_min > min:
            real_min = min
    return real_min

def check_min_2(lst_obj): # O(n^2)
    rez_min_el = lst_obj[0]
    min_el = lst_obj[0]
    for i in range(len(lst_obj)):
        for j in range(len(lst_obj)):
            if lst_obj[i] < lst_obj[j]:
                min_el = lst_obj[j]
        if rez_min_el > min_el:
            rez_min_el = min_el
    return rez_min_el

info = [1, 3, 6, 9]

print(func1(info))
print(func2(info))

