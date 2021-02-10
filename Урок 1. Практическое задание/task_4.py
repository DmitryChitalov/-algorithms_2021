"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

# Словарь с логинами и паролями:
logins = {
    'Andrew22 QwErTy': 'offline',
    'Mega_spider_man 22likeWebs22': 'offline',
    'ProUser2000 password123': 'offline',
    'Mike2006 9876543ewq': 'offline'
}


# 1 Способ:
def logging_in(network):
    # Просто проверка логина и пароля
    user_login = input('Input login: ')
    user_password = input('Input password: ')
    login_status = 'Access Denied'
    for i in network:
        i = i.split()
        if i[0] == user_login and i[1] == user_password:
            network.update({f'{user_login} {user_password}': 'online'})
            login_status = 'Access Allowed'
    # Переходим к регистрации
    if login_status == 'Access Denied':
        user_choice = input('There is no user with such login or password\nWould you like to register? (y/n): ')
        while user_choice != 'y' and user_choice != 'n':
            user_choice = input('You can only input "y" or "n": ')
        if user_choice == 'y':
            user_login = input('Input new login: ')
            user_password = input('Input new password: ')
            login_status = 'Successful authentication'
            for i in network:
                i = i.split()
                if user_login == i[0]:
                    login_status = 'Such login already exists!'
            if login_status == 'Successful authentication':
                network.update({f'{user_login} {user_password}': 'offline'})
    return login_status


# print(logging_in(logins))
# print(logins)
'''
Сложность данной функции O(n), так как, не смотря на большую вложнность некоторых операций, наиболее затратной из них
являются циклы, которые, в свою очередь, вложены только в условия с if
'''


# 1.5 Способ (Добавим цикл, чтобы можно было регистрироваться, пока не будут введены корректные данные)
def long_logging_in(network):
    # Просто проверка логина и пароля
    user_login = input('Input login: ')
    user_password = input('Input password: ')
    login_status = 'Access Denied'
    for i in network:
        i = i.split()
        if i[0] == user_login and i[1] == user_password:
            network.update({f'{user_login} {user_password}': 'online'})
            login_status = 'Access Allowed'
    # Переходим к регистрации
    if login_status == 'Access Denied':
        user_choice = input('There is no user with such login or password\nWould you like to register? (y/n): ')
        while user_choice != 'y' and user_choice != 'n':
            user_choice = input('You can only input "y" or "n": ')
        if user_choice == 'y':
            while login_status != 'Successful authentication':
                user_login = input('Input new login: ')
                user_password = input('Input new password: ')
                login_status = 'Successful authentication'
                for i in network:
                    i = i.split()
                    if user_login == i[0]:
                        login_status = 'Such login already exists!'
                        print(login_status)
                if login_status == 'Successful authentication':
                    network.update({f'{user_login} {user_password}': 'offline'})
    return login_status


# print(long_logging_in(logins))
# print(logins)

# Здесь уже сложность равна O(n^2), так как за повторение регистрации отвечает вложенный цикл

'''
Больше способов в голову не пришло, кроме как изменение первого. Но, если рассматривать их оптимальность,
то лучше выбрать способ 1.5, так как, так или иначе, человек, который хочет зарегистрироваться,
будет продорлжать это делать до удачной попытки, и, если реализовывать первую функцию, то ее все равно придется
зацикливать, причем с различными костылями, при этом заново логинясь.
'''