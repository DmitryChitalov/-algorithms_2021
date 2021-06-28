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


class DequeClassTest:
    def __init__(self):
        self.elems = []

    # Убрал две незадействованные функции

    def add_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)


def verify(string):
    test_obj = DequeClassTest()

    # Надо убрать пробелы и на всякий случай привести к нижнему регистру
    for element in string.replace(' ', '').lower():
        test_obj.add_rear(element)

    equal = True

    while test_obj.size() > 1 and equal:
        first = test_obj.remove_from_front()
        end = test_obj.remove_from_rear()
        if first != end:
            equal = False

    return equal


print(verify("молоко делили ледоколом"))
