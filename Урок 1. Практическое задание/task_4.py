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


def authorization(username, password, user_list):
    result = {'success': False, 'message': ''}

    user_data = user_list.get(username)

    if user_data is None:
        result['message'] = "User doesn't exists"
    elif not user_data.get('active'):
        result['message'] = "Your account is not activated, please confirm the activation"
    elif not password == user_data.get('password'):
        result['message'] = "Invalid password"
    else:
        result['success'] = True
        result['message'] = f'Welcome, {username}!'

    return result


users_dict = {
    'Alexandr': {'password': 'pass', 'active': True},
    'Maria': {'password': 'pass', 'active': True},
    'Marina': {'password': 'pass', 'active': True},
    'Ivan': {'password': 'pass', 'active': False},
    'Nicola': {'password': 'pass', 'active': True},
    'Nadya': {'password': 'pass', 'active': True},
    'Olga': {'password': 'pass', 'active': False}
}
print('====================')
user_doesnt_exist = authorization('Ilya', '123hja123', users_dict)
print(user_doesnt_exist.get('message'))

print('====================')
not_active_acc = authorization('Ivan', 'pass', users_dict)
print(not_active_acc.get('message'))

print('====================')
wrong_password = authorization('Maria', 'pass11', users_dict)
print(wrong_password.get('message'))

print('====================')
success_result = authorization('Alexandr', 'pass', users_dict)
print(success_result.get('message'))
