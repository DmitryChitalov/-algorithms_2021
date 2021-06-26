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


users_data = {'user_1': 'we3432dfwe4', 'user_2': '3ewqww3', 'user_3': '12ewqdasd34', 'user_4': '12ewqd34',
              'user_5': '12ewqdaasd34', 'user_6': 'ds234efsf', 'user_7': '12ewqd34', 'user_8': '12ewqd34',
              'user_9': 'we3432ddsfwe4', 'user_10': '3ewqwxzzcw3', 'user_11': '12ewsd34', 'user_12': '12edswqd34'}

users_activity = {'user_1': True, 'user_2': True, 'user_3': False, 'user_4': False, 'user_5': True, 'user_6': True,
                  'user_7': False, 'user_8': False, 'user_9': True, 'user_10': True, 'user_11': True, 'user_12': False}


def check_access_1(user, passwd):
    """
    return O(1) Constant time
    """
    if users_activity.get(user) is not False:  # O(n) Linear Time
        if users_data.get(user) == passwd:
            print(f"{user}, Welcome to aboard!")
        else:
            print(f"Please, {user}, check the password")
    else:
        print(f"{user}, Access denied. Do you want activate your account?")


def check_access_2(user, passwd):
    """
    return O(1) Constant time
    """
    for key_activity in users_activity.keys():  # O(n) Linear time
        if key_activity == user:
            _active = users_activity.get(user)  # O(1) Constant time
            if _active is False:
                return f'{user}, Access denied. Do you want activate your account?'
            else:
                for key_passwd in users_data.keys():
                    if key_passwd == user:
                        _key_passwd = users_data.get(user)
                        if _key_passwd == passwd:
                            return f'{user}, Welcome to aboard'
                        else:
                            return f'Please, {user}, check your password'


check_access_1('user_1', '23442w')
check_access_1('user_7', 'r22wer')

print(check_access_2('user_1', 'we3432dfwe4'))
print(check_access_2('user_7', 'fdee21'))
