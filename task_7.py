"""
Задание 7.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""


def polindrom_check (userstring):
    str_list = userstring.split(' ')
    userstring = ''.join(str_list)
    for i in range(0, len(userstring) // 2):
        if userstring[i] == userstring[len(userstring) - i - 1]:
            continue
        else:
            return 'Не является полиндромом'
    return 'Строка является полиндромом'


userstring = input('Введите строку для проверки')
print(polindrom_check(userstring))
