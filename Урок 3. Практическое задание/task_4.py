"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
import hashlib
import sqlite3


def url_save(url):
    conn = sqlite3.connect("algorithm_pass.db")
    cursor = conn.cursor()
    cursor.execute("""drop table if exists my_cash""")
    cursor.execute("""CREATE TABLE if not exists my_cash
                              (
                              url varchar(255),
                              cash varchar (300)
                              )
                       """)
    salt = url[:2]
    do_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    all_db = cursor.execute('Select url from my_cash')
    # print(all_db.fetchall())
    for i in all_db:
        if url in i:
            return f'{url=} уже есть в кэш'

    cursor.execute('insert into my_cash (url, cash) values ("{}","{}")'.format(url, do_hash))
    conn.commit()
    add = cursor.execute("select * from my_cash where url like '{}'".format(url))
    return f'{add.fetchall()}'


while True:
    # url_save('https://')
    print(url_save(input('https://')))



