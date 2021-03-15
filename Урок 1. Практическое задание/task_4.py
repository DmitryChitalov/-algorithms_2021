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

users_list = [
    {'login': 'user1',
     'password': 'password1',
     'status': True},
    {'login': 'user2',
     'password': 'password2',
     'status': True},
    {'login': 'user3',
     'password': 'password3',
     'status': False}
]


# O(N)
def authorization1(login_name, entered_password):
    if login_name in [item['login'] for item in users_list]:                # O(N)
        for item in users_list:                                             # O(N)
            if item['login'] == login_name:                                 # O(1)
                if item['status']:                                          # O(1)
                    if item['password'] == entered_password:                # O(1)
                        return True, 'Login OK'                             # O(1)
                    else:
                        return False, 'Incorrect password'                  # O(1)
                else:
                    return False, 'Account is not active, please activate'  # O(1)
    else:
        return False, 'Login name not found'                                # O(1)


# O(N)
def authorization2(login_name, entered_password):
    account_active = False                                                  # O(1)
    user_exists = False                                                     # O(1)
    password_matches = False                                                # O(1)
    for user in users_list:                                                 # O(N)
        if user['login'] == login_name:                                     # O(1)
            user_exists = True                                              # O(1)
        else:
            continue
        if user['status']:                                                  # O(1)
            account_active = True                                           # O(1)
        else:
            continue
        if user['password'] == entered_password:                            # O(1)
            password_matches = True                                         # O(1)
        else:
            continue
    if not user_exists:                                                     # O(1)
        return False, 'Login name not found'                                # O(1)
    elif not account_active:                                                # O(1)
        return False, 'Account is not active, please activate'              # O(1)
    elif not password_matches:                                              # O(1)
        return False, 'Incorrect password'                                  # O(1)
    else:
        return True, 'Login OK'                                             # O(1)


print(authorization1('user1', 'password1'))
print(authorization1('user2', 'password'))
print(authorization1('user3', 'password3'))
print(authorization1('user4', 'password3'))

print(authorization2('user1', 'password1'))
print(authorization2('user2', 'password'))
print(authorization2('user3', 'password3'))
print(authorization2('user4', 'password3'))

# authorization2 мне кажется более эффетивно, потому что в нем только один O(N)
