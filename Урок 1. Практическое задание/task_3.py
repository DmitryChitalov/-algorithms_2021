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

from random import randint

company_name_list = ['ООО Буренушка', 'ООО Главдорстрой', 'ООО ЧебурекиCo', 'ООО Новый день', 'ООО Атаман', 'ООО ТК']


def my_func1(input_list):  # O(N Log N) - линейно-логарифмическая, за счет sorted
    return sorted(input_list, key=lambda input_list: input_list[1], reverse=True)[:3]


def my_func2(input_list):  # 0(12n) - линейная
    top1 = ('', 0)  # O(1) - константная
    top2 = ('', 0)  # O(1) - константная
    top3 = ('', 0)  # O(1) - константная

    for company_dict in input_list:  # O(N) - линейная
        if company_dict[1] > top1[1]:  # O(N) - линейная
            top3 = top2  # O(1) - константная
            top2 = top1  # O(1) - константная
            top1 = company_dict  # O(1) - константная
        elif company_dict[1] > top2[1]:
            top3 = top2  # O(1) - константная
            top2 = company_dict  # O(1) - константная
        elif company_dict[1] > top3[1]:
            top3 = company_dict  # O(1) - константная
        else:
            continue

    return [top1, top2, top3]  # O(3) - константная


def my_func3(input_list): # O(N Log N) - линейно-логарифмическая
    temp_list = []  # 0(1) - константная
    top_list = [None, None, None]  # 0(3) - константная

    for company_dict in input_list:  # 0(N) - линейная
        temp_list.append(company_dict[1])  # 0(1) - константная

    temp_list.sort(reverse=True)  # O(N Log N) - линейно-логарифмическая

    for company_dict in input_list: # 0(N) - линейная
        if company_dict[1] == temp_list[0]:  # 0(1) - константная
            top_list.insert(0, company_dict)  # 0(1) - константная
        elif company_dict[1] == temp_list[1]:  # 0(1) - константная
            top_list.insert(1, company_dict)  # 0(1) - константная
        elif company_dict[1] == temp_list[2]:  # 0(1) - константная
            top_list.insert(2, company_dict)  # 0(1) - константная

    return top_list[:3]  # 0(3) - константная


# Генерация тестовых данных
storage_list = []

for company in company_name_list:
    company_tuple = (company, randint(0, 15000))
    storage_list.append(company_tuple)

top_list = my_func1(storage_list)
print(f'Результат работы первого алгоритма: \n{storage_list} \n{top_list}\n')

top_list = my_func2(storage_list)
print(f'Результат работы третьего алгоритма: \n{storage_list} \n{top_list}\n')

top_list = my_func3(storage_list)
print(f'Результат работы третьего алгоритма: \n{storage_list} \n{top_list}\n')

# Вывод: Второе решение более эффективное, несмотря на то, что код более длинный
