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


def get_numbs_substrings(s):
    n = len(s)
    hashes = set()
    for i in [s[i:j + 1] for i in range(n) for j in range(i, n)]:
        hashes.add(hash(i))
    return len(hashes)


if __name__ == '__main__':
    print(get_numbs_substrings('papa'))

# Отличие в результате связано с тем, что у меня в коде еще сама строка papa учитывается как подстрока(что верно)
