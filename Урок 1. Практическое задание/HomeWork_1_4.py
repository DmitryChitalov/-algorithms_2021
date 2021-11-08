# 1st O(1)

def accept_user(login_name, password):
    if not login_name in users_dict:
        print('Пожалуйста пройдите регистрацию на сайте')
    elif users_dict[login_name][1] == 'accept' and users_dict[login_name][0] == password:
        print('Добро пожаловать в личный кабинет')
    else:
        print('Пожалуйста пройдите регистарцию на сайте')

users_dict = {
    'ilya': ['qwerty', 'accept'],
    'balalayka': ['muzika', 'accept'],
    'noname': ['nopassword', 'cansel']
    }

login = input()
password = input()

accept_user(login, password)

