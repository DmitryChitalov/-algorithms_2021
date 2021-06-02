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
"""


def uniq_substring(usr_str):
    substring_set = set()
    for i in range(1, len(usr_str)):
        for j in range(len(usr_str)):
            temp_str = usr_str[j:j + i]
            substring_set.add(hash(temp_str))

    return len(substring_set)


user_answer = input('Введите строку: ')
print(f'Число уникальных подстрок: {uniq_substring(user_answer)}')
