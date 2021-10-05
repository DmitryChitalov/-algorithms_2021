"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""
from memory_profiler import profile
from uuid import uuid4
import hashlib
import sqlite3


# 1 простой вариант
salt = uuid4().hex
passw = '123'

base_passw = hashlib.sha256(salt.encode() + passw.encode()).hexdigest()

@profile
def login_1():
    if hashlib.sha256(salt.encode() + '123'.encode()).hexdigest() == base_passw:
        return f'Вы ввели правильный пароль'
    else:
        return f'Вы ввели неправильный пароль'

# 2 вариант через БД
@profile
def bd():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute("""CREATE TABLE users
                      (password_hash VARCHAR(100))
                   """)
    cursor.execute(f"""INSERT INTO users
                      VALUES ('{base_passw}')
                      """)

    sql_pass = cursor.execute("SELECT password_hash FROM users;").fetchone()[0]
    conn.close()

    if hashlib.sha256(salt.encode() + '123'.encode()).hexdigest() == sql_pass:
        return f'Вы ввели правильный пароль'
    else:
        return f'Вы ввели неправильный пароль'


if __name__ == '__main__':
    login_1()
    bd()

"""
На данном примере выигрыш не видно из-за того, что сами оперции занимают мало памяти,
но при использовании больших данных, мы сэкономим за счёт того, что сохраним данные в бд.
Это очень похоже не сериализацию с json.
"""