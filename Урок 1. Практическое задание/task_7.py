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


# вариант 1
def pal_checker_1(string: str):
    dc_obj = DequeClass()

    string = string.replace(' ', '').lower()
    # удаляем пробелы из строки и приводим строку к нижнему регистру
    for el in string:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal

# вариант 2
def pal_checker_2(string: str):
    dc_obj = DequeClass()

    for el in string:
        if el != ' ':
            dc_obj.add_to_rear(el.lower())
        # добавляем символ в дек, только если это не пробел
        # будет работать быстрее первого варианта,
        # т.к. нет дополнительных проходов по строке

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker_1("молоко делили ледоколом"))
print(pal_checker_1("А роза упала на лапу Азора"))

print(pal_checker_2("молоко делили ледоколом"))
print(pal_checker_2("А роза упала на лапу Азора"))
