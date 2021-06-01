import hashlib
import mysql.connector


def db_data_inserting(table_name):
    def hashing(function):
        def wrapped(*args):
            insert_cnx = mysql.connector.connect(user="root", password="fight2003",
                                                 host='127.0.0.1', database='my_test_db')
            insert_cursor = insert_cnx.cursor()
            while True:
                result = function(*args)
                result[1] = hashlib.sha256(result[0].encode() + result[1].encode()).hexdigest()
                insert_query = ("INSERT INTO {} (login, pass) VALUES (%s, %s)").format(table_name)
                try:
                    insert_cursor.execute(insert_query, result)
                    print(f'В базе данных сохранён пароль в виде: {result[1]}')
                    insert_cnx.commit()
                    insert_cnx.close()
                    break
                except mysql.connector.errors.IntegrityError:
                    print('Введённое имя пользователя уже существует.')
        return wrapped
    return hashing


def db_data_reading(table_name, login):
    read_cnx = mysql.connector.connect(user="root", password="fight2003",
                                       host='127.0.0.1', database='my_test_db')
    read_cursor = read_cnx.cursor()
    read_query = ("SELECT * FROM {} WHERE users.login = '{}'".format(table_name, login))
    read_cursor.execute(read_query)
    result = read_cursor.fetchall()
    read_cnx.close()
    if len(result) == 0:
        return None
    else:
        return result[0][2]


def data_hashing(hashed_data: list):
    hashed_data[1] = hashlib.sha256(hashed_data[0].encode() + hashed_data[1].encode()).hexdigest()
    return hashed_data


def entering_user_data():
    new_login = input('Введите имя пользователя: ')
    user_password = input('Введите пароль: ')
    user_data = [new_login, user_password]
    return user_data


@db_data_inserting('users')
def user_registration():
    """
    Функция регистрации пользователя
    :return: список, который содержит данные пользователя
    """
    print('Для регистрации в сервисе введите логин и пароль.')
    new_user_data = entering_user_data()
    return new_user_data


def user_authentication():
    print('Для входа в сервис введите логин и пароль.')
    hashed_user_data = data_hashing(entering_user_data())
    if db_data_reading('users', hashed_user_data[0]) == hashed_user_data[1]:
        return True
    elif db_data_reading('users', hashed_user_data[0]) is None:
        return False


user_choice = None
while user_choice != '0':
    user_choice = input('Введите\n"1" для регистрации пользователя,\n'
                        '"2" для входа в систему: ')
    if user_choice == '1':
        user_registration()
    elif user_choice == '2':
        if user_authentication():
            print(print('Авторизация пройдена успешно! Добро пожаловать!'))
            user_choice = '0'
        else:
            print('Имя пользователя или пароль неверны!')
    else:
        print('Ввод некорректен')
