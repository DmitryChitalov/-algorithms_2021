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
bs_users = {
    'user_01': {'pass': '1234', 'account_activated': True},
    'user_02': {'pass': '1334', 'account_activated': True},
    'user_03': {'pass': '1434', 'account_activated': True},
    'user_04': {'pass': '1534', 'account_activated': False},
    'user_05': {'pass': '1634', 'account_activated': True},
    'user_06': {'pass': '1734', 'account_activated': True},
    'user_07': {'pass': '1834', 'account_activated': True},
    'user_08': {'pass': '1934', 'account_activated': False},
    'user_09': {'pass': '2034', 'account_activated': True},
    'user_10': {'pass': '2134', 'account_activated': True},
    'user_11': {'pass': '2234', 'account_activated': True},
    'user_12': {'pass': '2334', 'account_activated': False}
}

# Вар. 01
# Сложность для функции: O(n)
# Для поиска значений используется перебор данных через конструкцию for in, имеющую линейную сложность O(n).


def check_user_for(users, user_name, user_pass):
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


# Вар. 02
# Сложность для функции: O(1)
# Для получения значения исользуется get, что дает константную сложность (получаем данные сразу).
# Этот вариант наиболее предпочтителен, т.к. имеет наименьшую сложность (константнная VS линейная)
# и соответственно, самую высокую скорость работы.

def check_user_get(users, user_name, user_pass):
    if users.get(user_name):
        if users[user_name]['pass'] == user_pass and users[user_name]['account_activated']:
            return f'Добро пожаловать, {user_name}!'
        elif users[user_name]['pass'] == user_pass and not users[user_name]['account_activated']:
            return f'{user_name}, ваша учетная запись не была активирована!\n' \
                       f'Пожалуйста, активируйте свою учетную запись!'
        elif users[user_name]['pass'] != user_pass:
            return 'Введен неверный пароль!'
    else:
        return f'Учетная запись {user_name} не обнаружена.'


print(check_user_for(bs_users, 'user_01', '1234'))
print(check_user_for(bs_users, 'user_01', '1235'))
print(check_user_get(bs_users, 'user_04', '1534'))
print(check_user_get(bs_users, 'user_14', '1534'))
