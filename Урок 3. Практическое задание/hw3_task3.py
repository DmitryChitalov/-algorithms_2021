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

import hashlib

class CombinatoricWord():
    def input_word(current_word):
        self.current_word = current_word
        self.set_of_strings = set()

    def get_strings(self)
        for i in range(len(self.current_word)):
            for j in range(i + 1, len(self.current_word) + 1):
                if self.current_word[i:j] != self.current_word:
                	self.set_of_strings.add(hashlib.sha256(self.current_word[i:j].encode()).hexdigest())
                	print self.set_of_strings[i:j]
        print(f'Всего во множестве: {len(self.set_of_strings)} элементов ')



new_combination = CombinatoricWord()
new_combination.input_word('mama')
new_combination.get_strings()

