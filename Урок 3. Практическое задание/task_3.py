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

# import hashlib
#
# user_string = 'papara'
# new_set = set()
# for i in range(len(user_string)):
#     for j in range((i + 1), (len(user_string) + 1)):
#         if user_string[i:j] != user_string:
#             new_set.add(hashlib.sha256(user_string[i:j].encode()).hexdigest())
#             print(user_string[i:j], end=' ')
# print()
# print(new_set)
# print(len(new_set))
#
# user_string = 'papara'  # -> Без хеша тоже нормально делает выборку
# new_list = []
# for i in range(len(user_string)):
#     for j in range((i + 1), (len(user_string) + 1)):
#         if user_string[i:j] not in new_list:
#             if user_string[i:j] != user_string:
#                 new_list.append(user_string[i:j])  # (hashlib.sha256(user_string[i:j].encode()).hexdigest())
#                 print(user_string[i:j], end=' ')
# print()
# print(new_list)
# print(len(new_list))
#
# user_string = 'papara'  # -> Поскольку выборка делается за один запуск - встренная функция hash() проще и быстрее
# new_set = set()
# for i in range(len(user_string)):
#     for j in range((i + 1), (len(user_string) + 1)):
#         if user_string[i:j] != user_string:
#             new_set.add(hash(user_string[i:j]))
#             print(user_string[i:j], end=' ')
# print()
# print(new_set)
# print(len(new_set))
#
# user_string = 'papara'  # -> 2й вариант решения без хеша тоже нормально делает выборку
# new_set = set([user_string[i:j] for i in range(len(user_string))
#                for j in range(i + 1, len(user_string) + 1) if user_string[i:j] != user_string])
# print()
# print(new_set)
# print(len(new_set))