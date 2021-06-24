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


def get_users_dict():
    return {
        'Alexandr': {'password': 'pass', 'active': True},
        'Maria': {'password': 'pass', 'active': True},
        'Marina': {'password': 'pass', 'active': True},
        'Ivan': {'password': 'pass', 'active': False},
        'Nicola': {'password': 'pass', 'active': True},
        'Nadya': {'password': 'pass', 'active': True},
        'Olga': {'password': 'pass', 'active': False}
    }


# Способ через условие Сложность: O(13) - константная
def authorization_elif(username, password):
    result = {'success': False, 'message': ''}   # O(2) - константная
    user_dict = get_users_dict()   # O(1) - константная
    user_data = user_dict.get(username)  # O(1) - константная

    if user_data is None:  # O(1) - константная
        result['message'] = "User doesn't exists"  # O(1) - константная
    elif not user_data['active']:  # O(1) - константная
        result['message'] = "Your account is not activated, please confirm the activation"  # O(1) - константная
    elif password != user_data['password']:  # O(1) - константная
        result['message'] = "Invalid password"  # O(1) - константная
    else:
        result['success'] = True  # O(1) - константная
        result['message'] = f'Welcome, {username}!'  # O(1) - константная

    return result  # O(1) - константная


# Способ через попытку Сложность: O(12) - константная
def authorization_try(username, password):
    result = {'success': False, 'message': ''}  # O(2) - константная
    user_dict = get_users_dict()  # O(1) - константная

    try:  # O(1) - константная
        user_data = user_dict[username]  # O(1) - константная

        if not user_data['active']:  # O(1) - константная
            result['message'] = "Your account is not activated, please confirm the activation"  # O(1) - константная
        elif password != user_data['password']:  # O(1) - константная
            result['message'] = "Invalid password"  # O(1) - константная
        else:
            result['success'] = True  # O(1) - константная
            result['message'] = f'Welcome, {username}!'  # O(1) - константная

    except KeyError:
        result['message'] = "User doesn't exists"

    return result  # O(1) - константная


# Результат работы условного алгоритма
print('====================')
user_doesnt_exist = authorization_elif('Ilya', '123hja123')
print(user_doesnt_exist.get('message'))

print('====================')
not_active_acc = authorization_elif('Ivan', 'pass')
print(not_active_acc.get('message'))

print('====================')
wrong_password = authorization_elif('Maria', 'pass11')
print(wrong_password.get('message'))

print('====================')
success_result = authorization_elif('Alexandr', 'pass')
print(success_result.get('message'))

# Результат работы попыточного алгоритма
print('********************')
user_doesnt_exist = authorization_try('Ilya', '123hja123')
print(user_doesnt_exist.get('message'))

print('********************')
not_active_acc = authorization_try('Ivan', 'pass')
print(not_active_acc.get('message'))

print('********************')
wrong_password = authorization_try('Maria', 'pass11')
print(wrong_password.get('message'))

print('********************')
success_result = authorization_try('Alexandr', 'pass')
print(success_result.get('message'))

# Вывод: Хотя оба варианта имеют константную сложность, считаю оптимальным второй вариант, и.к. там меньшее
# количество константных операций
