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


users = {
    'user_1': {'pass': '1234', 'account_activated': True},
    'user_2': {'pass': '5678', 'account_activated': True},
    'user_3': {'pass': '9012', 'account_activated': True},
    'user_4': {'pass': '3456', 'account_activated': False},
    'user_5': {'pass': '7890', 'account_activated': True},
    'user_6': {'pass': '1357', 'account_activated': True},
    'user_7': {'pass': '9246', 'account_activated': True},
    'user_8': {'pass': '8014', 'account_activated': False},
    'user_9': {'pass': '7025', 'account_activated': True},
    'user_10': {'pass': '8260', 'account_activated': True},
    'user_11': {'pass': '9876', 'account_activated': True},
    'user_12': {'pass': '5432', 'account_activated': False},
    'user_13': {'pass': '1098', 'account_activated': False}
}

# Вариант 1
# Сложность для функции: O(n)
# Для поиска значений используется конструкция for in, имеющую линейную сложность O(n).


def check_user_for_in(users, user_name, user_pass):
    for key, value in users.items():
        if key == user_name:
            if value['pass'] == user_pass and value['account_activated']:
                return f'Добро пожаловать, {user_name}!'
            elif value['pass'] == user_pass and not value['account_activated']:
                return f'{user_name}, ваша учетная запись не была активирована!\n' \
                       f'Пожалуйста, активируйте свою учетную запись!'
            elif value['pass'] != user_pass:
                return 'Введен неверный пароль!'
    return f'Учетная запись {user_name} не обнаружена.'


# Вариант 2
# Сложность для функции: O(1)
# Для получения значения используется метод get, что дает O(1).


def check_user_get(users, user_name, user_pass):
    if users.get(user_name):
        if users[user_name]['pass'] == user_pass and users[user_name]['account_activated']:
            return f'Добро пожаловать, {user_name}!'
        elif users[user_name]['pass'] == user_pass and not users[user_name]['account_activated']:
            return f'{user_name}, ваша учетная запись не активирована!\n' \
                       f'Пожалуйста, активируйте свою учетную запись!'
        elif users[user_name]['pass'] != user_pass:
            return 'Введен неверный пароль!'
    else:
        return f'Учетная запись {user_name} не обнаружена.'


print(check_user_for_in(users, 'user_1', '1234'))
print(check_user_for_in(users, 'user_1', '1235'))
print(check_user_get(users, 'user_4', '3456'))
print(check_user_get(users, 'user_14', '1234'))

# Вариант 2 предпочтительна, т.к. сложность константная O(1)