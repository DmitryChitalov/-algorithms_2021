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
"""
# Сложность: O(1)
def authentication_1(database, u_login, u_password):
    if database.get(u_login):
        if database[u_login]['password'] == u_password:
            if database[u_login]['is_activated'] == True:
                return 'Доступ предоставлен'
            elif database[u_login]['is_activated'] == False:
                return 'Для получения доступа необходимо выполнить активацию учетной записи'
            else:
                return 'Нет данных об активации Вашей учетной записи. Обратитесь в техподдержку'
        elif database[u_login]['password'] != u_password:
            return 'Неверный пароль'
    else:
        return 'Неверный логин'

# Сложность: O(n)
def authentication_2(database, u_login, u_password):
    for key, value in database.items():
        if key == u_login:
            if value['password'] == u_password:
                if value['is_activated'] == True:
                    return 'Доступ предоставлен'
                elif value['is_activated'] == False:
                    return 'Для получения доступа необходимо выполнить активацию учетной записи'
                else:
                    return 'Нет данных об активации Вашей учетной записи. Обратитесь в техподдержку'
            elif value['password'] != u_password:
                return 'Неверный пароль'
    return 'Неверный логин'


base_users = {
    'login_1': {'password': '111', 'is_activated': True}
    , 'login_2': {'password': '222', 'is_activated': True}
    , 'login_3': {'password': '333', 'is_activated': 2}
    , 'login_4': {'password': '444', 'is_activated': False}
}

print(authentication_1(base_users, 'login_1', '111'))
print(authentication_2(base_users, 'login_1', '111'))
print(authentication_1(base_users, 'login_2', '111'))
print(authentication_2(base_users, 'login_2', '111'))
print(authentication_1(base_users, 'login_3', '333'))
print(authentication_2(base_users, 'login_3', '333'))
print(authentication_1(base_users, 'login_4', '444'))
print(authentication_2(base_users, 'login_4', '444'))
print(authentication_1(base_users, 'login_5', '555'))
print(authentication_2(base_users, 'login_5', '555'))
