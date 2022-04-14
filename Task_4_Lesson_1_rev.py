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
# Вариант 1
# Хранилище реализовано в 2-х словарях (1 - логин-пароль, 2 - логин-информация об актиации)
# Общая сложность: O(n)

users = {
    '1': '1',
    'login_1': 'pass_1',
    'login_2': 'pass_2',
    'login_3': 'pass_3',
    'login_4': 'pass_4'
}

users_activation = {
    '1': True,
    'login_1': True,
    'login_2': False,
    'login_3': False,
    'login_4': False
}


def users_checking(user_login):
    user_pass = input('Please, input a password ')  # программа будет предлагать пользователю ввести пароль до верного
    while user_pass != 'q':                                                                        # O(n)
        if user_pass == users.get(user_log):                                                       # O(1)
            if users_activation.get(user_log):  # проверка активации                               # O(1)
                print('Access is allowed.')                                                        # O(1)
                break                                                                              # O(1)
            else:                                                                                  # O(1)
                print('Access is denied, please, activate your account.')                          # O(1)
                break                                                                              # O(1)
        else:                                                                                      # O(1)
            print('Access is denied, please, check the password.')                                 # O(1)
            user_pass = input('Please, input a password: ')                                        # O(1)


print('Welcome. If you want to quit, input "q"')                                                   # O(1)
# пользователь может прервать активацию в любой момент
user_log = input('Please, input your login ')  # для запуска функции проверяем логин               # O(1)
while user_log != 'q':                                                                             # O(n)
    if user_log in users:                                                                          # O(n)
        users_checking(user_log)                                                                   # O(1)
        break                                                                                      # O(1)
    else:                                                                                          # O(1)
        print('Sorry, user with this login do not exist, please check login ')                     # O(1)
        user_log = input('Please, input your login ')                                              # O(1)
print('*' * 50)


# Вариант 2
# Общая сложность O(1)
def user_checking_2(users_dict, user_name, user_password):
    if users_dict.get(user_name):                                                                  # O(1)
        if users_dict[user_name]['password'] == user_password \
                and users_dict[user_name]['activation']:                                           # O(1)
            return 'Пароль верен. Добро пожаловать.'                                               # O(1)
        elif users_dict[user_name]['password'] == user_password \
                and not users_dict[user_name]['activation']:                                       # O(1)
            return 'Учётная запись не аквтивирована! Пройдтите активацию!'                         # O(1)
        elif users_dict[user_name]['password'] != user_password:                                   # O(1)
            return 'Пароль неверный'                                                               # O(1)
    else:                                                                                          # O(1)
        return f'Пользователя {user_name} не существует.'                                          # O(1)


my_users = {'user1': {'password': '111111', 'activation': True},
            'user2': {'password': '222222', 'activation': False},
            'user3': {'password': '333333', 'activation': True},
            'user4': {'password': '444444', 'activation': False}
            }
print(user_checking_2(my_users, 'user1', '111111'))
print(user_checking_2(my_users, 'user5', '111111'))
# Вывод: вторая реализация эффективнее, т.к. в ней не используется цикл, сложность O(1)
