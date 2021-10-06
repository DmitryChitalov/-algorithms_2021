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
# O(n)


users = [
    {'login': 'qwerty1', 'password': 'qwerty1', 'is_active': True},
    {'login': 'qwerty2', 'password': 'qwerty2', 'is_active': True},
    {'login': 'qwerty3', 'password': 'qwerty3', 'is_active': False},
    {'login': 'qwerty4', 'password': 'qwerty4', 'is_active': False}
]

def function_O_n(login, password):
    for user in users:
        if user['login'] == login:
            if user['password'] == password:
                if user['is_active']:
                    print('Пользователь авторизован и допущен к ресурсу')
                    exit()
                else:
                    a = input('Ваша учетная запись не активирована. Для активации нажмите "1"')
                    if a == "1":
                        user['is_active'] = True
                        print('Пользователь авторизован и допущен к ресурсу')
                    exit()
            else:
                print('Неверный пароль.')
                exit()
    print('Пользователь не зарегестрирован, пройдите авторизацию')


#function_O_n('qwerty3', 'qwerty3')

users_1 = {
    'qwerty1': {'password': 'qwerty1', 'is_active': True},
    'qwerty2': {'password': 'qwerty2', 'is_active': True},
    'qwerty3': {'password': 'qwerty3', 'is_active': False},
    'qwerty4': {'password': 'qwerty4', 'is_active': False}
}


# O(1) Этот код быстрее, но нужно было изменить хранение данных, чтобы не вводить цикл

def function_O_1(login, password):
    if login in users_1:
        user = users_1[login]
        if user['password'] == password:
            if user['is_active']:
                print('Пользователь авторизован и допущен к ресурсу')
                exit()
            else:
                a = input('Ваша учетная запись не активирована. Для активации нажмите "1"')
                if a == "1":
                    user['is_active'] = True
                    print('Пользователь авторизован и допущен к ресурсу')
                exit()
        else:
            print('Неверный пароль.')
            exit()
    print('Пользователь не зарегестрирован, пройдите авторизацию')


function_O_1('qwerty3', 'qwerty5')

