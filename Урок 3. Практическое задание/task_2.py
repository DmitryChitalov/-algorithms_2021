import hashlib, binascii, json

"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""


def hash_password(user, password):
    '''Хэширует пароль'''
    password_value = password.encode('utf-8')
    salt_value = user.encode('utf-8')
    obj = hashlib.pbkdf2_hmac(hash_name='sha256',
                              password=password_value,
                              salt=salt_value,
                              iterations=100000)
    result = binascii.hexlify(obj).decode()
    print(f'Хэш пароля - {result}')
    return result


def user_to_file(user, password):
    ''' создает json запись в файл - пользователь и пароль '''

    data = {user: hash_password(user, password)}

    with open('json_base.json', 'r') as f:
        try:
            user_base = json.load(f)
        except:
            user_base = {}  # Если файл изначально пустой, создаем словарь

    with open('json_base.json', 'w') as f:
        user_base.update(data)
        json.dump(user_base, f)  # Перезаписываем обновленный json в файл

    return


def check_user(user, password):

    with open('json_base.json', 'r') as f:
        try:
            user_base = json.load(f)
        except:
            print('База пуста')
    if user_base[user] == hash_password(user, password):
        return True
    else:
        return False


user_enter = input('Введите пользователя: ')
first_pass_enter = input('Введите пароль: ')
user_to_file(user_enter, first_pass_enter)
second_pass_enter = input('Введите пароль повторно: ')

if check_user(user_enter, second_pass_enter):
    print('Пароли совпадают')
else:
    print('Пароли не совпадают')