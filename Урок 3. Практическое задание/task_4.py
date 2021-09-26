"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш

хеш-url : url


Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете усложнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

from hashlib import sha256
from pymongo import MongoClient
import config as cfg
from requests import get


class Cache:

    def __init__(self):
        self.__url_cashe = {}

        # Подключение к БД
        #  - Чтение настроек
        self.__db_host = cfg.get_config['MongoDB']['host']
        self.__db_port = int(cfg.get_config['MongoDB']['port'])
        self.__db_tz_aware = bool(cfg.get_config['MongoDB']['tz_aware'])
        self.__db_username = cfg.get_config['MongoDB']['username']
        self.__db_password = cfg.get_config['MongoDB']['password']

    def cache_url(self, url: str) -> str:
        with MongoClient(host=self.__db_host,
                         port=self.__db_port,
                         tz_aware=self.__db_tz_aware,
                         username=self.__db_username,
                         password=self.__db_password) as client:

            collection = client['Lesson03']['url_cache']
            url_hash = sha256(f"{url[8:11]}@{url}".encode('utf-8')).hexdigest()
            if collection.count_documents({"url_hash": url_hash}) > 0:
                print("\n\n========= Cached =========\n")
                return collection.find_one({"url_hash": url_hash})['url_html']
            else:
                url_html = get(url).text
                collection.insert_one({"url_hash": url_hash, "url_html": url_html})
                print("\n\n========= New =========\n")
                return url_html


if __name__ == '__main__':
    cch = Cache()
    print(cch.cache_url('https://docs.mongodb.com/manual/tutorial/insert-documents/'))
    print(cch.cache_url('https://gb.ru/lessons/158178'))
    print(cch.cache_url('https://docs.python.org/3.9/library/time.html#time.time'))
    print(cch.cache_url('https://gb.ru/lessons/158178'))
