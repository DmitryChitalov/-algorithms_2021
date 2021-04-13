"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

# hash?


def unique_substr(str_obj):
    substr_list = set()
    for i in range(1, len(str_obj)):
        for j in range(0, len(str_obj)):
            el = str_obj[j:j+i]
            substr_list.add(hash(el.encode('utf-8')))
    return len(substr_list)


my_str = 'papa'
print(unique_substr(my_str))
