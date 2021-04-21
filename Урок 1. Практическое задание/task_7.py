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
        self.lst = []

    def is_empty(self):
        return self.lst == []

    def add_to_front(self, elem):
        # Если не пробел + к верхнему регистру
        if elem != ' ':
            self.lst.append(elem.upper())

    def add_to_rear(self, elem):
        # Если не пробел + к верхнему регистру
        if elem != ' ':
            self.lst.insert(0, elem.upper())

    def remove_from_front(self):
        return self.lst.pop()

    def remove_from_rear(self):
        return self.lst.pop(0)

    def size(self):
        return len(self.lst)


def pal_checker(string):
    dc_obj = DequeClass()
    for el in string:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False
            # Добавил break. Если хотя бы одна пара букв не совпала, нет смысла продолжать цикл
            break

    return still_equal


print('Топот: ', pal_checker("Топот"))
print('А роза упала на лапу Азора: ', pal_checker("А роза упала на лапу Азора"))
print('lkjshdf gajkhdlfkjghirjh sakdv : ', pal_checker("lkjshdf gajkhdlfkjghirjh sakdv "))
