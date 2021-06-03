"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""
import hashlib

def db_data_inserting(table_name):
    pass


def db_data_reading(users, hashed_user_data):
    pass

def data_hashing(hashed_data: list):
        hashed_data[1] = hashlib.sha256(hashed_data[0].encode() + hashed_data[1].encode()).hexdigest()
        return hashed_data


def entering_user_data():
    new_login = input('Enter your username: ')
    user_password = input('Enter password: ')
    user_data = [new_login, user_password]
    return user_data



def user_registration():
    """
    User registration function
    """
    print('To register, enter your username and password.')
    new_user_data = entering_user_data()
    return new_user_data


def user_authentication():
    print('To enter your username and password.')
    hashed_user_data = data_hashing(entering_user_data())
    if db_data_reading('users', hashed_user_data[0]) == hashed_user_data[1]:
        return True
    elif db_data_reading('users', hashed_user_data[0]) is None:
        return False


user_choice = None
while user_choice != '0':
    user_choice = input('Enter \n "1" To register a user, \n '
                         '"2" To login:')
    if user_choice == '1':
        user_registration()
    elif user_choice == '2':
        if user_authentication():
            print(print('Authorization was successful! Welcome!'))
            user_choice = '0'
        else:
            print('Username or password is incorrect!')
    else:
        print('Input is incorrect')
