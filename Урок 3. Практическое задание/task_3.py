"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а


Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
"""

def unic_char(my_str, my_set=set(), my_set2=set()):
    for i in range(len(my_str)):
        for y in range(i, len(my_str)):
            if my_str[i:y + 1] != my_str:
                my_set2.add(my_str[i:y + 1])
                my_set.add(hash(my_str[i:y + 1]))
    for o in my_set2:
        print(o)

    return print(f'Количество уникальных подстрок: {len(my_set)}')


unic_char('papa')