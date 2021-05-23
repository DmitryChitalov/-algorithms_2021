"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import sqlite3
import hashlib
from datetime import datetime


def create_database():
    global sqlite_connection
    try:
        sqlite_connection = sqlite3.connect('sites.db')
        sqlite_create_table_query = '''CREATE TABLE sites(
                                    urls TEXT(255) NOT NULL,
                                    hash TEXT(255) NOT NULL,
                                    date_reg DATETIME);'''

        cursor = sqlite_connection.cursor()
        # print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        # print("Таблица SQLite создана")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    insert_urls()


def insert_urls():
    global hash, urls

    database = sqlite3.connect('sites.db')
    cursor = database.cursor()

    urls = input('Введите url адрес:  ').lower()
    ursl_descript = input('Введите описание (Например: "GOOGLE"): ').lower()
    urls_hash_descript = hashlib.sha256(ursl_descript.encode())
    hash = hashlib.sha256(urls.encode() + b'{urls_hash_descript}').hexdigest()

    cursor.execute("SELECT * FROM sites WHERE hash=?", [hash])
    search = cursor.fetchone()
    if search is None:
        print('Сайта нет в кеше! Он будет добавлен!')
        date_reg = datetime.now()
        data_user = '''INSERT INTO sites(urls, hash, date_reg)
                            VALUES (?, ?, ?);'''
        # Формируем кортеж для записи
        data_tuple = (urls, hash, date_reg)

        cursor.execute(data_user, data_tuple)
        database.commit()

        print('Сайт добавлен в кеш!')
        print(hash)

    elif hash == search[1]:
        print('Сайт есть в кеше! Кеширование не требуется')
        cursor.close()


create_database()
