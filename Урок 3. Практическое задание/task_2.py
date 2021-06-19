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
import pandas as pd
import MySQLdb
import sshtunnel
import logging
from sshtunnel import SSHTunnelForwarder

ssh_host = '192.168.1.58'
ssh_username = 'user'
ssh_password = '000000'
database_username = 'root'
database_password = '111111'
database_name = 'sample'
localhost = '127.0.0.1'


def open_ssh_tunnel(verbose=False):
    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG

    global tunnel
    tunnel = SSHTunnelForwarder(
        (ssh_host, 22),
        ssh_username=ssh_username,
        ssh_password=ssh_password,
        remote_bind_address=('127.0.0.1', 3306)
    )

    tunnel.start()
    print('ssh connected')


def mysql_connect():
    global connection

    connection = MySQLdb.connect(
        host=localhost,
        user=database_username,
        passwd=database_password,
        db=database_name,
        port=tunnel.local_bind_port
    )
    print('mysql connected')


def run_query(sql):
    return pd.read_sql_query(sql, connection)


def mysql_disconnect():
    connection.close()


def close_ssh_tunnel():
    tunnel.close


def password_salt_hasher(password):
    salt = 'salt_forever'
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()


open_ssh_tunnel()
mysql_connect()
user_password = password_salt_hasher(input('Input the password: '))
print(user_password)
cursor = connection.cursor()

# If you need to crete a table, you may execute the lines below

# cursor.execute("DROP TABLE IF EXISTS passwords")
# cursor.execute("""CREATE TABLE passwords(
#           id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
#           pass_hash VARCHAR(255))""")

sql = "INSERT INTO `passwords`(`pass_hash`) VALUES ('%s')" % (user_password)
try:
    cursor.execute(sql)
    connection.commit()
    print('Connection success')
except:
    connection.rollback()
    print('Operation error')

sql = "SELECT pass_hash FROM passwords WHERE pass_hash = '%s'" % (user_password)
cursor.execute(sql)
print('The new string saves in the db: '+str(cursor.fetchone()))

user_password_check = password_salt_hasher(input('Confirm the password, input it again: '))
sql = "SELECT * FROM passwords WHERE pass_hash = '%s'" % (user_password_check)
answer = ''
try:
    answer = cursor.execute(sql)
    connection.commit()
    print('Connection success')
except:
    connection.rollback()
    print('Operation error')
if answer != 0:
    print('Confirmed password is correct!')
else:
    print("Confirmed password isn't correct. Try again.")

mysql_disconnect()
close_ssh_tunnel()