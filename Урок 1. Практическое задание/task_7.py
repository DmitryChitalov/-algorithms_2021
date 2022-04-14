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
        self.my_list = []

    def is_empty(self):
        return self.my_list == []

    def add_to_front(self, elem):
        self.my_list.append(elem)

    def add_to_rear(self, elem):
        self.my_list.insert(0, elem)

    def remove_from_front(self):
        return self.my_list.pop()

    def remove_from_rear(self):
        return self.my_list.pop(0)

    def size(self):
        return len(self.my_list)


def pal_checker(string):
    dc_obj = DequeClass()
    new_string = string.replace(' ', '')
    for el in new_string:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("молоко делили ледоколом"))