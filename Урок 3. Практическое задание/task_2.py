"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""

import hashlib
import uuid
import sqlite3


class Database:

    def create_database(self, databasename):
        # Создание (проверка подключения) базы данных
        try:
            self.connect = sqlite3.connect(f'{databasename}.db')
            self.cur = self.connect.cursor()
            print("База данных создана и успешно подключена к SQLite")

            self.sqlite_select_query = "select sqlite_version();"
            self.cur.execute(self.sqlite_select_query)
            self.record = self.cur.fetchall()
            print("Версия базы данных SQLite: ", self.record)
            self.cur.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (self.connect):
                self.connect.close()
                print("Соединение с SQLite закрыто")

    def create_table(self, databasename):
        try:
            self.connect = sqlite3.connect(f'{databasename}.db')
            self.sqlite_create_table_query = '''CREATE TABLE users (
                                        userid INT PRIMARY KEY,
                                        firstname name TEXT,
                                        middlename TEXT,
                                        lastname TEXT,
                                        phone TEXT UNIQUE,
                                        email TEXT UNIQUE,
                                        hash_password TEXT,
                                        salt TEXT);'''

            self.cur = self.connect.cursor()
            print("База данных подключена к SQLite")
            self.cur.execute(self.sqlite_create_table_query)
            self.connect.commit()
            print("Таблица SQLite создана")

            self.cur.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (self.connect):
                self.connect.close()
                print("Соединение с SQLite закрыто")



class Users:

    def parametres(self):
        self.id = 1 #int(input('Значение id: '))
        self.firstname = 'Artem' #input('Введите имя: ')
        self.middlename = 'Victorovich' #input('Введите отчество: ')
        self.lastname = 'Stepanov' #input('Введите фамилию: ')
        self.phone = '12345' #input('Введите телефон: ')
        self.email = 'ok@google.com' #input('Введите почту: ')
        self.password = 'password' #input('Введите пароль: ')


    def salt_create(self):
        #Создание криптографической соли
        self.salt = uuid.uuid4().hex
        return self.salt


    def hash_password(self):
        "Создание хэша пароля с использованием крипт. соли"
        self.hash_password = hashlib.sha256(self.password.encode() + self.salt.encode()).hexdigest()
        return self.hash_password


    def insert_variables_into_db_table(self):
        try:
            # Создаем (подключаемся) к базе данных.
            self.connect = sqlite3.connect('Users.db')
            # Создаем объект cursor для выполнения SQL-запросов
            self.cur = self.connect.cursor()
            # Шаблон INSERT для SQLite3
            self.sqlite_insert = f"""INSERT INTO users(userid, firstname, middlename, lastname, phone, email, hash_password, salt)
                VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?);"""
            # Параметры помещаем в кортеж
            self.data_insert = (self.id, self.firstname, self.middlename, self.lastname, self.phone, self.email, self.hash_password, self.salt)

            # Выполняем
            self.cur.execute(self.sqlite_insert, self.data_insert)
            # Записываем изменения
            self.connect.commit()
            print("Данные добавлены в таблицу")
            # Закрываем объект
            self.cur.close()

        except sqlite3.Error as error:
            print('Ошибка при работе с SQLite3', error)

        finally:
            if (self.connect):
                self.connect.close()
                print('Соединение завершено')

    def get_hash_password(self, user_id):
        # Функция выбирает hash_password одного пользователя по id пользователя
        try:
            self.connect = sqlite3.connect(f'Users.db')
            self.cur = self.connect.cursor()
            print("Подключен к SQLite")

            self.sql_select_query = """select hash_password from users where userid = ? """
            self.get_hash_id = user_id
            self.cur.execute(self.sql_select_query, self.get_hash_id)
            self.db_hash_password = self.cur.fetchone()[0]
            #print(self.db_hash_password[0])

            self.cur.close()
            return self.db_hash_password

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if (self.connect):
                self.connect.close()
                print("Соединение с SQLite закрыто")

    def get_salt(self, user_id):
        # Функция выбирает hash_password одного пользователя по id пользователя
        try:
            self.connect = sqlite3.connect(f'Users.db')
            self.cur = self.connect.cursor()
            print("Подключен к SQLite")

            self.sql_select_query = """select salt from users where userid = ? """
            self.get_salt_id = user_id
            self.cur.execute(self.sql_select_query, self.get_salt_id)
            self.db_salt = self.cur.fetchone()[0]
            #print(self.db_salt[0])

            self.cur.close()
            return self.db_salt

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if (self.connect):
                self.connect.close()
                print("Соединение с SQLite закрыто")


    def check_password(self, user_id):
        "Сравнение хэшей пароля, введенного пользователем и хранящимся в базе данных"
        self.id_check = user_id #int(input('Значение id: '))
        self.password_check = 'passwor' #input('Введите пароль: ')

        for i in range(1000): #Замедляем хэширование чтобы негодяй потратил кучу времени
            self.check_hash_password = hashlib.sha256(self.password_check.encode() + self.get_salt(self.id_check).encode()).hexdigest()
            if self.check_hash_password == self.get_hash_password(self.id_check):
                return 'Пароль верный. Доступ разрешен'
            else:
                return 'Пароль неверный. Доступ запрещен'





database_2 = Database()
# database_2.create_table('users')

user_1 = Users()
user_1.parametres()
user_1.salt_create()
print(user_1.salt_create())
print(user_1.hash_password())
user_1.insert_variables_into_db_table()
# print(user_1.get_hash_password('1'))
# print(user_1.get_salt('1'))
print(user_1.check_password('1'))