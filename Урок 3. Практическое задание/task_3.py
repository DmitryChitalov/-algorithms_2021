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



def get_unique_substrings(some_srting):
    return {
        some_srting[start_ind: end_ind] for start_ind in range(len(some_srting)) \
            for end_ind in range(start_ind + 1, len(some_srting) + 1) \
                if len(some_srting) > len(some_srting[start_ind: end_ind])
    }



some_srting = input('Введите строку, состоящию только из строчных латинских букв: ')

print(get_unique_substrings(some_srting))

print(f'Число уникальных подстрок в строке "{some_srting}" = {len(get_unique_substrings(some_srting))}')
