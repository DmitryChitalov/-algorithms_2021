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


def split_word(word):
	count_symb_substr = 1
	list_symb_substr = []
	while count_symb_substr < len(word):
		count = 0
		while count < len(word):
			if hash(word[count:count+count_symb_substr]) not in list_symb_substr:
				list_symb_substr.append(hash(word[count:count+count_symb_substr]))
			count += 1
		count_symb_substr += 1
	return list_symb_substr


print(len(split_word(input("Введите слово: "))))