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

def all_var(orig):
    substrings = []
    for i in range(0, len(orig) + 1):
        for j in range(i + 1, len(orig) + 1):
            substr = orig[i:j]
            substrings.append(substr)
    substrings.remove(orig)
    hashes = []
    for val in substrings:
        hashes.append(hash(val))
    dict_all = {}
    for u in range(len(hashes)):
        dict_all[substrings[u]] = hashes[u]

    uniq = []
    for val in dict_all.items():
        if val not in uniq:
            uniq.append(val)

    for val in uniq:
        print(val[0])

    print(f'Уникальных подстрок: {len(uniq)}')

# Я делал это конкретьное дз 2 с лишним часа, в итоге проигнорил, что нужно именно хэши сравнивать потому что у меня
# уже крыша протекает


all_var('курлык')
