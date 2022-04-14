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

def num_uniq_substr(s):
    list_str = set()
    for i in range(1, len(s)):
        for j in range(len(s)):
            tmp_str = s[j:j + i]
            list_str.add(hash(tmp_str))

    return len(list_str)

str = input('Введите строку: ')
print('Число уникальных подстрок:', num_uniq_substr(str))


