"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.

Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных).

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""
import hashlib

# список все алгоритмов, доступных в системе
# print(hashlib.algorithms_available)
# существующие алгоритмы модуля
# print(hashlib.algorithms_guaranteed)


salt = 'do crazy stuff'
filename = 'saved_pass.txt'


def save_to_file(hash):
    # open(filename, "x")
    with open(filename, "r+") as f:
        data = f.read()
        print(data)
        f.seek(0)
        f.write(str(hash))
        # f.truncate()
        print(data)

def ask_password():
    hash_pass = hashlib.sha256(input("Введите пароль: ").encode() + salt.encode())
    save_to_file(hash_pass)
    return hash_pass

def read_file():
    with open(filename, "r") as f:
        data = str(f.read())
        print("Data in file:", data)
        # f.seek(0)
        return data


def ask_password_again():
    hash_1 = read_file()
    hash_2 = hashlib.sha256(input("Введите пароль повторно   : ").encode() + salt.encode())
    print(hash_1, hash_2)
    print(type(hash_1), type(hash_2))
    if str(hash_2) == hash_1:
        print("Вы ввели правильный пароль")
    else:
        print("Пароли отличаются!")


# print(f'Созданный хеш: {ask_password()}')

ask_password()
ask_password_again()
