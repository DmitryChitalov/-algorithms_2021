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

# 1 O(N Log N)
data = [
    {
        "company": "In Lorem Donec PC",
        "sy": 724294
    },
    {
        "company": "Dolor Tempus Non Limited",
        "sy": 909766
    },
    {
        "company": "Faucibus Leo Inc.",
        "sy": 962101
    },
    {
        "company": "Id Nunc Inc.",
        "sy": 195898
    },
    {
        "company": "Curae; Corp.",
        "sy": 173927
    },
    {
        "company": "Eget Foundation",
        "sy": 138245
    },
    {
        "company": "Est Congue A LLC",
        "sy": 604730
    }
]
s_data = sorted(data, key=lambda i: i['sy'], reverse=True)

print(s_data[0:3])

# 2 O(N Log N)
data2 = [
    [
        "Aliquam Auctor Velit LLP",
        594299
    ],
    [
        "Aliquam Ultrices Iaculis Limited",
        771210
    ],
    [
        "Odio PC",
        386738
    ],
    [
        "Tincidunt Dui Augue Consulting",
        568170
    ],
    [
        "Semper Company",
        419231
    ],
    [
        "Vehicula Aliquet Libero Limited",
        375008
    ],
    [
        "Dictum Ltd",
        270285
    ],
    [
        "Ante Iaculis Nec Incorporated",
        653971
    ],
    [
        "Tincidunt Limited",
        678139
    ],
    [
        "Sit Amet Incorporated",
        779722
    ],
    [
        "Mattis LLC",
        470602
    ]]
s_data = sorted(data2, key=lambda i: i[1], reverse=True)
for i in range(3):
    print(s_data[i]) # O(1)