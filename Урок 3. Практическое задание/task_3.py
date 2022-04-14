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


def get_unique_substrings(s):
    unique_substrings = set()
    hash_substrings = set()

    for i in range(len(s) + 1):
        for j in range(i):
            if s[j:i] != s:
                hash_substrings.add(hash(s[j:i]))
                unique_substrings.add(s[j:i])
    print(f'{s} - {len(hash_substrings)} уникальныйх подстрок')
    for item in unique_substrings:
        print(item)
    # print(hash_substrings)


if __name__ == '__main__':
    get_unique_substrings('papa')
