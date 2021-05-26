"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
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


def maxprofit_1(storage):  # O(n log n)
    sorted_dict = {}
    sorted_keys = sorted(storage, key=storage.get)  # O(n log n)

    for el in sorted_keys[-3:]:  # O(n)
        sorted_dict[el] = storage[el]  # O(1)
    for el, value in sorted_dict.items():  # O(n)
        print(el, value)  # O(1)


def maxprofit_2(dict):
    third = first = second = 0  # O(1)
    first_name = second_name = third_name = ''  # O(1)
    for el, value in dict.items():  # O(n)
        if value > first:  # O(1)
            third = second  # O(1)
            third_name = second_name  # O(1)
            second = first  # O(1)
            second_name = first_name  # O(1)
            first = value  # O(1)
            first_name = el  # O(1)
        elif value > second:  # O(1)
            third = second  # O(1)
            third_name = second_name  # O(1)
            second = value  # O(1)
            second_name = el  # O(1)
        elif value > third:  # O(1)
            third = value  # O(1)
            third_name = el  # O(1)

    print(f'{first_name}: {first}\n{second_name}: {second}\n{third_name}: {third}')


storage = {
    'Company_name_1': 223344,
    'Company_name_2': 46782,
    'Company_name_3': 12345,
    'Company_name_4': 12345,
    'Company_name_5': 313337
}

print(f'Data company')
for key, value in storage.items():
    print(key, value)
print(f'\nFunction best 3 O(n log n)')
maxprofit_1(storage)
print(f'\nFunction best 3 O(n)')
maxprofit_2(storage)

"""
В функции maxprofit_1 код смотрится на порядок понятней и проще 
+ если нужно будет его масштабировать как вариант чтобы найти не 3, а 4 компании и прочее, 
то достаточно поменять значение одной переменной. 
В варианте же с функцией maxprofit_2 масштабируемость будет целой проблемой,
так как нужно будет вводить целую пачку доп переменный, но зато этот вариант позволяет
всего лишь один раз пробежаться по словарику и дело сделано. 

По Big O notation maxprofit_2 получается лучше, но вот если чтото нужно будет поменять
то maxprofit_1 понятнее и гибкий.
"""
