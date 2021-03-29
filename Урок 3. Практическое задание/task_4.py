"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
import sqlite3
from hashlib import sha256
from  random import choice
from string import ascii_uppercase

conn = sqlite3.connect("url_cash.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS urls_dat")
cur.execute("""CREATE TABLE IF NOT EXISTS urls_dat (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                    url_ TEXT NOT NULL,hash_ TEXT NOT NULL, 
                                                    salt TEXT NOT NULL);""")
class Master_Url:
    '''Класс работы с базой данных кешированных URL'''
    def __init__(self,db):
        self.__conn = sqlite3.connect("url_cash.db")
        self.__cur = conn.cursor()

    def hash_find(self,url):
        '''Поиск хеша URL в БД , кеширование при отсутствии'''
        
        db_cash_list = (self.__cur.execute("SELECT * FROM urls_dat;")).fetchall()
        for row in db_cash_list:
            salt = row[3]
            url_hash = self.__url_to_cash(url,salt)
            if url_hash == row[2]:
                return f"{url} есть в БД"

        salt = self.__salt_gen(12)
        url_hash = self.__url_to_cash(url,salt)
        db_row = (url,url_hash,salt)
        self.__cur.execute("INSERT INTO urls_dat (url_,hash_,salt) VALUES(?,?,?);", db_row)        
        return f"{url} занесен в БД"

    def __url_to_cash(self,url,salt):
        '''Кеширование URL'''
        hash_url = sha256(url.encode() + salt.encode()).hexdigest()
        return hash_url

    def __salt_gen(self,salt_len):
        ''' Генерация соли для новых URL'''
        salt = ''.join(choice(ascii_uppercase) for i in range(salt_len))
        return salt


##################################################################################
print("_-"*10, " TEST ","-_"*10)
m_url = Master_Url("url_cash.db")
print(m_url.hash_find("https://geekbrains.ru"))
print(m_url.hash_find("https://youtube.ru"))
print(m_url.hash_find("https://yandex.ru"))
print(m_url.hash_find("https://geekbrains.ru"))
print(m_url.hash_find("https://yandex.ru"))
print(m_url.hash_find("https://yandex.ru"))
print(m_url.hash_find("https://geekbrains.ru"))
print(m_url.hash_find("https://github.ru"))

#################################################################################
print("_-"*10, " DATABASE ","-_"*10)
db_cash_list = (cur.execute("SELECT * FROM urls_dat;")).fetchall()
for i in db_cash_list:
    print(i)
conn.close()