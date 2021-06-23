# coding=utf8
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

import mysql.connector
from sqlalchemy import create_engine
import pandas as pd


def get_passwd_lst_bd(col='passwd'):
    con = mysql.connector.connect(user='user', passwd='any', database='ido')
    sql = pd.read_sql(f'SELECT {col} FROM users', con)
    return sql


def get_passwd():
    passwd = input('Введите пароль: \n')
    salt_id = max(get_passwd_lst_bd('id')['id']) + 1
    salt = f'{salt_id}kulebyaka'                    # Соль- вероятность повторения низкая. привязка к id пользователя
    result = bytes(f"{passwd}{salt}", encoding='utf-8')
    print(result)
    result = hashlib.sha3_256(result).hexdigest()
    print(result)
    return result


def get_df(diction):
    df = pd.DataFrame([diction], columns=diction.keys())
    return df


def update_db(df):
    passwd = input('Введи свой админовский пароль: \n')
    # Создать соединение и указать кодировку
    con = mysql.connector.connect(user='root', passwd=passwd, database='ido')
    engine = create_engine(f'mysql://root:{passwd}@localhost/ido?charset=utf8', echo=True)

    # Записать датафрейм в базу поверх данных с заменой (replace). Можно писать в конец имеющейся таблицы ('append')
    # index=False - признак того, что индекс не участвует в качестве данных.
    df.to_sql('users', con=engine, if_exists='append', index=False)
    # Контроль таблицы
    sql = pd.read_sql('SELECT * FROM users', con)
    print(sql)


def registration():
    last_name = input('Введите Вашу фамилию: \n')
    first_name = input('Введите Ваше имя: \n')
    patronymic = input('Введите Ваше отчетсво: \n')
    email = input('Укажите email: \n')
    phone = input('Укажиет телефон контакта: \n')

    def validation_pass():
        passwd = get_passwd()
        print('Для проверки пароля введите его еще раз. \n')
        passwd_2 = get_passwd()
        if passwd == passwd_2:
            if passwd not in get_passwd_lst_bd():
                result = {'last_name': last_name, 'first_name': first_name, 'patronymic': patronymic,
                          'email': email, 'phone': phone, 'passwd': passwd}
                update_db(get_df(result))
            else:
                print("Выберите другой пароль, этот слишком простой")
                validation_pass()
        else:
            print('Пароль не совпадает. Введите пароль заново')
            validation_pass()
    validation_pass()


registration()

