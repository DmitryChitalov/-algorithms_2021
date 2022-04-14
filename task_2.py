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
# Вариант с O(n^2)
lst = [2, 8, 0, 7, -9, 6, 5]
for i in lst:
    mins = True
    for j in lst:
        if i > j:
            mins = False
    if mins:
        print(i)

lst = [2, 8, 0, 7, -9, 6, 5]

# Второй вариант с O(n)
mins = lst[0]
for i in lst:
    if i < mins:
        mins = i

print(mins)