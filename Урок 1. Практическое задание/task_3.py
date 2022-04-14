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

corp = {"ООО Газалмаз": 12009238,
        "Трест Мясосвинрыбторг": 5404300,
        "ООО Пирамидинвест": 3204359132,
        "Росгнетнадзор": 2349632,
        "ООО Космический мусор холдинг": 204845943,
        "ООО Цис-трансконтинентперевозки": 5345506234,
        "ООО Дедлайн брейкинг солюшнз": 2340259258,
        "Капитал спендерс альянс": 958337772,
        "Баббл маркет дотком": 345345886496,
        "ООО ААА": 2359349,
        "ООО ЕЕЕ": 22939503,
        "ИП Шаурмян Вазген Тигранович": 923485,
        "Краш тест моторз": 2943482}

# Первое решение, сложность: O(NlogN)
bestcorp = dict(reversed(sorted(corp.items(), key=lambda x: x[1])[-3:]))

for i in bestcorp.items():
    print(i[0] + ':', i[1])


# Второе решение, сложность: O(N)
corps = list(corp.items())
max = corps[0][1]
num = 0

for j in range(3):
    max = corps[0][1]
    for n in range(len(corps)):
        if corps[n][1] >= max:
            max = corps[n][1]
            num = n
    print(corps[num][0] + ':', corps[num][1])
    corps.remove(corps[num])


'''
Вывод - эффективнее второе решение, сложность меньше
встроенные функции это хорошо, но иногда можно реализовать свой более оптимизированный алгоритм, 
пусть и менее красиво написанный
'''