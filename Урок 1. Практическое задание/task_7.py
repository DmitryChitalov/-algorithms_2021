"""
Задание 7.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""

class Deque:

    def __init__(self):
        self.elems = []

    def add_to_head(self, elem):
        self.elems.insert(0,elem)

    def add_to_tail(self, elem):
        self.elems.append(elem)

    def remove_from_head(self):
        return self.elems.pop(0)

    def remove_from_tail(self):
        return self.elems.pop()

    def is_empty(self):
        return self.elems == []

    def get_size(self):
        return len(self.elems)

    def get_elem_from_head(self):
        return self.elems[0]

    def get_elem_from_tail(self):
        return self.elems[-1]


def pal_checker(string):
    dc_obj = Deque()

    string = string.lower()
    words = string.split()
    work_string = ''.join(words)

    for el in work_string:
        dc_obj.add_to_tail(el)

    still_equal = True

    while dc_obj.get_size() > 1 and still_equal:
        first = dc_obj.remove_from_head()
        last = dc_obj.remove_from_tail()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("топот"))
print(pal_checker("молоко делили ледоколом"))
print(pal_checker('АААаа'))
print(pal_checker('АБВгде'))
print(pal_checker('АгА ага'))
