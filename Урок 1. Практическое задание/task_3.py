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

company = {'company_3': 3000, 'company_4': 40, 'company_1': 100, 'company_5': 5, 'company_2': 200}


# №1 O(n)
def variant_1(company):
    top = 3
    lst = []
    for val in company.values():
        lst.append(val)
    lst.sort()

    for el in company:
        for idx in (range(-top, 0)):
            if company[el] == lst[idx]:
                print(el)


# №2 O(N logN)
def variant_2(company):
    new_dict_company = sorted(company.items(), key=lambda x: x[1], reverse=True)
    for i in range(3):
        print(new_dict_company[i][0])


variant_1(company)
variant_2(company)

"""
Решения №1 более эффективно, чем решение №2, так как линейная зависимость - функция,
 которая возрастает медленнее, чем функция N*logN. Соответственно, 2 решение будет отрабатывать дольше.
"""