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

def pal_checker(string):
    dc_obj = DequeClass()
    my_world = re.sub(r'\s+', '', string) # можно так
    for el in my_world:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("молоко делили ледоколом"))
print(pal_checker("топот"))