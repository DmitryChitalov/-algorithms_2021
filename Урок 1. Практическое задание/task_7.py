""" Домашнее задание к уроку №1 курс Алгоритмы и структуры данных на Python
    студент: Максим Сапунов Jenny6199@yandex.ru
    29.05.2021
"""
#    Задание 7.
#    Задание на закрепление навыков работы с деком
#    В рассмотренном на уроке листинге есть один недостаток
#    Приведенный код способен "обработать" только строку без пробелов, например, 'топот'
#    Но могут быть и такие палиндромы, как 'молоко делили ледоколом'
#    Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
#    и в таких строках (включающих пробелы)
#    Примечание:
#    Вам не нужно писать код с нуля. Вам нужно доработать пример с урока.


class DequeClass:
    """ Простое представление дэка."""

    def __init__(self):
        """ Конструктор класса."""
        self.element = []

    def is_empty(self):
        return self.element == []

    def add_to_rear(self, elem):
        """ Добавить элемент в конец дэка. """
        self.element.append(elem)

    def add_to_front(self, elem):
        """ Добавить элемент в начало дэка."""
        self.element.insert(0, elem)

    def remove_from_rear(self):
        """ Удалить элемент из конца дэка. """
        return self.element.pop()

    def remove_from_front(self):
        """ Удалить элемент из начала дэка. """
        return self.element.pop(0)

    def size(self):
        """ Возвращает длину дэка. """
        return len(self.element)


def is_string_palindrome(palindrome):
    var1 = DequeClass()
    for symbol in palindrome:
        var1.add_to_rear(symbol)
    symbols_equal = True
    while var1.size() > 1 and symbols_equal:
        start_symbol = var1.remove_from_rear()
        last_symbol = var1.remove_from_front()
        if start_symbol != last_symbol:
            symbols_equal = False
    return True


if __name__ == '__main__':
    string = 'молоко делили ледоколом'
    print(is_string_palindrome(string))
