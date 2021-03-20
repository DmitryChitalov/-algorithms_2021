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

str_val = "zasqr"

substrings = set()
len_str = len(str_val)
count = 0
end_count = len_str - 1
val_bool = True

for i in str_val:
    substrings.add(hash(i))

while count <= len_str - 2:
    if val_bool:
        for i in range(0, end_count):
            if str_val[i:] != "" and str_val[i:] != str_val:
                substrings.add(hash(str_val[i:]))
        val_bool = False
    else:
        for i in range(0, end_count):
            if str_val[count:-i] != "":
                substrings.add(hash(str_val[count - 1:-i]))

    count += 1

print(substrings)
print("{} уникальных подстрок - {}".format(str_val, len(substrings)))
