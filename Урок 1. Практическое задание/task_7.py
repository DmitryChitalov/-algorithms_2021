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

def pal_checker(item):
    class_obj = DequeClass()
    new_item = item.replace(' ', '')
    for el in new_item:
        class_obj.add_to_rear(el)

    is_polydrome = True

    while class_obj.size() > 1 and is_polydrome:
        first = class_obj.remove_from_front()
        last = class_obj.remove_from_rear()
        if first != last:
            is_polydrome = False

    return is_polydrome

print(pal_checker('молоко делили ледоколом'))

