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
    'user1': ['pass1', 'active'],
    'user2': ['pass2', 'non-active'],
    'user3': ['pass3', 'active'],
    'user4': ['pass4', 'non-active'],
}


def check_user(login, password):
    """
    Время работы алгоритма составит O(N).
    """
    if login not in users:  # O(N)
        return 'Invalid logn.'  # O(1)
    if users[login][0] != password:  # O(1)
        return 'Incorrect password.'  # O(1)
    if users[login][1] == 'non-active':  # O(1)
        return 'Please, activate you account.'  # O(1)
    return 'Success.'  # O(1)


print(check_user('user1', 'pass1'))
print(check_user('user2', 'pass2'))
print(check_user('user3', 'pass3'))
print(check_user('user4', 'pass1'))
print(check_user('user5', 'pass1'))
print('-' * 30)


def check_user1(login, password):
    """
    Время работы алгоритма составит O(1). Данный алгоритм будет более эффективным так как позволяет
    нам получить преимущество от работы со словарем, и проверить вхождение элемента без обхода.
    """
    if users[login]:  # O(1)
        return 'Invalid logn.'  # O(1)
    if users[login][0] != password:  # O(1)
        return 'Incorrect password.'  # O(1)
    if users[login][1] == 'non-active':  # O(1)
        return 'Please, activate you account.'  # O(1)
    return 'Success.'  # O(1)


print(check_user('user1', 'pass1'))
print(check_user('user2', 'pass2'))
print(check_user('user3', 'pass3'))
print(check_user('user4', 'pass1'))
print(check_user('user5', 'pass1'))
