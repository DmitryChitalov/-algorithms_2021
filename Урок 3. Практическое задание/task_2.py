"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""
import hashlib


def salt_and_pass(s):
    user_salt = 'salt for password'
    user_pass_hash = hashlib.sha256(s.encode() + user_salt.encode()).hexdigest()
    print(user_pass_hash)
    return user_pass_hash


def get_pass_to_file():
    with open('bd_hash_pass.txt') as file:
        s = file.readline()
        return s


with open('bd_hash_pass.txt', 'w') as bd_hash:
    bd_hash.write(salt_and_pass('qwerty'))


n = 3
while n > 0:
    user_pass = input("Введите пароль\n")
    if salt_and_pass(user_pass) == get_pass_to_file():
        print("Пароль принят.")
        break
    else:
        n -= 1
        if n == 2:
            print(f"Пароль не верный, у вас {n} попытки.")
        elif n == 1:
            print(f"Пароль не верный, у вас {n} попытка.")
        else:
            print("Попытки кончились, запись заблокиролванна.")
        continue
