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
import hashlib
import pymysql.cursors


# Подключиться к базе данных.


class Network:
    connection = pymysql.connect(host='localhost', user='root', password='*****', db='user_pass',
                                 charset='utf8mb4')

    def login(self):
        try:
            passwd = input('Введите пароль для регистрации: ')
            salt = 'login_user'
            hash_obj = hashlib.sha256((passwd + salt).encode('utf-8'))
            # Сохраняем хэш в столбец с паролем
            cursor = self.connection.cursor()
            sql = f"INSERT into user_password (hash_pas) VALUES ('{hash_obj.hexdigest()}')"
            cursor.execute(sql)
            self.connection.commit()
            print('Регистрация завершена')
            print(f'Сохраненный хеш: {hash_obj.hexdigest()}')
        except Exception as exp:
            print(f'Регистрация не удалась, ошибка {exp}')

    def register(self):
        try:
            cursor = self.connection.cursor()
            salt = 'login_user'
            sql_check = "SELECT hash_pas FROM user_password"  # Выполняем Select запрос для получения хешей паролей
            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql_check)
            all_pas = [row[0] for row in cursor]  # Создаем список со всеми хешами паролей

            passwd = input('Введите пароль: ')
            hash_obj = hashlib.sha256((passwd + salt).encode('utf-8'))
            # Выполняется цикл, пока пароль не совпадет
            while hash_obj.hexdigest() not in all_pas:
                passwd = input('Вы не верно ввели пароль, попробуйте еще раз: ')
                hash_obj = hashlib.sha256((passwd + salt).encode('utf-8'))
            print('Вы ввели правильный пароль')
        except Exception as exp:
            print(f'Регистрация не удалась, ошибка {exp}')

    def close_session(self):
        self.connection.close()


net = Network()

net.login()
net.register()
net.close_session()
