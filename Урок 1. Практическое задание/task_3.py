"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
"""
# 1 решение

company_dict = {'company_1': 1000,
                'company_2': 2000,
                'company_3': 3000,
                'company_4': 4000,
                'company_5': 5000
                }

# Сложность решения O(3n) Лучше использовать этот, так как 3n < n log n


def search_max(my_company_dict):
    final_list = []
    number_of_key = ''
    max_item = 0
    for elem in range(3):
        for keys, values in my_company_dict.items():  # O(n)
            if values > max_item:
                max_item = values
                number_of_key = keys
        final_list.append(number_of_key)
        final_list.append(max_item)
        my_company_dict.pop(number_of_key, max_item)
        max_item = 0
    return final_list


print(search_max(company_dict))

# 2 решение

# Сложность решения O(n log n)

list_of_company = list(company_dict.items())
list_of_company.sort(key=lambda enum: enum[1], reverse=True)  # O(n log n)


"""
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
