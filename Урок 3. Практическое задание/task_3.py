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

user_string = 'papara'  # -> Поскольку выборка делается за один запуск - встренная функция hash() проще и быстрее
new_set = set()
for i in range(len(user_string)):
    for j in range((i + 1), (len(user_string) + 1)):
        if user_string[i:j] != user_string:
            new_set.add(hash(user_string[i:j]))
            # print(user_string[i:j], end=' ')
print()
print(new_set)
print(len(new_set))

user_string = 'papara'  # -> вариант решения без хеша
new_set = set([user_string[i:j] for i in range(len(user_string))
               for j in range(i + 1, len(user_string) + 1) if user_string[i:j] != user_string])
print()
print(new_set)
print(len(new_set))