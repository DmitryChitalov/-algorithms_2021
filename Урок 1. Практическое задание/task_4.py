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


# O(1) Процедура не имеет цикла, а значит имеет константную сложность, поэтому она эффективнее.
def authorization_1(name, login, password):
    if users[name][0] == login and users[name][1] == password and users[name][2] == True:       # O(1)
        return 'Доступ разрешён!'                                                               # O(1)
    elif users[name][0] == login and users[name][1] == password and users[name][2] == False:    # O(1)
        return 'Пройдите активацию!'                                                            # O(1)
    elif users[name][0] != login or users[name][1] != password:                                 # O(1)
        return 'Проверьте логин и пароль!'                                                      # O(1)

# O(n)
def authorization_n(name, login, password):
    for key, value in users.items():                                                # O(n)
        if key == name:                                                             # O(1)
            if value[0] == login and value[1] == password and value[2] == True:     # O(1)
                return 'Доступ разрешён!'                                           # O(1)
            elif value[0] == login and value[1] == password and value[2] == False:  # O(1)
                return 'Пройдите активацию!'                                        # O(1)
            elif value[0] != login or value[1] != password:                         # O(1)
                return 'Проверьте логин и пароль!'                                  # O(1)


users = {'User1': ('juke', 'password', True),
         'User2': ('uire', 'password2', True),
         'User3': ('ewue', 'password3', False)}

print(authorization_1('User1', 'juke', 'password'))
print(authorization_1('User2', 'uirke', 'password2'))
print(authorization_1('User3', 'ewue', 'password3'))

print(authorization_n('User1', 'juke', 'password'))
print(authorization_n('User2', 'uirke', 'password2'))
print(authorization_n('User3', 'ewue', 'password3'))
