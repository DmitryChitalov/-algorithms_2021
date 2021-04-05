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

# Эффективнее решение 1, т.к. в нем осуществляется меньшее количество действий, поэтому
# оно должно отрабатывать быстрее (по времени)

def find_companies_names(companies_repo):
    # Сложность: O(N) + O(NlogN) + O(N**2) + O(1) = O(N**2)

    profit = [value for value in companies_repo.values()]   # O(N)

    profit.sort()                                           # O(NlogN) - из таблицы
    max_profit = profit[-3:]                                # O(1) - берем 3 последних элемента

    right_companies = []                                    # O(1) - присвоение
    for name, value in companies_repo.items():              # O(N) - цикл по всем кортежам, полученным из словаря
        if value in max_profit:                             # O(N) - необходимо произвести сравнение значения со свеми
                                                            # элементами списка
            right_companies.append(name)                    # O(1) - добавление в конец списка

    return right_companies                                  # O(1) - возврат из функции


def find_companies_names_with_max_profit(companies_repo):
    # Сложность: O(N) + O(1) + O(N**2) + O(N) = O(N**2)

    profit = [value for value in companies_repo.values()]    # O(N)

    max_profit = []                                          # O(1)
    for i in range(3):                                       # O(3)
        max_value = max(profit)                              # присвоение О(1), мах - О(N)??
        max_profit.append(max_value)                         # O(1) - добавление в конец списка
        profit.remove(max_value)                             # O(N) - нужно сравнитьтребуемое значение с каждым
                                                             # элементом списка

    names = []                                               # O(1)
    values = []                                              # O(1)
    for key in companies_repo.keys():                        # O(N)
        if companies_repo[key] in max_profit:                # O(N)
            names.append(key)                                # O(1)
            values.append(companies_repo[key])               # O(1)
    
    right_storage = {names[i]:values[i] for i in range(len(names))} # O(N)
    return right_storage                                     # O(1)

storage = {'mvideo': 100, 'hp': 100000000, 'asus': 65346578658762, 'eldorado': 54732, 'lenovo': 0,
             'samsung': 6746218643}

print(f'компании с максимальной прибылью: {", ".join(find_companies_names(storage))}')
print(f'новое хранилище с данными о компаниях: {find_companies_names_with_max_profit(storage)}')