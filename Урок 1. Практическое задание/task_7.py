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
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_to_front(self, item):
        self.items.append(item)

    def add_to_rear(self, item):
        self.items.insert(0, item)

    def remove_from_front(self):
        return self.items.pop()

    def remove_from_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def check_palindrome(phrase):
    deq_obj = DequeClass()
    phrase = phrase.replace(' ', '')
    for el in phrase:
        deq_obj.add_to_rear(el)
    checker = True
    while deq_obj.size() > 1 and checker:
        _first_symbol = deq_obj.remove_from_front()
        _last_symbol = deq_obj.remove_from_rear()
        if _first_symbol != _last_symbol:
            checker = False

    return checker


if __name__ == '__main__':
    print(check_palindrome("молоко делили ледоколом"))
