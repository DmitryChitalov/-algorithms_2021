"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

# hash?


def sub_str(usr_str):
    sub_str_set_hash = set()
    for i in range(len(usr_str)):
        for j in range(len(usr_str[i:]), i, -1):
            sub_str_set_hash.add(hash(usr_str[i:j]))
        sub_str_set_hash.add(hash(usr_str[i:]))
    sub_str_set_hash.discard(hash(usr_str))
    return len(sub_str_set_hash)


user_str = input("Enter Your string: ")
print(f"String: {user_str}\n"
      f"Sum substring: {sub_str(user_str)}")
