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


def authentication_1():                              # O(2n), но фактически число попыток ограничено
    username = input('Введите имя пользователя')
    password = input('Введите пароль')
    attempt_username = 0
    attempt_password = 0
    attempt_activation = 0
    while True:                                                                               # O(n)
        if attempt_username == 4 or attempt_password == 4:                                    # O(1)
            return 'Вы превысили число попыток'
        username = username.lower()                                                           # O(1)
        password = password                                                                   # O(1)
        if not users.get(username):                                                           # O(1)
            print(f'Пользователь с таким именем не найден. Осталось попыток: {3 - attempt_username}')
            attempt_username += 1                                                             # O(1)
            username = input('Введите имя еще раз')                                           # O(1)
        elif password != users.get(username)[0]:                                              # O(1)
            print(f'Пароль введен не верно. Осталось попыток: {3 - attempt_password}')
            attempt_password += 1                                                             # O(1)
            password = input('Попробуйте еще раз')                                            # O(1)
        else:
            break
    if not users.get(username)[1]:                                                            # O(1)
        answer = input('Ваш аккаунт еще не активирован. Желаете его активировать?\ny - Да\nn - Нет')  # O(1)
        while True:                                                                           # O(n)
            if attempt_activation == 4:                                                       # O(1)
                return 'Вы превысили число попыток'
            answer = answer.lower()                                                           # O(1)
            if answer == 'y':                                                                 # O(1)
                users.update({username: [password, 1]})                                       # O(1)
                return f'Ваш аккаунт успешно активирован. Добро пожаловать {username}.'       # O(1)
            elif answer == 'n':                                                               # O(1)
                return 'Вы сможете активировать аккаунт в любой момент.'                      # O(1)
            else:
                print(f'Вы ошиблись в букве. Осталось попыток: {3 - attempt_activation}')
                attempt_activation += 1                                                       # O(1)
                answer = input('Ваш аккаунт еще не активирован. Желаете его активировать?\ny - Да\nn - Нет')  # O(1)
    return f'Добро пожаловать {username}.'                                                    # O(1)


def authentication_2(username, password):                                              # O(1)
    if users.get(username):                                                            # O(1)
        if password == users.get(username)[0] and users.get(username)[1]:              # O(1)
            return f'Добро пожаловать {username}.'
        elif password == users.get(username)[0] and not users.get(username)[1]:        # O(1)
            return f'Пройдите активацию аккаунта'
        elif password != users.get(username)[0]:                                       # O(1)
            return f'Пароль введен не верно'
    else:
        return f'Пользователь с таким именем не найден.'                               # O(1)


users = {
    'alpha@mail.ru': ['sdgg4433sd', 1],
    'bravo1': ['d65gv1sdg1', 0],
    'charlie@mail.ru': ['df6gg3', 1],
    'alphadestroyer': ['qwerty', 1],
    'echo': ['3dfb11', 1],
    'dancinglover': ['fg5d1fg31', 0],
    'golf@mail.ru': ['4iogyk3', 1],
    'hotel_nirvana': ['besthotel', 1],
    'india': ['fwerh653', 0]
}

print(authentication_1())

username_2 = input('Введите имя пользователя').lower()
password_2 = input('Введите пароль')
print(authentication_2(username_2, password_2))


""" Теоретически проще функция authentication_2, но на практике я бы использовал более медленный вариант 
authentication_1, т.к. он позволяет польтзователю предпринять несколько попыток ввода данных без перезагрузки
приложения.
"""
