"""
Задание 7.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)

Примечание:
Вам не нужно писать код с нуля. Вам нужно доработать пример с урока.
"""


class Palindrome:

    def __init__(self, text):
        self.letters = []
        self.add(text)

    def add(self, text):
        self.letters.clear()
        for el in text.replace(' ', ''):
            self.add_front(el)
        print('Added palindrome')

    def add_front(self, item):
        self.letters.append(item)

    def add_behind(self, item):
        self.elems.insert(0, item)

    def remove_front(self):
        return self.letters.pop()

    def remove_behind(self):
        return self.letters.pop(0)

    def check(self):
        while len(self.letters) > 1:
            first = self.remove_front()
            last = self.remove_behind()
            if first != last:
                return False
        return True


if __name__ == '__main__':
    a = Palindrome("молоко делили ледоколом")
    print(a.check())