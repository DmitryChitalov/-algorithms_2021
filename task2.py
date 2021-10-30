"""Определямем случайны спискок"""
lst = [11, 200, 3, 7, 9, 2, 4, 9, 7, 4, 6, 1]

"""Предположим, что минимальное значение идет первым в списке, сложность всего выражения О(n^2)"""
for el in range(len(lst)):
    lowest = el

    """"Отсортируем список"""

    for j in range(el+1, len(lst)):
        if lst[j] < lst[lowest]:
            lowest = j
        lst[el], lst[lowest] = lst[lowest], lst[el]


print(f'Minimum value in the list: {lst[0]}')


"""Вариант сортировки сложность О(n)"""


def my_min(value):
    low = value[0]
    for i in value:
        if i < low:
            low = i
    return low


nums = [2, 3, 5, 9, 17, 12, 2, 3]
print(my_min(nums))



