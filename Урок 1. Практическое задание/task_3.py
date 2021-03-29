"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

"""
Вариант 1
Используем цикл for 

Сначала мы используем функцию sorted() для упорядочивания значений словаря. 
Затем мы перебираем отсортированные значения, находя ключи для каждого значения. 
Мы добавляем эти пары ключ-значение в отсортированном порядке в новый словарь, если значения совпадают
"""


# Итоговая сложность: 1 + NlogN + 3(N + N(1 + 1)) = 1 + NlogN + 9N
def f_1(p_wrh):
    r_wrh = {}  # O(1)
    # Отбираем три наибольших значения
    sorted_values = sorted(p_wrh.values(), reverse=True)[0:3]  # O(N Log N)

    for i in sorted_values:  # O(3)
        for k in p_wrh.keys():  # O(N)
            if p_wrh[k] == i:  # O(1)
                r_wrh[k] = i  # O(1)
    return r_wrh  # 0


"""
Вариант 2
Используем функцию sorted для словаря

Сначала мы используем функцию sorted() для сортировки элементов по значению ключа. 
Затем мы просто копируем три наибольщих элемента в пустой словарь
"""


# Итоговая сложность: 1 + NlogN + 3 + 3 = 1 + NlogN + 6
def f_2(p_wrh):
    r_wrh = {}  # O(1)
    # Отбираем три наибольших значения
    sorted_keys = sorted(p_wrh, key=p_wrh.get, reverse=True)[0:3]  # O(N Log N)

    for i in sorted_keys:  # O(3)
        r_wrh[i] = p_wrh[i]  # O(1)
    return r_wrh  # 0


# Для хранилища используем словарь
wrh = {'Company 1': 213200, 'Company 2': 1213200, 'Company 3': 200, 'Company 4': 442444, 'Company 5': 99988}
print(f'Исходный словарь: \n{wrh}')

# Тест 1
print(f'Результат для варианта 1: \n{f_1(wrh)}')

# Тест 2
print(f'Результат для варианта 2: \n{f_2(wrh)}')

# Вывод: Вариант 2 более эффективен, т.к. значение итоговой сложности меньше.
