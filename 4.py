my_users = {'user1': {'login': 'Artem','password': '123', 'activation': True},
            'user2': {'login': 'Artem','password': 'abc', 'activation': False},
            'user3': {'login': 'Artem','password': '1717', 'activation': True},
            'user4': {'login': 'Artem','password': '1956', 'activation': False}
            }
# Сложность O(n)
def account1 (users, user, login, user_password) :
    for key, value in users.items():
        if key == user:
            if value['password'] == user_password and value['login']==login and value['activation']:
                return "Добро пожаловать! Доступ к ресурсу предоставлен"
            elif value['password'] == user_password and value['login']==login and not value['activation']:
                return "Учетная запись не активна! Пройдите активацию!"
            elif value['password'] != user_password or value['login']!=login:
                return "Пароль или логин не верный"

    return ( "Данного пользователя не существует" )
print (account1 (my_users ,'user2' ,'Artem' ,'abc'))


#Сложность  O(1)
def account2 (users, user, login, user_password) :
    if users.get(user):
        if users[user]['password'] == user_password and users[user]['activation']:
            return "Добро пожаловать! Доступ к ресурсу предоставлен"
        elif users[user]['password'] == user_password and users[user]['login']==login and not users[user]['activation']:
            return "Учетная запись не активна! Пройдите активацию!"
        elif users[user]['password'] != user_password or users[user]['login']!=login:
            return "Пароль или логин не верный"

    return ( "Данного пользователя не существует" )