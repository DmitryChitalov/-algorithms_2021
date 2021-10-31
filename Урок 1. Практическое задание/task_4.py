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

profiles ={
    'Roman': {'password': '123',
              'activation': True},
    'Sergey': {'password': '0000',
              'activation': False},
    'Dmitriy': {'password': '1111',
              'activation': True}
}


def check_login(profiles, name, password):
    for key, val in profiles.items():
        if name == key:
            if val['password'] == password and val['activation'] == True:
                return 'Доступ разрешён'
            elif val['password'] == password and val['activation'] == False:
                return 'Пройдите активацию'
            else:
                return 'Не верный пароль'
    else:
        return 'Не верный логин'

# O(N)
print(check_login(profiles, 'Sergey', '0000'))


def check_login2(profiles, name, password):
    if profiles[name] == name:
        if profiles[name]['password'] == password and profiles[name]['activations'] == True:
            return 'Доступ разрешён'
        elif profiles[name]['password'] == password and profiles[name]['activations'] == False:
            return 'Пройдите аутентификацию'
        else:
            return 'Не верный пароль'
    else:
        return 'Не верный логин'

# O(1)
print(check_login(profiles, 'Roman', '123'))