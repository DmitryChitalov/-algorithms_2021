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
import pymysql.cursors

# Подключиться к базе данных.
connection = pymysql.connect(host='localhost', user='root', password='*****', db='user_pass', charset='utf8mb4')
print("Подключение выполнено!")

passwd = input('Введите пароль: ')
salt = 'login_user'
hash_obj = hashlib.sha256(passwd.encode('utf-8') + salt.encode('utf-8'))
print(hash_obj.hexdigest())
# 3b2aded5e8d001845710769929773d9c3fa579615eb2e1897b1da5841437ce32 (if passwd == 'password')
try:
    # SQL
    cursor = connection.cursor()
    sql = f"INSERT into user_password (hash_pas) VALUES ('{hash_obj.hexdigest()}')"  # Сохраняем хэш в столбец с паролем
    cursor.execute(sql)
    connection.commit()
    print('Регистрация завершена')
    # SQL
    sql_check = "SELECT hash_pas FROM user_password"
    # Выполнить команду запроса (Execute Query).
    cursor.execute(sql_check)
    all_pas = []
    for row in cursor:
        all_pas.extend(row)
    passwd_1 = input('Повторите пароль: ')
    hash_obj_1 = hashlib.sha256(passwd_1.encode('utf-8') + salt.encode('utf-8'))
    while hash_obj_1.hexdigest() not in all_pas:
        passwd_1 = input('Вы не верно ввели пароль, попробуйте еще раз: ')
        hash_obj_1 = hashlib.sha256(passwd_1.encode('utf-8') + salt.encode('utf-8'))
    print('Вы ввели правильный пароль')
finally:
    connection.close()
    print('Сессия завершена')
