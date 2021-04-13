import sqlite3


class Storage:
    def __init__(self):
        self.__conn = sqlite3.connect("users.db")
        self.__cur = self.__conn.cursor()
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS users
                              (username text PRIMARY KEY, passwd_hash blob, last_login text)
                           """)

    def create_account(self, username, passwd):
        try:
            query = "INSERT INTO users VALUES (?,?,?)"
            self.__cur.execute(query, (username, passwd, '-'))
            self.__conn.commit()
        except sqlite3.DatabaseError:
            return 'Ошибка БД при создании аккаунта'
        return 'ok'

    def update_account(self, username, new_passwd=''):
        try:
            query = "UPDATE users SET passwd_hash = (?) WHERE username = (?)"
            self.__cur.execute(query, (new_passwd, username))
            self.__conn.commit()
        except sqlite3.DatabaseError:
            return 'Ошибка БД при обновлении пароля'
        return 'ok'

    def delete_account(self, username):
        try:
            query = f"DELETE FROM users WHERE username = (?)"
            self.__cur.execute(query, (username,))
            self.__conn.commit()
        except sqlite3.DatabaseError:
            return 'Ошибка БД при удалении аккаунта'
        return 'ok'

    def update_login_time(self, username):
        try:
            query = "UPDATE users SET last_login = strftime('%Y-%m-%d %H-%M-%S','now') WHERE username = (?)"
            self.__cur.execute(query, (username,))
            self.__conn.commit()
        except sqlite3.DatabaseError:
            return 'Ошибка БД'
        return 'ok'

    def get_login_time(self, username):
        try:
            query = "SELECT last_login FROM users WHERE username = (?)"
            self.__cur.execute(query, (username,))
        except sqlite3.DatabaseError:
            return 'Ошибка БД'
        return self.__cur.fetchone()

    def get_passwd_hash(self, username):
        try:
            query = "SELECT passwd_hash FROM users WHERE username = (?)"
            self.__cur.execute(query, (username,))
        except sqlite3.DatabaseError:
            return 'Ошибка БД'
        return self.__cur.fetchone()

    def close(self):
        self.__conn.close()

    def __del__(self):
        self.__conn.close()
