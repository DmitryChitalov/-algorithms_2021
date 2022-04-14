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

# палиндром
from re import sub


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

    for el in sub(r"[\W_]", '', string).lower():
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


print(f"'молоко делили ледоколом' - {pal_checker('молоко делили ледоколом')}")
print("А в Енисее – синева - ", pal_checker('А в Енисее – синева'))
print("А за работу дадут? – Оба раза! - ", pal_checker('А за работу дадут? – Оба раза!'))
print("А к долу лодка - ", pal_checker('А к долу лодка'))
print("А кобыле цена дана, да не целы бока - ", pal_checker('А кобыле цена дана, да не целы бока'))
print('"Ба-бах!" - у уха бабы - ', pal_checker('"Ба-бах!" - у уха бабы'))
print("Двор – доход РОВД - ", pal_checker('Двор – доход РОВД'))
