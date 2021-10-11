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

class Deque:
    def __init__(self):
        self.deque = []
    def add_right(self,el):
        self.deque.append(el)
    def add_left(self,el):
        self.deque.insert(0, el)
    def pop_right(self):
        self.deque.pop()
    def pop_left(self):
        self.deque.pop(0)
w = Deque()
w.add_left(1)
w.add_left(2)
w.add_left(3)
print(w.deque)
w.pop_left()
print(w.deque)
w.pop_right()
print(w.deque)