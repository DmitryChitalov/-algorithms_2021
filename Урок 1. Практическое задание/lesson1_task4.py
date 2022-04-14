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

# Первый вариант - сложность O(1)


class Account:
    def __init__(self, login, password, is_active):
        self.login = login
        self.password = password
        self.is_active = is_active


def authenticate(login, password, accounts):  # O(1)
    account = accounts.get(login)
    if account is None:
        return f'No such user {login}'
    if not account.is_active:  # O(1)
        return 'Please activate your account'
    if password != account.password:  # O(1)
        return 'Incorrect password'
    return 'Access granted'


# Второй вариант сложность O(n)


def authenticate_2(login, password, accounts):  # O(n)
    for account in accounts.values():  # O(n)
        if login != account.login:  # O(1)
            continue
        if not account.is_active:  # O(1)
            return 'Please activate your account'
        if password != account.password:  # O(1)
            return 'Incorrect password'
        return 'Access granted'
    return f'No such user {login}'


accounts_list = [Account('jonny', '369', True),
                 Account('Donald_trump', '999', False),
                 Account('lada', '555', True),
                 Account('er_404', '40404', True)]

accounts_dict = {it.login: it for it in accounts_list}

print(authenticate_2('tom', '333', accounts_dict))
print(authenticate_2('lada', '555', accounts_dict))
print(authenticate('lada', '555', accounts_dict))
print(authenticate('tom', '333', accounts_dict))

# Эффективнее будет первое решение со сложность O(n),
# т.к. оно использует словарь, а большинство операций со словарем имеют сложность O(1).