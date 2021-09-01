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
    """Класс палиндром"""

    def __init__(self):
        self.elems = []

    def is_empty(self):
        """Проверка на пустоту экземпляра"""
        return self.elems == []

    def add_to_rear(self, elem):
        """Добавление элемента в конец"""
        self.elems.append(elem)

    def add_to_front(self, elem):
        """Добавление элемента в начало"""
        self.elems.insert(0, elem)

    def remove_from_rear(self):
        """Удаление элемента из конца"""
        return self.elems.pop()

    def remove_from_front(self):
        """Удаление элемента из начала"""
        return self.elems.pop(0)

    def size(self):
        """Размер экземпляра"""
        return len(self.elems)


def pal_checker(string):
    """Проверка на палиндром"""
    string = string.replace(' ', ' ').lower()

    dc_obj = DequeClass()

    for el in string:
        dc_obj.add_to_front(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_rear()
        last = dc_obj.remove_from_front()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("молоко делили ледоколом"))
print(pal_checker("Молоко делили Ледоколом"))
print(pal_checker("Обычная фраза"))