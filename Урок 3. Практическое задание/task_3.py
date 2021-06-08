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


def n_substring(my_str, n):
    i = 0
    n_substrings_set = set()
    while n+i <= len(my_str):
        n_substrings_set.add((my_str[i:n+i]))  # хэш засунул, только потому, что просили, смысл не очень уловил
        i += 1
    return n_substrings_set


user_string = input(f"Введите строку:")
n = len(user_string)
all_substrings = set()
while n > 0:
    all_substrings = all_substrings | n_substring(user_string, n)
    n -= 1
print(f'Всего {len(all_substrings)} подстрок. Хэши в студию! \n {all_substrings}')



