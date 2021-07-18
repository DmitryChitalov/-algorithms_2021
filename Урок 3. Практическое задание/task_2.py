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


# Усложнил

def store_the_pass(login, paswrd=None):
    """Turn login and pass for cheking, or login for insert data into database"""

    dbh = sqlite3.connect('C:\\Users\\dkozi\\OneDrive\\Документы\\paswrds.db')
    sth = dbh.cursor()
    if not paswrd and sth.execute("SELECT password, salt FROM pshash WHERE login=?", [login]).fetchall():
        _all = sth.execute("SELECT password, salt FROM pshash WHERE login=?", [login]).fetchall()
        s = _all[0][0]
        v = _all[0][1]
        print('В базе данных хранится строка: ', s)
        print('Вы ввели правильный пароль' if hashlib.sha256(v.encode() +
                                                             input("Введите пароль еще раз для проверки: ").encode(
                                                                 'UTF-8')).hexdigest() == s else "Введенный пароль "
                                                                                                 "неверен")
        return
    else:
        try:
            salt = uuid4().hex
            sth.execute("INSERT INTO pshash (login, password, salt) VALUES (?, ?, ?)",
                        (login, hashlib.sha256(salt.encode() + paswrd.encode('UTF-8')).hexdigest(), salt))
            dbh.commit()
            return
        except sqlite3.IntegrityError:
            print('This login is already at use')
            return


if __name__ == '__main__':
    import sqlite3
    import hashlib
    from uuid import uuid4

    store_the_pass('deniskozin', '123')
    store_the_pass('deniskozin')
    store_the_pass('deniskozin', '453')
    store_the_pass('kozindenis', 'aaaaa')
    store_the_pass('kozindenis')
