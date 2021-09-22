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


######################################
# O(n)

def sign_in(login, password):
    if login in users.keys() and users[login] == password and is_activate[login] is True:  # O(n)
        print('Sign in is successful!')
    elif login not in users.keys():  # O(n)
        print('Please create a new account!')
    elif users[login] != password:  # O(1)
        print('Your password is incorrect!')
    elif is_activate[login] is False:  # O(1)
        print('Your account is not activated, please check your email')


#######################################
# O(1)

def sign_in_2(login, password):
    if users.get(login):  # O(1)
        if users[login] == password:  # O(1)
            if is_activate[login]:  # O(1)
                print('Sign in is successful!')
            else:
                print('Your account is not activated, please check your email')
        else:
            print('Your password is incorrect!')
    else:
        print('Please create a new account!')


users = {
    'Gector': '28336279',
    'Bobr': '1276579',
    'Pussy': 'weytuy4'
}

is_activate = {
    'Gector': True,
    'Bobr': True,
    'Pussy': False
}

sign_in('Gector', 'user6')
sign_in('Pussy', 'weytuy4')
sign_in_2('Gector', 'user6')
sign_in_2('Pussy', 'weytuy4')
