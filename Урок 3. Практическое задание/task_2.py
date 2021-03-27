"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
# sqlite, postgres, db_api, orm
import hashlib
from sqlite3 import Error, connect


class DatabaseOfPasswords:
    def __init__(self, path):
        self.connection = self.create_connection(path)

    # подключились к базе данных. если ее нет, то создали новую
    @staticmethod
    def create_connection(path):
        connection = None
        try:
            connection = connect(path)
            print('Соединение установлено')
        except Error as e:
            print(f'Ошибка соединения: {e}')
        return connection

    # запрос в бд
    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print('Запрос выполнен успешно')
        except Error as e:
            print(f'Запрос не выполнен. Ошибка: {e}')

    # для select-запроса
    def execute_read_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f'Запрос не выполнен. Ошибка: {e}')

    # вставка значений
    def insert(self, login, passwd):
        insert_val = f"""
            INSERT INTO
                passwords (login, password)
            VALUES ('{login}', '{passwd}');
    
            """
        try:
            self.execute_query(insert_val)
        except Error as e:
            print(f'Ошибка "{e}"')

    # собственно проверка пароля
    def autorization(self):
        user_login = str(input('Введите логин: '))

        select_password = f"SELECT password FROM passwords WHERE login = '{user_login}';"
        data = self.execute_read_query(select_password)
        if not data:
            print('Вы не зарегистрированы в системе. Зарегистрируйтесь.')
            user_login = str(input('Введите логин: '))
            user_password = str(input('Введите пароль: '))

            hash_password = hashlib.sha256(user_password.encode() + user_login.encode()).hexdigest()
            self.insert(user_login, hash_password)
        else:
            user_password = str(input('Введите пароль: '))
            hash_password = hashlib.sha256(user_password.encode() + user_login.encode()).hexdigest()
            if data[0][0] != hash_password:
                print('Неверный пароль. Отказано в доступе')
            else:
                print('Доступ разрешен')


db1 = DatabaseOfPasswords('C:\\Users\Михаил\Desktop\ЖАННА УЧЕБА\Алгоритмы и структуры данных\sm_app.sqlite')

drop_table = 'Drop table if exists passwords;'
create_passwords_table = """
    CREATE TABLE IF NOT EXISTS passwords(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        login TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
    """

print('В базе данных создаем таблицу для хранения паролей: ')
db1.execute_query(drop_table)
db1.execute_query(create_passwords_table)

print('Добавим в базу несколько пользователей:')

login1 = 'user1'
passwd1 = '123'
print(f'{login1} : {passwd1}')

login2 = 'user2'
passwd2 = '123'
print(f'{login2} : {passwd2}')

db1.insert(login1, hashlib.sha256(passwd1.encode() + login1.encode()).hexdigest())
db1.insert(login2, hashlib.sha256(passwd2.encode() + login2.encode()).hexdigest())

db1.autorization()

print()
print('Выведем на экран всех пользователей и их хеши:')

select_from_table = "SELECT * FROM passwords;"
database_table = db1.execute_read_query(select_from_table)
for el in database_table:
    print(el)

