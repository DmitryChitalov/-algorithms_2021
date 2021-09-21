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


class DequeClass:

    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)


def pal_checker(string):

    dc_obj = DequeClass()

    for el in string.replace(' ',''):
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


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