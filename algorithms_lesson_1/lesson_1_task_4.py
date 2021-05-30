#РЕШЕНИЕ 1: сложность O(N) 

def data_check_1(user_data, user_login, user_password):
    for el in user_data:
        if user_data['login'] == user_login:
            if user_data['password'] == user_password and user_data['is_activated']:
                return 'Welcome! Access to the resource is open'
            elif user_data['password'] == user_password and not user_data['is_activated']:
                return 'You should activate your account'
            elif user_data['password'] != user_password:
                return 'Wrong password!'
    return 'No such user'


# РЕШЕНИЕ 2: сложность O(1)
def data_check_2(user_data, user_login, user_password):
    if user_data['login'] == user_login:
        if user_data['password'] == user_password \
                and user_data['is_activated']:
            return 'Welcome! Access to the resource is open'
        elif user_data['password'] == user_password \
                and not user_data['is_activated']:
            return 'You should activate your account'
        elif user_data['password'] != user_password:
            return 'Wrong password!'
    else:
        return 'No such user'


user_data = {'login': 'John', 'password': '0830', 'is_activated': True}
user_login = input('Enter login: ')
user_password = input('Enter password: ')

print(data_check_1(user_data, user_login, user_password))
print(data_check_1(user_data, user_login, user_password))

# ВЫВОД: 2-е решение лучше, т.к. его сложность меньше, чем у 1-го благодарая отсутствию цикла. 
