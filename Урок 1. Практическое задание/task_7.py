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

def conv_to_list(string):  # преобразование строки в массив - убраны пробелы и разбита строка в список по ,
    conv_list = []
    # string = string.replace('  ', ' ')  # Можно добавить спец символы, которые следует удалять
    string = string.split(' ')
    for element in string:
        # print(element)
        conv_list.append(str(element))
        conv_list = list(set(conv_list))   # set - убирет повторы в списке
    return(conv_list)

def pal_checker_1(string):
    print("Введенная строка:", string, '\n')
    # например: 'топот топот лол' - каждое слово разбирается отдельно
    if ' ' in string:
        list_string = conv_to_list(string)
        print('list_string', list_string)
        for element in list_string:
            print('element ', element)
            pal_checker(element)
    else:
        dc_obj = DequeClass()
        for el in string:
            dc_obj.add_to_rear(el)

        still_equal = True

        while dc_obj.size() > 1 and still_equal:
            first = dc_obj.remove_from_front()
            last = dc_obj.remove_from_rear()
            if first != last:
                still_equal = False
        print('palindrom?', still_equal , '\n-----------------------')

    # return still_equal

def pal_checker_2(string):
    print("Введенная строка:", string)
    # например: 'топот топот лол' - каждое слово разбирается отдельно
    string = string.replace(' ', '')  # Можно добавить спец символы, которые следует удалять

    dc_obj = DequeClass()
    for el in string:
        dc_obj.add_to_rear(el)
    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False
    return still_equal


# print(conv_to_list("молоко делили ледоколом"))
# print(pal_checker_1("молоко делили ледоколом топот"))
print("---------        Задача на поиск палиндрома      -----------")
print("палиндром? - ", pal_checker_2("молоко    делили ледоколом"), '\n')
print("палиндром? - ", pal_checker_2("топ от"), '\n')
