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
word = input('ведите слово')
len_word = len(word)

set_hash = set()
second_set_hash = set()
for i in range(len_word):
    for a in range(len_word):
        hash_word = hash(word[i:a])
        hash_word_reverse = hash(word[i:a:-1])
        set_hash.add(hash_word)
        set_hash.add(hash_word_reverse)
        for b in set_hash:
            if b:
                second_set_hash.add(b)

print(f'{word} - {len(second_set_hash)} уникальных подстрок.')
