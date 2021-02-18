"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
import sqlite3
from hashlib import sha256
from  random import choice
from string import ascii_uppercase

conn = sqlite3.connect("lesson3_task2.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                    pass TEXT NOT NULL, 
                                                    salt TEXT NOT NULL);""")
conn.commit()
##################################################################################

def heshed_str(input_str,salt):
    ''' Возвращает хеш строки'''
    return sha256(input_str.encode() + salt.encode()).hexdigest()

def salt_gen(salt_len):
        ''' Генерация соли для новых URL'''        
        return ''.join(choice(ascii_uppercase) for i in range(salt_len))

def verify_pass(input_str):
    db_cash_list = (cur.execute("SELECT * FROM users;")).fetchall()
    for row in db_cash_list:
        salt = row[2]
        pass_hash = sha256(user_input_str.encode() + salt.encode()).hexdigest()
        if pass_hash == row[1]:
            return f"Пароль верен !"
    else:
        return f"Ошибка ввода !"
#############################################################################
user_input_str = input("Введите пароль:").strip(' ')

salt = salt_gen(12)
hash_psw = heshed_str(user_input_str,salt)

db_row = (hash_psw,salt)
cur.execute("INSERT INTO users (pass,salt) VALUES(?,?);", db_row)
conn.commit()
##############################################################################
user_input_str = input("Повторите пароль:").strip(' ')

res = verify_pass(user_input_str)
print(res)

