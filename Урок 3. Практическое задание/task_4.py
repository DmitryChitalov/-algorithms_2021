"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

url : хеш-url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


import hashlib
import pymysql
import requests


class CacheUrl:
    def __init__(self, link):
        self.connection = pymysql.connect(
                        host='localhost',
                        user='root',
                        password='******',
                        db='cache',
                        charset='utf8mb4'
                        )
        self.cursor = self.connection.cursor()
        self.link = link

    def hash_url(self):  # Хэшируем адрес страницы
        salt = 'some_salt'.encode()
        dk = hashlib.sha256(salt + self.link.encode()).hexdigest()
        return dk

    def select(self):
        sql = """
            SELECT hash FROM url_hash
            """
        self.cursor.execute(sql)
        val = self.cursor.fetchall()
        print(val)
        return val

    def update(self):  # Апдэйтим данные при посещении страницы
        sql = """
            UPDATE url_hash SET
            hash = '%s',
            content = '%s',
            created_at = NOW()
            WHERE hash = '%s'
            """ % (self.hash_url(), requests.get(self.link).url, self.hash_url())
        self.cursor.execute(sql)
        self.connection.commit()
        self.connection.close()

    def insert(self):  # Проверяем наличие страницы в базе
        if self.hash_url() in [i[0] for i in self.select()]:  # если есть совпадение
            self.update()                                     # вызываем функцию апдэйт
        else:                                                 # иначе добавляем данные в базу
            sql = """
                INSERT INTO url_hash (hash, content)
                VALUES ('%s', '%s')
                """ % (self.hash_url(), requests.get(self.link).url)
            self.cursor.execute(sql)
            self.connection.commit()
            self.connection.close()


obj_cash = CacheUrl('http://www.mail.ru')
obj_cash.insert()
"""
 Так же хотел реализовать удаление при достижении строк в таблицы определенного значения
 но времени нужно больше.
"""

# Ещё одна реализация без использования БД
base = {}


def hash_url(url):
    salt = 'some_salt'.encode()
    dk = hashlib.sha256(salt + url.encode()).hexdigest()
    return dk


def insert(url):
    if hash_url(url) in base.keys():
        return print('url exists')
    else:
        base[hash_url(url)] = requests.get(url).url


link = 'http://www.mail.ru'
insert(link)
print(base)  # {'796cfb53e135cad6bd4e1256e93f9b4a46519ce6d66d9ceea327fcef73b55727': 'https://mail.ru/'}
