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


def uniqe_substrings() -> str:
    my_string = input("Введите слово или набор латинских букв: ").lower()
    hash_set = set()
    for i in range(len(my_string)):
        for j in range(len(my_string[i:])):
            hash_set.add(hash(my_string[i:j+1]))
            print(f"Включает в  себя: {my_string[i:j+1]}")
    return f"{my_string} - {len(hash_set)-1} уникальных подстрок.\n"


print(uniqe_substrings())
