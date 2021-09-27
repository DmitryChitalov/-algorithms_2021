#!/usr/bin/env python3

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


def substrings(string: str) -> list:
    tmp = set()

    for i in range(len(string)):
        for j in range(len(string)):
            subs = string[i:j + 1]
            if subs not in ['', string]:
                tmp.add((hash(subs), subs))

    return [x[1] for x in tmp]

    # tmp = dict()

    # for i in range(len(string)):
    #     for j in range(len(string)):
    #         subs = string[i:j+1]
    #         if subs not in ['', string]:
    #             tmp[hash(subs)] = subs

    # return tmp.values()

    # return list(set([string [i:j+1] for j in range(len(string)) for i in range(len(string)) if string [i:j+1] != '' and string [i:j+1] != string]))


def main():
    result = substrings('papa')
    print(f'количество различных (уникальных) подстрок: {len(result)}\n{result}')


if __name__ == '__main__':
    main()
