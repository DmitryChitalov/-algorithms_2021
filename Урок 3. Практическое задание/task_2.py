"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.

Самый простой вариант хранения хешей - просто в оперативной памяти (в переменных).

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""

from hashlib import sha256
from pymongo import MongoClient
import config as cfg


class UserAuthenticator:

    def __init__(self):
        # Подключение к БД
        #  - Чтение настроек
        self.__db_host = cfg.get_config['MongoDB']['host']
        self.__db_port = int(cfg.get_config['MongoDB']['port'])
        self.__db_tz_aware = bool(cfg.get_config['MongoDB']['tz_aware'])
        self.__db_username = cfg.get_config['MongoDB']['username']
        self.__db_password = cfg.get_config['MongoDB']['password']

    def create_password(self):
        pwd_hash = sha256(f"lesson03task_2@{input('Введите пароль: ')}".encode('utf-8')).hexdigest()
        print(f"Полученный хеш: {pwd_hash}")
        if self.__find_hash(pwd_hash):
            print("Пароль уже есть в БД.")
        else:
            self.__save_to_db(pwd_hash)
        repwd_hash = sha256(f"lesson03task_2@{input('Введите пароль повторно: ')}".encode('utf-8')).hexdigest()
        if pwd_hash == repwd_hash:
            print("Введённые пароли совпадают")
        else:
            print("Введённые пароли не совпадают!")
            print(f"pwd_hash: {pwd_hash}")
            print(f"repwd_hash: {repwd_hash}")

    def __save_to_db(self, password):
        with MongoClient(host=self.__db_host,
                         port=self.__db_port,
                         tz_aware=self.__db_tz_aware,
                         username=self.__db_username,
                         password=self.__db_password) as client:

            collection = client['Lesson03']['passwords']
            filter_query = {
                'pwd': password,
            }
            collection.update_one(filter_query, {'$set': {'pwd': password}}, upsert=True)

    def __find_hash(self, pwd_hash):
        with MongoClient(host=self.__db_host,
                         port=self.__db_port,
                         tz_aware=self.__db_tz_aware,
                         username=self.__db_username,
                         password=self.__db_password) as client:

            collection = client['Lesson03']['passwords']
            if collection.count_documents({"pwd": pwd_hash}) > 0:
                return True
            else:
                return False


if __name__ == '__main__':
    ua = UserAuthenticator()
    ua.create_password()
