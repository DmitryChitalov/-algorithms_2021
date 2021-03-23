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
        self.element = []

    def is_empty(self):
        return self.element == []

    def add_to_front(self, elem):
        self.element.append(elem)

    def add_to_rear(self, elem):
        self.element.insert(0, elem)

    def remove_from_front(self):
        return self.element.pop()

    def remove_from_rear(self):
        return self.element.pop(0)

    def size(self):
        return len(self.element)


def pal_checker(str_obj):
    dc_obj = DequeClass()

    str_obj = ''.join(str_obj.split())

    for el in str_obj:
        dc_obj.add_to_rear(el)

    still_eq = True

    while dc_obj.size() > 1 and still_eq:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_eq = False

    return still_eq


print(pal_checker('молоко делили ледоколом'))
