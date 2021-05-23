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


def database_connect():
    conn = sqlite3.connect('cash_url.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS cash_url (
                url TEXT UNIQUE, 
                cash_url TEXT)
        """)
    conn.commit()
    return conn


def check_cash(url):
    conn = database_connect()
    cursor = conn.cursor()
    cursor.execute('SELECT url FROM cash_url WHERE url = ?', (url,))
    url = cursor.fetchone()
    return url


def get_hash(url):
    salt = url + 'secret_prase'
    hash_obj = hashlib.sha256(salt.encode() + url.encode())
    hex_dig = hash_obj.hexdigest()
    return hex_dig


def add_url(url):
    add_url = 'INSERT INTO cash_url(url, cash_url) VALUES (?, ?);'
    data_tuple = (url, get_hash(url))
    conn = database_connect()
    cursor = conn.cursor()
    cursor.execute(add_url, data_tuple)
    conn.commit()


def get_all_url():
    conn = database_connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cash_url')
    get_all = cursor.fetchall()
    return get_all


url = input('Введите url для добавления в базу кеша')
if url == '':
    print('Вы не ввели url')
else:
    check = check_cash(url)
    if check is None:
        add_url(url)
        print('URL добавлен в кеш')
        print(f'В данный момент страницы в кеше')
        get_all = get_all_url()
        for el in get_all:
            print(el)
    else:
        print('Данная страница уже есть в кеше!')
