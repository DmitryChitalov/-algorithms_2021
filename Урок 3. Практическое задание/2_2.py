import hashlib


def registration():
    login = input('введите логин: ')
    password = input('введите пароль: ')
    result = hashlib.sha256(login.encode() + password.encode()).hexdigest()
    with open('hesh_fr', 'r', encoding='utf_8') as check:
        for data in check:
            if data == result:
                return print('Вы уже есть в системе')
            else:
                with open('hesh_fr', 'w', encoding='utf_8') as record:
                    record.write(result)
                return print('Вы зарегестрировались')


def entrance():
    login_1 = input('введите логин: ')
    password_1 = input('введите пароль: ')
    result_2 = hashlib.sha256(login_1.encode() + password_1.encode()).hexdigest()
    with open('hesh_fr', 'r', encoding='utf_8') as check_2:
        for data_2 in check_2:
            if result_2 == data_2:
                print('Вы вошли в систему')
            else:
                print('Пароль или логин не совпадают '
                      'Попробуйте еще раз')
                entrance()


registration()
entrance()
