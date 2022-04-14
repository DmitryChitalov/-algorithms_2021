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
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor( )

    def register(self, login, password):
        try:
            self.cursor.execute('insert into pass_hash values (:login, :pass_hash)',
                                {'login': login,
                                 'pass_hash': HashedPasses.hash_pass(login, password)})
            self.connection.commit( )
            print('Успешная регистрация.')
        except sqlite3.IntegrityError:
            print('Данный логин уже занят.')

    def login(self, login, password):
        self.cursor.execute('select hash from pass_hash where login = :login', {'login': login})
        result = self.cursor.fetchall( )
        try:
            if HashedPasses.hash_pass(login, password) == result[0][0]:
                print('Успешная авторизация.')
            else:
                print('Был введён неверный пароль.')
        except IndexError:
            print('Такого пользователя не существует.')

    @staticmethod
    def hash_pass(login, password):
        return sha256(login.encode('utf-8') + password.encode('utf-8')).hexdigest( )


if __name__ == '__main__':
    AUTHORIZATION_BASE = HashedPasses('LOGIN_PASS.db')
    action = input('У вас уже имеется аккаунт?(Да/Нет) ')
    if action.lower( ) == 'да':
        login = input('Введите имя пользователя: ')
        password = input('Введите пароль: ')
        AUTHORIZATION_BASE.login(login, password)
    if action.lower( ) == 'нет':
        login = input('Введите имя пользователя: ')
        password = input('Введите пароль: ')
        AUTHORIZATION_BASE.register(login, password)
