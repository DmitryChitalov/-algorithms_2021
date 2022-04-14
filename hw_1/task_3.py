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

company_list = {
    'Apple': 100,
    'Amazon': 120,
    'Huawei': 50,
    'nVidia': 30,
    'Microsoft': 60,
    'Google': 40,
    'PetroChina': 160,
}

print('Изначальный список компаний:')
print(company_list)


# первый способ - сортировка словаря:

sorted_company_list = {}
sorted_keys = sorted(company_list, key=company_list.get, reverse=True)  # O(NlogN)
for i in sorted_keys:                                                   # O(n)
    sorted_company_list[i] = company_list[i]                            # O(1)


print('\nСписок первых трех компаний по доходам (первый способ):')
count = 0
for key in sorted_company_list:     # это вывод данных, к алгоритму он не относится
    if count < 3:
        print(f'{key}: {sorted_company_list[key]}')
    count += 1
# итоговый алгоритм имеет сложность O(n)


# второй способ - поиск самой доходной компании и перенос её в новый список (три раза)

company_list_2 = company_list.copy() # чтоб не портить заданный словарь, создадим копию его
profitabliest_company = {}
for i in range(3):                      # O(1)
    max_profit = 0
    max_profit_company_name = ''
    for k, v in company_list_2.items(): # O(n) находим самое большое значение
        if v > max_profit:              # O(1)
            max_profit = v
            max_profit_company_name = k
    profitabliest_company[max_profit_company_name] = max_profit
    del company_list_2[max_profit_company_name]

print('\nСписок первых трех компаний по доходам (второй способ):')
for key in profitabliest_company:
    print(f'{key}: {profitabliest_company[key]}')
# алгоритм формально имеет сложность O(n), но если следовать РЕР-8,
# то вместо for i in range(3): надо писать как for i in range(MAX_NUMBER):
# тогда сложность алгоритма возрастает до O(n^2)



# третий способ - воспользуемся модулем Collections:
from collections import Counter

company_list_3 = company_list.copy() # чтоб не портить заданный словарь, создадим копию его
profitabliest_company = Counter(company_list_3).most_common(3)      # O(1)
print('\nСписок первых трех компаний по доходам (третий способ):')
for i in profitabliest_company:
    print(f'{i[0]}: {i[1]}')

# формально алгоритм имеет сложность O(1), но мы не знаем как реализован метод внутри модуля

# Однако, судя по всему, третий способ - самый лучший
# как с точки зрения алгоритма, так и с точки зрения реализации.



