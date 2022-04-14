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


def is_pal(string: str):
    deq = DequeClass()
    deq.elems = list(string.replace(' ', '').replace(',', '').replace('.', '').replace('!', '').lower())
    while len(deq.elems) > 1:
        if deq.remove_from_front() != deq.remove_from_rear():
            return False
    return True


print(is_pal('rot or or rot'))
print(is_pal('rot or'))
print(is_pal('r'))
print(is_pal('rr'))
print(is_pal('r r'))
print(is_pal('ro'))
print(is_pal('ротор'))
print(is_pal('saippuakauppias'))
print(is_pal('Муза, ранясь шилом опыта, ты помолишься на разум'))
print(is_pal('Дорог Рим город или дорог Миргород'))