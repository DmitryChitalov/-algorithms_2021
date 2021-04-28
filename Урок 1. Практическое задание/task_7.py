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


def pal_checker(string):  # O(n)
    tmp = DequeClass()  # O(1)

    for el in string:  # O(n)
        if not el.isspace():  # O(1)
            tmp.add_to_rear(el)  # O(1)
    equal = True  # O(1)

    while tmp.size() > 1 and equal:  # O(n)
        first = tmp.remove_from_front()  # O(1)
        last = tmp.remove_from_rear()  # O(1)
        if first != last:  # O(1)
            equal = False  # O(1)
    return equal  # O(1)


print(pal_checker("молоко делили ледоколом"))   # True
print(pal_checker("топот"))   # True
print(pal_checker("Жесть"))   # False
