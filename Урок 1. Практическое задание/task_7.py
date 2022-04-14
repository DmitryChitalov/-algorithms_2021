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


def pal_checker(string):
    dc_obj = DequeClass()
    no_space = ''.join(string.split())  # перед обработкой текста убераем пробелы
    for el in no_space:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()

        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("молоко делили ледоколом"))
print(pal_checker("молоко делили ледоколом"))
print(pal_checker("театр тает"))
print(pal_checker("утоп в поту"))
print(pal_checker("город дорог"))
print(pal_checker("медея едем"))
print(pal_checker("цепок скопец"))
print(pal_checker("он же нежно"))
print(pal_checker("терпит и прет"))
print(pal_checker("рембо обмер"))
print(pal_checker("олудили дуло"))

#Проблема в том, что выдает False если будет знаки припинания 
#или заглавная буква, вцелом зада решена

