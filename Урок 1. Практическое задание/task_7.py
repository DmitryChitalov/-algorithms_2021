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
from task_16 import DequeClass
import re


def remove_extra_spaces(space_str):
    """
    Функция удаляет лишние пробелы из строки (множественные пробелы заменяет на одинарные)
    """
    return re.sub(r'\s+', ' ', space_str)


def pal_checker(string):
    """
        Функция отрабатывает правильно, только если слова разделены одним пробелом.
        Если между пробелами два и более пробелов, следует убрать лишние.
        Одинарные пробелы в начале и конце строки не помеха.
    """
    dc_obj = DequeClass()

    for el in string:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        if first == ' ':
            first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if last == ' ' and dc_obj.size() == 0:
            break
        elif last == ' ':
            last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("топот"))
print(pal_checker("молоко делили ледоколом"))
print(pal_checker(remove_extra_spaces("   молоко        делили      ледоколом  ")))
print(pal_checker("aa aa"))
print(pal_checker("aa a aa"))
print(pal_checker("a aa a"))
print(pal_checker("a ab a"))