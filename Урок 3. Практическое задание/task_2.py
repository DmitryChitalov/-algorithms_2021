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
from uuid import uuid4
import hashlib
import sqlite3

# создаем переменную с паролем и переменную с солью
user_pass = input('Введите пароль: ')
salt = uuid4().hex

# Коннектимся к БД
conn = sqlite3.connect('passwords.sqlite')
# Создаем курсор для работы с БД
cursor = conn.cursor()
# Создаем таблицу паролей с 2 стобцами - хеш и пароль
cursor.execute("CREATE TABLE passwords (hash VARCHAR NOT NULL UNIQUE, password VARCHAR NOT NULL)")
# Получаем хеш введенного пользователем пароля, "солим"
hash_user_pass = hashlib.sha256(salt.encode() + user_pass.encode()).hexdigest()
print(f'В БД хеш для вашего пароля: {hash_user_pass}')
# Добавляем хеш и сам пароль в таблицу нашей БД
cursor.execute('INSERT INTO passwords (hash, password) VALUES (?, ?)', (hash_user_pass, user_pass))
# Выводим значения столбцов, для того, чтобы можно было сравнить хеши
cursor.execute('SELECT * FROM passwords')
# Создаем переменную с повторным паролем
check_pass = input('Введите ваш пароль еще раз: ')
# Получаем его хэш
hash_check_pass = hashlib.sha256(salt.encode() + check_pass.encode()).hexdigest()
# Сравниваем
if hash_check_pass == cursor.fetchall()[0][0]:
    print('Вы ввели правильный пароль!')
else:
    print('Пароли не совпали!')
conn.close()
