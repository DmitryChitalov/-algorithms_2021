import sqlite3


class Storage:
    def __init__(self):
        self.__conn = sqlite3.connect("users.db")
        self.__cur = self.__conn.cursor()
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS users
                              (username text PRIMARY KEY, passwd_hash blob, last_login text)
                           """)

    def create_account(self, username, passwd):
        query = f"INSERT INTO users VALUES (?,?,?)"
        self.__cur.execute(query, (username, passwd, '-'))
        self.__conn.commit()
        return 'ok'

    def update_account(self, username, new_passwd=''):
        if new_passwd == '':
            query = f"UPDATE users " \
                    f"SET last_login = strftime('%Y-%m-%d %H-%M-%S','now') " \
                    f"WHERE username = '{username}'"
        else:
            query = f"UPDATE users " \
                    f"SET passwd_hash = '{new_passwd}' " \
                    f"WHERE username = '{username}'"
        self.__cur.execute(query)
        self.__conn.commit()

    def delete_account(self, username):
        query = f"DELETE FROM users WHERE username = {username}'"
        temp = self.__cur.execute(query)
        print('delete_account', temp)
        self.__conn.commit()

    def get_last_login(self, username):
        query = f"SELECT last_login FROM users WHERE username = '{username}'"
        self.__cur.execute(query)
        return self.__cur.fetchone()

    def get_passwd_hash(self, username):
        query = f"SELECT passwd_hash FROM users WHERE username = '{username}'"
        self.__cur.execute(query)
        return self.__cur.fetchone()

    def __del__(self):
        self.__conn.close()
