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


input_str = input("Введите строку: ")
input_len = len(input_str)

unique_substr = set()
unique_substr_len_prev = 0  # для вывода информацию о подстроке

for i in range(input_len):  # Перебираем все варианты
    for j in range(input_len - 1 if i == 0 else input_len, i, -1):  # не должно попасть в результат само входное слово
        unique_substr.add(hash(input_str[i:j]))
        if len(unique_substr) > unique_substr_len_prev:
            print(f'Подстрока "{input_str[i:j]}" уникальна')
            unique_substr_len_prev += 1
        else:
            print(f'Подстрока "{input_str[i:j]}" уже есть в множетве')

print(f"Количество различных подстрок в строке {input_str}:", len(unique_substr))
