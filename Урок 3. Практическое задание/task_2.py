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


def authorization():
    login = input('Введите логин: ')
    passwd = input('Введите пароль: ')
    dict = load_dict_from_file()
    if login in dict:
        if hashlib.sha256(login.encode() + passwd.encode()).hexdigest() == dict[login]:
            print('Вы авторизованы')
        else:
            print('Пароль не совпадает. Попробуйте ещё раз')
    else:
        if input(f'Пользователя {login} не существует. Создать? (y)') == 'y':
            dict[login] = hashlib.sha256(login.encode() + passwd.encode()).hexdigest()
            save_dict_to_file(dict)


def save_dict_to_file(dic):
    """Функция сохранения словаря в файл"""
    with open('authorization.txt', 'w') as file:
        file.write(str(dic))


def load_dict_from_file():
    """Функция загрузки словаря из файла"""
    with open('authorization.txt', 'r') as file:
        data = file.read()
    return eval(data)


authorization()
