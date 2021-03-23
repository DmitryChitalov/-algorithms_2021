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


# Вариант 1 - O(N logN)
def max_profit1(vocabulary):
    list_profit = sorted(list(vocabulary.values()), reverse=True)[:3]  # O(N logN)
    result = {k: v for k, v in vocabulary.items() if v in list_profit}  # O(n)
    for k, v in result.items():
        print(k, v)


# Вариант 2 - O(N logN)
def max_profit2(vocabulary):
    list_profit = [(v, k) for k, v in vocabulary.items()]
    list_profit = sorted(list_profit, reverse=True)[:3] # O(N logN)
    print(list_profit)


# Вариант 3 - O(N logN)
def max_profit3(vocabulary):
    list_profit = [(v, k) for k, v in vocabulary.items()]
    list_profit = sorted(list_profit, reverse=True) # O(N logN)
    for i in range(3):
        print(list_profit[i][1], list_profit[i][0])


# Вариант 4  - O(N logN)
def max_profit4(vocabulary):
    list_profit = sorted(list(vocabulary.values()), reverse=True)[:3]  # O(N logN)
    for k, v in vocabulary.items():  # вся дальнейшая конструкция, наверное O(N), так как вне зависимости от длины второй цикл будет выполняться одно и то же время
        if v in list_profit:
            print(k, v)

repository = {
    'company1': 80000000,
    'company3': 90000000,
    'company2': 90000000,
    'company4': 222000000,
    'company5': 90000000
}

max_profit1(repository)
print()
max_profit2(repository)
print()
max_profit3(repository)
print()
max_profit4(repository)

# Вывод: решения получились очень похожи, сложность у всех примерно одинаковая, но во втором варианте,
# на мой взгляд, действий меньше, поэтому я считаю, что он лучше.
