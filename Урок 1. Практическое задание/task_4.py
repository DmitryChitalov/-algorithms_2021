"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

# 1. O(1)
database = {
    "admin": {"password": "123321", "activ": True},
    "user": {"password": "123", "activ": False}
    }

user = 'usup'
password = '123'


def check_usr_1(base, user, password):  # O(1)
    try:                                            # O(1)
        if base[user]["password"] == password:      # O(1)
            if base[user]["activ"] == True:         # O(1)
                rez = f"Добрый день {user}"         # O(1)
            else:                                   # O(1)
                rez = f"Добрый день {user}, необходимо актевицировать аккаунт"      # O(1)
        else:                                       # O(1)
            rez = "Password не верный"              # O(1)
    except:                                         # O(1)
        rez = "Login не верный"                     # O(1)
    return rez                                      # O(1)


print(check_usr_1(database, user, password))

# 2. -  O(N)
users_data = {
    'max77': ['#777$grr', 'Maxim', 'Furla', '2.05.1983', '777-777-7777', 0],
    'milochka': ['5898&gwr', 'Mila', 'Watson', '1.03.2001', '222-222-2222', 0],
    'andyra': ['555kl555', 'Andy', 'Mall', '01.08.1990', '555-555-5555', 0]
    }


def check_login(login):                                                 # O(1)
    if login in users_data:                                             # O(N)
        check_pass()                                                    # O(1)
    else:                                                               # O(1)
        print('Login не верный. Пройдите регистрацию.')                 # O(1)


def check_pass():                                                       # O(1)
    i = 0                                                               # O(1)
    while i < 3:                                                        # O(1)
        password = input('Введите password: ')                          # O(1)
        if password == users_data[user_login][0]:                       # O(N)
            users_data[user_login].pop(-1)                              # O(1)
            users_data[user_login].append(1)                            # O(1)
            print("Аккаунт активирован. Добро пажаловать!")             # O(1)
            break                                                       # O(1)
        else:                                                           # O(1)
            i += 1                                                      # O(1)
            print(f'не верный пароль. осталось {(3 - i)} попыток!')     # O(1)


user_login = input('Введите login: ')                                   # O(1)
check_login(user_login)                                                 # O(1)

# 2.1. - O(N**2)


def check_usr_2(login, password):                                           # O(1)
    if login in users_data:                                                 # O(N)
        i = 0                                                               # O(1)
        while i < 3:                                                        # O(1)
            if password == users_data[user_login][0]:                       # O(N)
                users_data[user_login].pop(-1)                              # O(1)
                users_data[user_login].append(1)                            # O(1)
                print("Аккаунт активирован. Добро пажаловать!")             # O(1)
                break                                                       # O(1)
            else:                                                           # O(1)
                i += 1                                                      # O(1)
                print(f'не верный пароль. осталось {(3 - i)} попыток!')     # O(1)
                password = input('Введите password: ')                      # O(1)
    else:                                                                   # O(1)
        print('Login не верный. Пройдите регистрацию')                      # O(1)


user_login = input('Введите login: ')                                        # O(1)
user_password = input('Введите password: ')                                  # O(1)
check_usr_2(user_login, user_password)                                       # O(1)

# 3.


class User:
    def __init__(self, login, password, act):
        self.login = login
        self.password = password
        self.act = act


data_base = [User("login1", "3245", False),
             User("login2", "sgs4", True),
             User("login3", "fsse5343sd", True),
             User("login4", "09i3ojnr3dasd", False)
             ]


def chek_usr_3(db, user_name):                          # 0(N)
    for log in db:                                      # 0(N)
        if log.login == user_name:                      # 0(1)
            if not log.act:                             # 0(1)
                print("Активируйте аккаунт")
            else:                                       # 0(1)
                print("Вход в аккаунт разрешен")
            break                                       # 0(1)
    else:                                               # 0(1)
        print("Пройдите регестрацию")


chek_usr_3(data_base, "login1")

