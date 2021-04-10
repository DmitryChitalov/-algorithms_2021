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
hash_tab = set()
base_str = input('Введите сткоку >')
hash_tab.add(hash(base_str))
for a in range(len(base_str)):
    sub_str = base_str[a:]
    for b in range(len(sub_str), 0, -1):
        str_hash = hash(sub_str[:b])
        if str_hash not in hash_tab:
            hash_tab.add(str_hash)
            print(f'{sub_str[:b]}')
hash_tab.remove(hash(base_str))
print(f'В строке {base_str} {len(hash_tab)} уникальных подстрок')
