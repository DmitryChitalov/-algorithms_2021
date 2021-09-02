import sqlite3
from hashlib import sha256


def create_table() -> None:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    # Текст запроса
    sql_request = """
        CREATE TABLE IF NOT EXISTS users 
        (
        id INTEGER UNIQUE,
        login TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        PRIMARY KEY("id")
        );
    """
    # Попытка выполнить запрос
    try:
        cursor.execute(sql_request)
    except sqlite3.DatabaseError as err:
        print("Error: ", err)
    else:
        print("Таблица создана")
        conn.close()


def insert_user_data_2_table(login: str, password: str) -> bool:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    # Текст запроса
    sql_request = """
        INSERT INTO users 
        (id, login, password)
        VALUES
        (NULL, ?, ?)
    """
    # Новый пользователь для добавления в БД
    new_user = (login, password)

    # Попытка выполнить запрос
    try:
        cursor.execute(sql_request, new_user)
        success = True
    except sqlite3.DatabaseError as err:
        print("Error: ", err)
    else:
        # Сохранить транзакцию
        conn.commit()
        print("Запись в БД добавлена")
        conn.close()

    return success


def select_user_from_table(login: str) -> tuple:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    # Текст запроса
    sql_request = """
        SELECT 
            login, 
            password 
        FROM 
            users 
        WHERE login = ?;
    """

    user_log = (login,)

    # Попытка выполнить запрос
    try:
        cursor.execute(sql_request, user_log)
        user_data = cursor.fetchone()
        # print(user_data)

    except sqlite3.DatabaseError as err:
        print("Error: ", err)
    else:
        conn.close()

    return user_data


def get_login_n_hash(login: str, password: str) -> tuple:
    hash_obj = sha256(login.encode() + password.encode()).hexdigest()
    return login, hash_obj


def add_user_2_db():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    hash_the_user = get_login_n_hash(login, password)
    insert_user_data_2_table(hash_the_user[0], hash_the_user[1])


def chek_user():
    login = input("Введите логин для валидации: ")
    password = input("Введите пароль для валидации: ")

    # Пользователь из БД
    user_to_login = select_user_from_table(login)

    if user_to_login is None:
        print("Введенный пользователь не существует. Зарегистрируйтесь в системе.")
        add_user_2_db()
    else:
        if get_login_n_hash(login, password)[1] == user_to_login[1]:
            print("Пароль введен верно. Добро пожаловать.")
        else:
            print("Пароль неверный!")


if __name__ == '__main__':
    # add_user_2_db()
    # Проверка существования пользователя в БД. Ввести нового если отсутствует.
    chek_user()
