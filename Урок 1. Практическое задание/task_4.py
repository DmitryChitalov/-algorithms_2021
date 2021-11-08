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

""" Структура user_info: user_info = {login:(password, activation)} """
user_info = {'user_1': ('12345', True), 'user_2': ('46789', True), 'user_3': ('97543', False)}

# Решение №1:
# Сложность: О(1)


def user_auth(login, password):
    if login in user_info.keys() and password == user_info[login][0] and user_info[login][1] is True:   # O(1)
        return f'Пользователь {login}, вы авторизованы!'                                                # O(1)
    elif login not in user_info.keys() or password != user_info[login][0]:                              # O(1)
        return f'Извините, мы не можем найти пользователя с введенными логином и паролем. ' \           
               f'Проверьте правильность введенных вами данных.'                                         # O(1)
    else:
        return f'Уважаемый {login}, ваша учётная запись не активирована!'                               # O(1)

# Решение №2:
# Сложность: О(n)


def user_auth1(login, password):
    user_info_lst = list(user_info.items())                                                             # O(n)
    for item in user_info_lst:                                                                          # O(n)
        if item[0] == login and item[1][0] == password and item[1][1] is True:                          # O(1)
            return f'Пользователь {login}, вы авторизованы!'                                            # O(1)
        elif item[0] == login and item[1][0] == password and item[1][1] is False:                       # O(1)
            return f'Уважаемый {login}, ваша учётная запись не активирована!'                           # O(1)

    return f'Извините, мы не можем найти пользователя с введенными логином и паролем. ' \
           f'Проверьте правильность введенных вами данных.'                                             # O(1)


print(user_auth('user_1', '12345'))
print(user_auth('user_2', '46789'))
print(user_auth('user_3', '97543'))
print(user_auth('user_4', '97543'))
print('*' * 50)
print(user_auth1('user_1', '12345'))
print(user_auth1('user_2', '46789'))
print(user_auth1('user_3', '97543'))
print(user_auth1('user_4', '97543'))


"""
Первое решение эффективнее, т.к. не используется цикл.
"""