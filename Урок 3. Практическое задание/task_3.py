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
from pprint import pprint

TEST_STRING = 'papa'


def permutation1(s: str, d=dict()) -> dict:
    if len(s):
        # if len(s) != 1:
        d[hash(s)] = s
        return d | permutation1(s[:-1], d) | permutation1(s[1:], d)
    return d


def permutation2(st: str, s=set()) -> set:
    if len(st):
        s.add(hash(st))
        return s | permutation2(st[:-1], s) | permutation2(st[1:], s)
    return s


if __name__ == '__main__':
    res = permutation1(TEST_STRING)
    print(f'Count of unique substring is {len(res.keys())}')
    pprint(res)
    print()
    res = permutation2(TEST_STRING)
    print(f'Count of unique substring is {len(res)}')
    pprint(res)
    exit(0)

'''
выходной словарь включает саму исходную строку, которая частный случай подстроки:

Count of unique substring is 7
{-8947889323220907942: 'apa',
 -4288541607835941840: 'pa',
 1330555953908181415: 'ap',
 2140981377012498533: 'pap',
 3741590063541246851: 'papa',
 4299977071224642671: 'p',
 7226091154185768689: 'a'}

Count of unique substring is 7
{-8947889323220907942,
 -4288541607835941840,
 1330555953908181415,
 2140981377012498533,
 3741590063541246851,
 4299977071224642671,
 7226091154185768689}
 '''
