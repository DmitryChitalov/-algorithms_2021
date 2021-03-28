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


def palindrom_check(string):
    string = string.replace(' ', '').lower()

    dc_obj = DequeClass()

    for el in string:
        dc_obj.add_to_rear(el)

    equality = True

    while dc_obj.size() > 1 and equality:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            equality = False

    return equality


if __name__ == '__main__':
    print('Проврека строк на признак палиндрома: ')
    pal_1 = "Молоко делили ледоколом"
    print(pal_1)
    print(palindrom_check(pal_1))
    pal_2 = 'а Роза упала на лапу Азора'
    print(pal_2)
    print(palindrom_check(pal_2))
    pal_3 = 'Просто строка'
    print(pal_3)
    print(palindrom_check(pal_3))
