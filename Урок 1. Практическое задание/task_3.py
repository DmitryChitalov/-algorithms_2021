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

base_company = {
    'Mail.ru Group': 1000,
    'Yandex': 2000,
    'Rambler': 3000,
    'gmail': 1500,
    'google': 2600,
    'Yahoo!': 3700,
    'Bing': 4080,
    'msn': 500
}


# первый вариант - O(N^2)
def sorted_1(company_dict):
    company_lst = [el for el in company_dict.values()]
    company_lst.sort(reverse=True)
    for el in company_lst[:3]:
        for i, j in company_dict.items():
            if j == el:
                print(i, j)


# второй вариант - O(N log N)
list_from_dictionary = list(base_company.items())
list_from_dictionary.sort(key=lambda i: i[1], reverse=True)
for i in range(3):
    print(list_from_dictionary[i][0], ':', list_from_dictionary[i][1])


# третий вариант - O(N)
def three_max(list_input):
    input_max = {}
    list_d = dict(list_input)
    for i in range(3):
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    return input_max


print(three_max(base_company))
sorted_1(base_company)
