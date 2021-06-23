# Решение O(n)
users = {'user1': {'password': 'password1', 'active_flag': True},
         'user2': {'password': 'password2', 'active_flag': False},
         'user3': {'password': 'password3', 'active_flag': True}
         }


def user_check(username, password):
    for key, index in users.items():
        if key == username:
            if index['password'] == password and index['active_flag']:
                return f'{username} вошел в систему'
            elif index['password'] == password and not index['active_flag']:
                return f'Для {username} необходимо активировать учетную запись'
            elif index['password'] != password:
                return f'Для {username} введен неверный пароль'
    return f'Пользователя {username} не существует'


print(user_check('user1', 'password1'))
print(user_check('user2', 'password2'))
print(user_check('user3', 'password3'))
print(user_check('user', 'password'))

# Решение O (1)
users = {'user1': {'password': 'password1', 'active_flag': True},
         'user2': {'password': 'password2', 'active_flag': False},
         'user3': {'password': 'password3', 'active_flag': True}
         }


def user_check(username, password):
    if username in users:
        if users[username]['password'] == password and users[username]['active_flag']:
            return f'Пользователь {username} вошел в систему'
        if users[username]['password'] != password:
            return f'Пользователь {username} ввел не верный пароль'
        if users[username]['password'] == password and not users[username]['active_flag']:
            return f'Пользователь {username} активируйте учетную запись'
    return f'Пользователь {username} не зарегистрирован'


print(user_check('user1', 'password1'))
print(user_check('user2', 'password'))
print(user_check('user2', 'password2'))
print(user_check('user7', 'password'))

# Еще одно решение O(1)
users = {'user1': {'password': 'password1', 'active_flag': True},
         'user2': {'password': 'password2', 'active_flag': False},
         'user3': {'password': 'password3', 'active_flag': True}
         }


def user_check(username, password):
    if users.get(username):
        if users[username]['password'] == password and users[username]['active_flag']:
            return f'Пользователь {username} вошел в систему'
        if users[username]['password'] != password:
            return f'Пользователь {username} ввел не верный пароль'
        if users[username]['password'] == password and not users[username]['active_flag']:
            return f'Пользователь {username} активируйте учетную запись'
    return f'Пользователь {username} не зарегистрирован'


print(user_check('user1', 'password1'))
print(user_check('user2', 'password'))
print(user_check('user2', 'password2'))
print(user_check('user7', 'password'))

# Лушее решение - О(1), т.к. оно быстрее.
