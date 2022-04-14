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

users = {'user_1': {'password': '12345', 'authentication': True},
         'user_2': {'password': '11111', 'authentication': False},
         'user_3': {'password': '54321', 'authentication': True}
         }

# Сложность: # O(n) - линейная
def check_user_1(login, password, users):
    if login in users.keys():                                                           # O(n) - линейная
        if password == users[login]['password']:                                        # O(1) - константная
            if users[login]['authentication']:                                          # O(1) - константная
                print('Вход выполнен')                                                  # O(1) - константная
            else:
                print('Учетная запись не активированна. Подтвердите свои данные')       # O(1) - константная
        else:
            print('Неверный пароль')                                                    # O(1) - константная
    else:
        print("Пользователь с данным логином не существует")                            # O(1) - константная

check_user_1('user_1', '12345', users)


# Сложность: # O(n) - линейная
def check_user_2(login, password, users):
    for el in users:                                                                    # O(n) - линейная
        if el == login:                                                                 # O(1) - константная
            if password == users[login]['password']:                                    # O(1) - константная
                if users[login]['authentication']:                                      # O(1) - константная
                    return 'Вход выполнен'                                              # O(1) - константная
                else:
                    return 'Учетная запись не активированна. Подтвердите свои данные'   # O(1) - константная
            else:
                return 'Неверный пароль'                                                # O(1) - константная
    return 'Пользователь с данным логином не существует'                                # O(1) - константная

print(check_user_2('user_2', '11111', users))

"""Оба варианта решения с линейной сложностью"""





