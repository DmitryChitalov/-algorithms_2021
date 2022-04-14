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

users_dict = {
    'user1': {'password':'bdjhsjhkjasn', 'activation': True},
    'user2': {'password':'qwertyyy', 'activation': False},
    'user3': {'password':'123456789', 'activation': True},
    'user4': {'password':'wwwweeeee', 'activation': True},
    'user5': {'password':'qwe1234', 'activation': False},
    'user6': {'password':'77777777', 'activation': True},
    'user7': {'password':'qwertyqwerty', 'activation': False},
    'user8': {'password':'123qweqwe', 'activation': True},
}


def authentication1(user_name, password):
    """
    Обращение к полям словаря по ключам занимает константное время.
    Однако первая проверка (not in) зависит от количества ключей в словаре, поэтому сложность данного алгоритма O(N).
    """
    if user_name not in users_dict:
        return "User with this name doesn't exist!"
    elif password != users_dict[user_name]['password']:
        return "Wrong password!"
    elif not users_dict[user_name]['activation']:
        return "You should activate your account before enter!"
    else:
        return "Welcome!"


def authentication2(user_name, password):
    """
    Данный алгоритм работает в 4 раза медленнее, чем предыдущий, и требует больше дополнительной памяти
    на дублирование данных из словаря. Его сложность также O(N).
    """
    logins = list(users_dict.keys())        # O(N)
    passwords = []
    activations = []
    for login in logins:                    # O(N)
        passwords.append(users_dict[login]['password'])
        activations.append(users_dict[login]['activation'])

    if user_name not in logins:             # O(N)
        return "User with this name doesn't exist!"
    else:
        user_index = logins.index(user_name)    # O(N)

    if password != passwords[user_index]:
        return "Wrong password!"
    elif not activations[user_index]:
        return "You should activate your account before enter!"
    else:
        return "Welcome!"


print(authentication1('user4', 'wwwweeee'))
print(authentication2('user4', 'wwwweeee'))

