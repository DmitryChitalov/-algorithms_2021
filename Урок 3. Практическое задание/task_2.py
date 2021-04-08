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
import sqlite3


class SQLite:
    def __init__(self, database_file):
        """Подключение к БД и создание курсора соединения"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def create_tables(self, name_tab):
        """Создание таблиц"""
        with self.connection:
            self.cursor.execute(f"DROP TABLE IF EXISTS {name_tab};")
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {name_tab} ("
                                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                                "`login` varchar(10) ,"
                                "`password` TEXT );")

    def add_user(self, user_name, user_pasw):
        """Добавляю юзера и пароль"""
        with self.connection:
            self.cursor.execute("INSERT INTO users (`login`, `password`)"
                                " VALUES(?, ?);", (user_name, user_pasw))

    def select_sha(self, user_name):
        """Извлечь все из нужной таблицы"""
        with self.connection:
            result = self.cursor.execute(f'SELECT `password` '
                                         f'FROM users '
                                         f'WHERE `login` = "{user_name}"').fetchone()
            if result:
                return f'В базе данных хранится строка: {"".join(result)}'
            else:
                return


# Создаём базу данных и таблицу
db = SQLite('log_info.db')
db.create_tables('users')


def make_hash(login, passw):
    """Делаем Хеш"""
    return hashlib.sha256(login.encode() + passw.encode()).hexdigest()


def log_in():
    """Регистрируемся по Логину и Паролю"""
    print(f'>>> Форма Регистрации <<<')
    user_login = (input(f'Введите логин: ')).lower()
    user_passw = input(f'Введите пароль: ')
    db_hash = make_hash(user_login, user_passw)
    db.add_user(user_login, db_hash)
    print(db.select_sha(user_login))


log_in()

print(f'>>> Авторизация <<<')


def sign_in(trying=2):
    """Проверка Логина и Пароля"""
    user_input = input(f'Введите логин: ')
    data = db.select_sha(user_input)
    if not data:  # Попытки для логина
        print('Нет такого Юзера')
        print(f'Осталось попыток: {trying}')
        return print('Вот и всё!') if trying == 0 else sign_in(trying - 1)
    elif data.split(': ')[1] == make_hash(user_input, input('Верно, а сейчас пароль: ')):
        print(f'Ура, все верно!')
    else:
        count = 3  # Попытки для пароля
        print('Пароль не верный!!!')
        print(f'Кол-во попыток: {count}')
        while True:
            user_input_2 = input('Введите пароль: ')
            count -= 1
            if data.split(': ')[1] == make_hash(user_input, user_input_2):
                print('Все верно, вы вошли!')
                break
            elif count == 0:
                print("Хватит, пошли гулять :)")
                break


sign_in()