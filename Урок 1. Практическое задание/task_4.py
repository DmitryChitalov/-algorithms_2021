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

# линейная сложность


def check_user_n(user_log, name, password):
    for key, value in user_log.items():
        if key == name:
            if value['password'] == password and value['activation']:
                print('Access granted')
            elif value['password'] == password and not value['activation']:
                print('Follow the activation procedure')
            elif value['password'] != password:
                print('Wrong password')
        else:
            print('Wrong name')


# константная сложность


def check_user_const(user_log, name, password):
    if user_log.get(name):
        if user_log[name]['password'] == password and user_log[name]['activation']:
            print('Access granted')
        elif user_log[name]['password'] == password and not user_log[name]['activation']:
            print('Follow the activation procedure')
        elif user_log[name]['password'] != password:
            print('Wrong password')
    else:
        print('Wrong name')
