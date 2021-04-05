"""
Задание 7.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
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


def checker(line):
    status = True
    dec_1 = DequeClass()
    new_line = ''.join(line.split())
    for item in new_line:
        dec_1.add_to_rear(item)
    while dec_1.size() > 1 and status:
        first = dec_1.remove_from_front()
        last = dec_1.remove_from_rear()
        if first != last:
            status = False
    return status


print(checker('молоко делили ледоколом'))
print(checker('вадим вадик'))
