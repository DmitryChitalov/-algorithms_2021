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


def get_substrs(text):
    hashes = {}
    for i in range(len(text)):
        for j in range(len(text), i, -1):
            hash_ = hash(text[i:j])
            if hash_ not in hashes:
                hashes[hash_] = text[i:j]
    del hashes[hash(text)]
    print(f"{text} - {len(hashes)} уникальных подстрок")
    print()
    [print(v) for v in hashes.values()]


if __name__ == '__main__':
    get_substrs('papa')
