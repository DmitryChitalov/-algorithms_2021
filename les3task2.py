import hashlib

def hash_making(login, password):
    hash_obj = hashlib.sha256((login.encode() + password.encode()))
    hex_res = hash_obj.hexdigest()
    return login, hex_res


def get_hash():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    hash1 = hash_making(login, password)
    print(f'Hash: {hash1}')
    print("Введите запрашиваемые данные еще раз: ")
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    hash2 = (login, password)

    if hash1 == hash2:
        print('Данные совпали. Доступ предоставлен')
    else:
        print('Вы ввели неверные данные! Доступ не предоставлен')


get_hash()
