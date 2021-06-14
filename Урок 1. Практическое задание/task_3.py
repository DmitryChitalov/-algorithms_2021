"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


# 1) придумайте 2-3 решения (не менее двух)
# вариант 1: O(n)
def func_1(dict_x):
    num = 3
    list_x = []
    while num != 0:
        x = 0
        y = None
        for i in dict_x:
            if dict_x[i] > x and i not in list_x:
                x = dict_x[i]
                y = i
        list_x.append(y)
        num -= 1
    return list_x


# вариант 2: O(n)
def func_2(dict_x):
    list_name = []
    list_value = []
    for i in dict_x.items():
        if len(list_name) < 3:
            list_name.append(i[0])
            list_value.append(i[1])
        elif i[1] > min(list_value):
            list_name.append(i[0])
            list_value.append(i[1])
            list_name.remove(list_name[list_value.index(min(list_value))])
            list_value.remove(min(list_value))
    return list_name


# вариант 3:    O(n log n)
def func_3(dict_x):
    list_x = sorted(dict_x, key=dict_x.get, reverse=True)
    return list_x[:3]


dct = {'apple': 10000000, 'samsung': 9000000, 'lg': 1000000, 'google': 8000000, 'honor': 7000000, 'windows': 11000000}
lst = []
print(func_1(dct))
print(func_2(dct))
print(func_3(dct))

# 2) оцените сложность каждого решения в нотации О-большое
# func_1 = O(n), func_2 = O(n), func_3 = O(n log n)

# 3) сделайте вывод, какое решение эффективнее и почему

# Первая функция берёт первую сумму сравнивает её с следующей и сохраняет
# большую итак 3 раза по всему списку

# Вторая берёт 3 первые суммы проходит 1 раз по списку откидывая каждый раз
#  меньшею

# Третья сортирует.

# Если я всё правильно понял с урока то лучше выбрать второй вариант  так как в первой нужно 3 раза пройти по списку.
# Если бы я делал выбор не посмотрев первый урок я бы выбрал третью.
# Жду коментариев правильно ли я сделал выводы. Спасибо!
