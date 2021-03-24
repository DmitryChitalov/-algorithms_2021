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
from operator import itemgetter


# для первого варианта я использовала метод sorted
def foo_1(repo_list, quantity):
    sorted_list = sorted(repo_list, key=itemgetter(1))  # O(n*log n)
    sorted_list.reverse()  # O(n)
    res_list = []  # O(1)
    for i in range(quantity):  # O(n)
        res_list.append(sorted_list[i])  # O(1)
    return res_list  # O(1)


# для второго варианта я использовала пузырьковую сортировку
def bubble_sort(repo_list, quantity):
    sorting_list = [el for el in repo_list]  # O(n)
    swapped = True  # O(1)
    while swapped:  # O(n)
        swapped = False  # O(1)
        for i in range(len(sorting_list) - 1):  # O(n)
            if sorting_list[i][1] > sorting_list[i + 1][1]:  # O(1)
                sorting_list[i], sorting_list[i + 1] = sorting_list[i + 1], sorting_list[i]  # O(1)
                swapped = True  # O(1)
    sorting_list.reverse()  # O(n)
    counter = 0  # O(1)
    res_list = []  # O(1)
    while counter < quantity:  # O(n)
        res_list.append(sorting_list[counter])  # O(1)
        counter += 1  # O(1)
    return res_list  # O(1)


repository = [('comp1', 1000), ('comp2', 1100), ('comp3', 10000), ('comp4', 2500), ('comp5', 100)]
print(foo_1(repository, 3))
print(bubble_sort(repository, 3))

# Сложность первого алгоритма: O(n*log n)
# Сложность второго алгоритма: O(n^2)

# Вывод: первый алгоритм эффективнее
