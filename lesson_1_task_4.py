## Два способа
## Первый - с помощью встроенной функции get получаем пользователя из словаря, алгоритм константа
## Второй - ищем пользователя в цикле - алгоритм линейный за счет цикла

def auth_1(users_dict, user_name, password):
    if users_dict.get(user_name):
        if users_dict[user_name]['password'] == password:
            if users_dict[user_name]['is_active'] == 1:
                return 'доступ разрешен'
            else:
                return 'Необходимо активировать учетку'
        else:
            return 'Неверный пароль'
    else:
        return 'Пользователя не существует'

def auth_2(users_dict, user_name, password):
    for key, value in users_dict.items():
        if key == user_name:
            if value['password'] == password:
                if value['is_active'] == 1:
                    return 'Доступ разрешен'
                else:
                    return 'Необходимо активировать учетку'
            else:
                return 'Неверный пароль'
    else:
        return 'Пользователя не существует'


## Входные данные и вызов функций
users_dict = {
    'user1': {'password': 'paswword1', 'is_active': 1},
    'user2': {'password': 'password2', 'is_active': 0},
    'user3': {'password': 'password3', 'is_active': 1},
    'user4': {'password': 'password4', 'is_active': 0},
    'user5': {'password': 'password5', 'is_active': 1},
    'user6': {'password': 'password6', 'is_active': 0},
            }

print(auth_1(users_dict, 'user2', '1111111'))
print(auth_1(users_dict, 'user3', 'password3'))

print(auth_2(users_dict, 'user5', '1111111'))
print(auth_2(users_dict, 'user6', 'password6'))

