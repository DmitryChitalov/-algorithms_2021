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
def get_substrings(string):
    substrings = set()
    for i in range(1, len(string)):
        for j in range(len(string)):
            substring = string[j:j+i]
            print(hash(substring))
            substrings.add(substring)
    return substrings

print(get_substrings('papa'))