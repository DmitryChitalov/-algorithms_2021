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

# Пытался решить через алгоритм МакКрейта, не получилось :(


def uniq_subsrtring(user_string):
    substrings_set = set()
    max_index = len(user_string)

    for i in range(max_index):
        for j in range(max_index):
            iteration_value_hash = hash(user_string[i:j + 1])
            substrings_set.add(iteration_value_hash)

    substrings_set.remove(hash(''))
    substrings_set.remove(hash(user_string))

    return len(substrings_set)


target_string = 'рара'
print (f'Количество уникальных подстрок в строке "{target_string}": {uniq_subsrtring(target_string)}')
