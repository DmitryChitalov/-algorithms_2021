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
print('Welcome Guest!\n')
profile = ['usr1', 'sss', None]
print(profile)


def user_func():
    print('Welcome Guest!\n')
    profile = ['usr1', 'sss', None]

    user_name = ""  # O(1)
    while not user_name:  # O(N)
        user_name = input('\nUsername:')  # O(1)
        if user_name != profile[0]:  # O(N)
            user_name = input('\a User not found!\nUsername:')  # O(1)
        elif user_name == profile[0]:  # O(N)
            print('ok')
    password = ""  # O(1)
    while not password:  # O(N)
        password = input('\nPassword:')  # O(1)
        if password != profile[1]:  # O(N)
            password = input('\a Wrong password!\nPassword:')  # O(1)
        elif password == profile[1]:  # O(N)
            print('ok')
    user_activation = ""  # O(1)
    while profile[2] is None:  # O(N)
        user_activation = input('Profile not activated!\nFor activation type 1: ')  # O(1)
        if user_activation == '1':  # O(N)
            profile.insert(2, 1)  # O(1)
            print('Profile activated')
        else:
            print('Profile not active')

    if user_name == profile[0] and password == profile[1] and user_activation is not None:  # O(N)
        print('\nWelcome', user_name, '!')
    else:
        print('\nWrong Username or Password.\n Access Denied!')
    return input('\nPress \'Enter\' to continue.')


user_func()  # Получается O(N^9)

""" 2nd """
print('Welcome oh so mighty Guest!\n')
pro_file = ['Zorro', 'qqq', None]
print(pro_file)


def user_1():

    for usr_name in pro_file:  # O(N)
        usr_name = ""  # O(1)
        usr_name = input('Username:')  # O(1)
        if usr_name != pro_file[0]:  # O(N)
            input('User not found, try again!\nUsername:')  # O(1)
        elif usr_name == pro_file[0]:  # O(N)
            print('ok')
            break
    return 'Username accepted!'


def password():

    for pass_word in pro_file:  # O(N)
        pass_word = ""  # O(1)
        pass_word = input('Password:')  # O(1)
        if pass_word != pro_file[1]:  # O(N)
            input('Wrong password, try again!\nPassword:')  # O(1)
        elif pass_word == pro_file[1]:  # O(N)
            print('ok')
            break
    return 'Password Accepted!'


def activation():

    for user_act in pro_file:  # O(N)
        user_act = ""  # O(1)
        user_act = input('Profile not activated!\nFor activation type 1: ')  # O(1)
        if user_act == '1':  # O(N)
            pro_file.insert(2, '1')  # O(1)
            print('Profile activated')
            break
        else:
            print('Profile not active')
    print('\nWelcome: ', pro_file[0], '!')
    return input('\nPress \'Enter\' to continue...')  # O(1)


user_1()
password()
activation()
"""
В этом варианте вышло O(N^8), что дает ему большую скорость
"""