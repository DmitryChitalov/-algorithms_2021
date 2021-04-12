import sqlite3


class Storage:
    def __init__(self):
        self.__conn = sqlite3.connect("users.db")
        self.__cur = self.__conn.cursor()
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS users
                              (passwd_hash text PRIMARY KEY, last_login text)
                           """)

    def close(self):
        self.__conn.close()

    def get_account(self, passwd):
        query = f"SELECT last_login FROM users WHERE passwd_hash = {passwd}"
        self.__cur.execute(query)
        return self.__cur.fetchone()

    def create_account(self, passwd):
        query = f"INSERT INTO users VALUES ('{passwd}', '-')"
        temp_exec = self.__cur.execute(query)
        print('create_account', temp_exec)
        self.__conn.commit()

    def update_account(self, prev_passwd, new_passwd=''):
        if new_passwd == '':
            query = f"UPDATE users " \
                    f"SET last_login = strftime('%Y-%m-%d %H-%M-%S','now') " \
                    f"WHERE passwd_hash = '{prev_passwd}'"
        else:
            query = f"UPDATE users " \
                    f"SET passwd_hash = '{new_passwd}' " \
                    f"WHERE passwd_hash = '{prev_passwd}'"
        temp = self.__cur.execute(query)
        print('update_account', temp)
        self.__conn.commit()

    def delete_account(self, passwd):
        query = f"DELETE FROM users WHERE passwd_hash = {passwd}'"
        temp = self.__cur.execute(query)
        print('delete_account', temp)
        self.__conn.commit()

    def __del__(self):
        self.__conn.close()
