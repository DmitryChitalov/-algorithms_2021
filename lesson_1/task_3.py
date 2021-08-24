"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
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


##############################################################################
def get_companies_with_max_profit_1(companies, cnt):
    """
    найдем компанию с максимальной прибылью, удалим ее из списка
    после этого можно найти следующую компанию с максимальной прибылью и так далее

    Сложность O(n^2)
    """

    local_companies = list(companies)  # создаем локальну копию, чтобы не менять входной объект
    max_profit_companies = []

    for _ in range(cnt):  # O(n)

        max_profit = {'profit': local_companies[0]['profit'], 'company_index': 0}

        for i in range(1, len(local_companies)):  # O(n)
            if local_companies[i]['profit'] > max_profit['profit']:
                max_profit['profit'] = local_companies[i]['profit']
                max_profit['company_index'] = i

        max_profit_companies.append(local_companies.pop(max_profit['company_index']))

    return max_profit_companies


##############################################################################
def get_companies_with_max_profit_2(companies, cnt):
    """
    перебираем элементы массива и сравниваем с другими элементами массива, определяя сортировку
    берем нужное количество элементов срезом

    Сложность O(n^2)
    """

    # инициализация массива, в котором будут храниться компании в отсортированном виде
    companies_weight = []
    for i in range(len(companies)):
        companies_weight.append({})

    for i in range(len(companies)):  # O(n)

        company_weight = 0  # позиция компании в общем рейтинге

        for j in range(len(companies)):  # O(n)

            # обработаем случай равенства
            if companies[i]['profit'] == companies[j]['profit'] and i > j:
                company_weight += 1
            elif companies[i]['profit'] > companies[j]['profit']:
                company_weight += 1

        companies_weight[company_weight] = companies[i]

    return companies_weight[-cnt:]  # O(n)


##############################################################################
def get_companies_with_max_profit_3(companies, cnt):
    """
    цикл в цикле в цикле
    по количеству нужных элементов осуществляем сортировку элементов массива
    и каждый раз берем самый большой элемент

    Сложность O(n^3)
    """

    result = []

    for _ in range(cnt):  # O(n)

        companies_weight = []
        map_index = []

        for i in range(len(companies)):
            companies_weight.append({})
            map_index.append(0)

        for i in range(len(companies)):  # O(n)

            company_weight = 0  # позиция компании в общем рейтинге

            for j in range(len(companies)):  # O(n)

                # обработаем случай равенства
                if companies[i]['profit'] == companies[j]['profit'] and i > j:
                    company_weight += 1
                elif companies[i]['profit'] > companies[j]['profit']:
                    company_weight += 1

            map_index[company_weight] = i
            companies_weight[company_weight] = companies[i]

        result.append(companies_weight[-1])
        companies.pop(map_index[-1])

    return result


##############################################################################
company_list = [
    {'name': 'Company 1', 'profit': 9000},
    {'name': 'Company 2', 'profit': 2000},
    {'name': 'Company 3', 'profit': 3000},
    {'name': 'Company 4', 'profit': 3000},
    {'name': 'Company 5', 'profit': 5000},
    {'name': 'Company 6', 'profit': 5000},
    {'name': 'Company 7', 'profit': 7000},
    {'name': 'Company 8', 'profit': 8000},
    {'name': 'Company 9', 'profit': 8000}
]

print('get_companies_with_max_profit_1: ', get_companies_with_max_profit_1(company_list, 3))
print('get_companies_with_max_profit_2: ', get_companies_with_max_profit_2(company_list, 3))
print('get_companies_with_max_profit_3: ', get_companies_with_max_profit_3(company_list, 3))

# функции get_companies_with_max_profit_2 и get_companies_with_max_profit_2 эффективнее get_companies_with_max_profit_3
# потому что обладают меньшей сложность. Для первой функции сложность O(n^2), для второй - O(n^2), для третьей O(n^3)
