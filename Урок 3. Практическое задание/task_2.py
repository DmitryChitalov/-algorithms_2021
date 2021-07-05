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
from hashlib import sha256
from os.path import join, dirname
from sqlite3 import connect, OperationalError, IntegrityError


class HashClass:
    def __init__(self):
        self.db_obj = join(dirname(__file__), "user_data.sqlite")
        self.conn = connect(self.db_obj)
        self.crs = self.conn.cursor()

    def create_table(self):
        create_stmt = "CREATE TABLE user_info (user_login varchar(255) unique, hash_password varchar(255));"
        try:
            self.crs.execute(create_stmt)
        except OperationalError:
            print("Таблица уже есть")
        else:
            self.conn.commit()
            print("Таблица создана")

    def get_hash(self):
        login = input("введите логин: ")
        passwd = input("введите пароль: ")
        hash_obj = sha256(login.encode() + passwd.encode()).hexdigest()
        return login, hash_obj

    def register(self):
        login, reg_hash = self.get_hash()
        insert_stmt = "INSERT INTO user_info (user_login, hash_password) VALUES (?, ?);"
        user_info = (login, reg_hash)
        try:
            self.crs.execute(insert_stmt, user_info)
        except IntegrityError:
            print("Данный логин уже занят, попробуйте войти в свою учетку")
        else:
            self.conn.commit()
            print(f"{login}, Вы зарегестрировались")
        self.conn.close()

    def log_in(self):
        login, checked_hash = self.get_hash()
        select_stmt = "SELECT hash_password FROM user_info WHERE user_login = ?;"
        self.crs.execute(select_stmt, (login,))
        out_hash = self.crs.fetchone()
        try:
            if checked_hash == out_hash[0]:
                print(f"{login}, вход в учетную запись выполнен")
            else:
                print("Возможно вы ошиблись при введении пароля, попробуйте еще раз")
        except TypeError:
            print("Возможно вы ошиблись при введении логина, попробуйте еще раз или пройдите регистрацию")
        self.conn.close()  # после выполнения входа нет нужды оставлять активным подключение к базе


Our_website = HashClass()
Our_website.create_table()
Our_website.register()
Our_website = HashClass()
Our_website.log_in()

"""
Данные в базе, которую прикладываю к проекту
логин: user01
пароль: 2021

Предложенный вариант не идеален, так как приходится регулярно создавать подключение и курсор через создание экземпляра 
класса, но сделано это, чтобы не оставлять активным подключение к БД. В учебном примере это не так критично, но при 
подключении большого числа пользователей нагрузка будет существенно увеличена. 

Жаль, что в учебных проектах мало шансов наступить на эти грабли, так как нагрузки особо не будет, а значит на эти 
грабли есть риск наступить уже при работе над реальным проектом.
"""