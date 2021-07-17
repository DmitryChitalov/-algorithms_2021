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
import mysql.connector

login = input('Введите login: ')  # логин будет солью
passw = input('Введите пароль: ')

hash_obj = hashlib.sha256(passw.encode('utf-8') + login.encode('utf-8'))
print(f'В переменной хранится пароль: {hash_obj.hexdigest()}')

# запись в файл
with open('hesh.txt', 'w', encoding='utf-8') as file_1:
    file_1.writelines(hash_obj.hexdigest())

# запись в БД
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rooter",
    database="vk"
)
cursor = mydb.cursor()
cursor.execute("SELECT p.id FROM passwords p WHERE p.login = %s", (login,))
id_bd = cursor.fetchall()
if not id_bd:
    cursor.execute("INSERT INTO passwords VALUES (null, %s, %s)", (hash_obj.hexdigest(), login,))
    mydb.commit()
else:
    print('Данный login уже хранится в БД (занят)! Придумайте другой')

passw2 = input('Введите пароль еще раз для проверки: ')
hash_obj2 = hashlib.sha256(passw2.encode('utf-8') + login.encode('utf-8'))

# проверяем в переменной
if hash_obj.digest() == hash_obj2.digest():
    print('Вы ввели правильный пароль')
else:
    print('Вы ввели не верный пароль')

# проверяем из файла
with open('hesh.txt', 'r', encoding='utf-8') as f:
    hash_obj_file = f.read()
print(f'В файле хранится пароль: {hash_obj_file}')
if hash_obj2.hexdigest() == hash_obj_file:
    print('Вы ввели правильный пароль')
else:
    print('Вы ввели не верный пароль')

# проверяем из БД
if not id_bd:
    cursor.execute("SELECT p.passw FROM passwords p WHERE p.login = %s", (login,))
    hash_bd = cursor.fetchall()
    print(f'в БД такой пароль: {hash_bd[0][0]}')
    if hash_obj2.hexdigest() == hash_bd[0][0]:
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели не верный пароль')

mydb.close()
