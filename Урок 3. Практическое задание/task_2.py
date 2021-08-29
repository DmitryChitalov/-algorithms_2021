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
import sqlite3
from hashlib import sha256


class HashedPasses:
    def __init__(self, db):
        self.salt = b'selfsalted'
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor( )

    def __check_pass(self):
        password = input('Введите пароль для проверки: ')
        self.cursor.execute('select hash from pass_hash where pass = :password', {'password': password})
        result = self.cursor.fetchall( )
        try:
            if sha256(self.salt + password.encode('utf-8')).hexdigest( ) == result[0][0]:
                print('Вы ввели правильный пароль')
        except IndexError:
            print('Данного пароля нет в базе данных.')
            return None

    def __add_pass(self):
        password = input('Введите пароль: ')
        password_hash = sha256(self.salt + password.encode('utf-8')).hexdigest( )
        print(f'В базе данных хранится строка: {password_hash}')
        self.cursor.execute('insert into pass_hash values (:hash, :pass)',
                            {'hash': password_hash,
                             'pass': password})
        self.connection.commit( )

    def truncate_table(self):
        self.connection.execute('delete from pass_hash')
        self.connection.commit( )

    def task_scenarion(self):
        self.__add_pass( )
        self.__check_pass( )


test1 = HashedPasses('task_3_db.db')
test1.task_scenarion( )
