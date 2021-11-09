
users = {'user_login_1': {'password': 'user_password_1', 'status': True},
         'user_login_2': {'password': 'user_password_2', 'status': False}
         }

# O(n) - Линейная сложность

"""
ВЫВОД
Сложность данного алгоритма растет прямо пропорционально изменению 
количеству элементов в массиеве, что является
наименее эффективной в сравнении с константной сложностью
"""


def check_auth_1(login, password):
    for key, value in users.items():
        if key == login:
            if value['password'] == password and value['status']:
                return 'Вход выполнен успешно!'
            elif value['password'] != password:
                return 'Неверный пароль!'
            elif value['password'] == password and not value['status']:
                return 'Активируйте ваш профиль!'
    return 'Пользователь не найден'


# O(1) - сложность константная
"""
ВЫВОД
Данная сложность эффективнее, т.к. скорость выполнения этого алгоритма не зависит от длины массива. 
"""


def check_auth_2(login, password):
    if not users.get(login):
        return 'Пользователь не найден!'
    if not users.get(login).get('password') == password:
        return 'Неверный пароль!'
    if not users.get(login).get('status'):
        return 'Активируйте ваш профиль!'
    return 'Вход выполнен успешно!'


print(check_auth_1('user_login_1', 'user_password_1'))
print(check_auth_1('user_login_1', 'user_pass'))
print(check_auth_1('user_login_2', 'user_password_2'))
print(check_auth_1('user_log', 'user_password_1'))

print(check_auth_2('user_login_2', 'user_password_2'))
print(check_auth_2('user_login_1', 'user_password_1'))
print(check_auth_2('user_login_2', 'user_pass'))
print(check_auth_2('user_log', 'user_password_2'))
