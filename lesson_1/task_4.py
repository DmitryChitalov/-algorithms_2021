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


# Сложность O(1)
def autorization_1(users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password and users[user_name]['act'] == 'True':
            return 'Добро пожаловать'
        elif users[user_name]['password'] == user_password and users[user_name]['act'] == 'False':
            return 'Активируйте учетную запись'
        elif users[user_name]['password'] != user_password:
            return 'Введён не верный пароль'
    else:
        return 'Данного пользователя не существует'


# Сложность O(n)
def autorization_2(users, user_name, user_password):
    user_in_users = False
    for user in users:
        if user == user_name:
            user_in_users = True
            if users[user_name]['password'] == user_password and users[user_name]['act'] == 'True':
                return 'Добро пожаловать'
            elif users[user_name]['password'] == user_password and users[user_name]['act'] == 'False':
                return 'Активируйте учетную запись'
            elif users[user_name]['password'] != user_password:
                return 'Введён не верный пароль'

    if not user_in_users:
        return 'Данного пользователя не существует'


if __name__ == '__main__':
    users_dict = {'Alex': {'password': '123', 'act': 'True'},
                  'Pol': {'password': '321', 'act': 'False'}}

    # Тест 1
    test_user = 'Alex'
    test_pass = '123'
    print(autorization_1(users_dict, test_user, test_pass))
    print(autorization_2(users_dict, test_user, test_pass))
    print('\n\n')
    # Тест 2
    test_user = 'Alex'
    test_pass = '111'
    print(autorization_1(users_dict, test_user, test_pass))
    print(autorization_2(users_dict, test_user, test_pass))
    print('\n\n')
    # Тест 3
    test_user = 'Pol'
    test_pass = '321'
    print(autorization_1(users_dict, test_user, test_pass))
    print(autorization_2(users_dict, test_user, test_pass))
    print('\n\n')
    # Тест 4
    test_user = 'Max'
    test_pass = '321'
    print(autorization_1(users_dict, test_user, test_pass))
    print(autorization_2(users_dict, test_user, test_pass))



