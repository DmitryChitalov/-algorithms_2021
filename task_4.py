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

users_list = {'user1': {'password': '123', 'activation': True},
              'user2': {'password': '456', 'activation': True},
              'user3': {'password': '789', 'activation': False},
              'user4': {'password': 'qwer', 'activation': False}
              }


# O(1)
def login_user1(users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password and users[user_name]['activation']:  # O(1)
            return "Доступ разрешон"
        elif users[user_name]['password'] == user_password and not users[user_name]['activation']:  # O(1)
            return "Не активен"
        elif users[user_name]['password'] != user_password:  # O(1)
            return "Неверный пароль"
    else:
        return "Пользователь не существует"


# O(N)
def login_user2(users, user_name, user_password):
    for key, value in users.items():  # O(N)
        if key == user_name:  # O(1)
            if value['password'] == user_password and value['activation']:  # O(1)
                return "Доступ разрешон"
            elif value['password'] == user_password and not value['activation']:  # O(1)
                return "Не активен"
            elif value['password'] != user_password:  # O(1)
                return "Неверный пароль"
    return "Пользователь не существует"


print(login_user1(users_list, 'user1', '123'))
print(login_user2(users_list, 'user3', '1111'))
