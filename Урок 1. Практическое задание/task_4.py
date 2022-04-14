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

# Вариант 1:
users_auth = {('user1', '1111'): 'aсtivated',
              ('user2', '1111'): 'aсtivated',
              ('user3', '1111'): 'non-aсtivated'
             }


def pass_user_authorization(dict_obj, tuple_obj):
    """
    Сложность линейная O(N) доминирующая
    """
    keys_lst = dict_obj.keys()  # O(1)
    if tuple_obj in keys_lst:  # O(N) ЗАВИСИТ ОТ ДЛИНЫ СПИСКА
        if dict_obj[tuple_obj] == 'aсtivated':
            return 'authorization passed'  # O(1)
        else:
            return 'the account is not activated! for activating your account click on the link below: '  # O(1)
    else:
        return 'authorization failed! incorrect login or password!'  # O(1)


print(pass_user_authorization(users_auth, ('user1', '1111')))
print(pass_user_authorization(users_auth, ('user3', '1111')))
print(pass_user_authorization(users_auth, ('user2', '0000')))

# Вариант 2:
users_auth_1 = [[{'user1': '1111'}, 'aсtivated'], [{'user2': '1111'}, 'non-aсtivated']]


def pass_user_authorization_1(list_obj, lgn, psw):
    """
    Сложность квадратичная O(N^2)  доминирующая
    """
    for i in range(len(list_obj)):  # O(N^2)  для вложенных циклов
        for l, p in list_obj[i][0].items():
            if l == lgn and p == psw:  # O(1)
                if list_obj[i][1] == 'aсtivated':  # O(1)
                    return 'authorization passed'  # O(1)
                else:
                    return 'the account is not activated! for activating your account click on the link below: ' # O(1)
            else:
                return 'authorization failed! incorrect login or password!'  # O(1)


print(pass_user_authorization_1(users_auth_1, 'user1', '1111'))
print(pass_user_authorization_1(users_auth_1, 'user1', '0000' ))
print(pass_user_authorization_1(users_auth_1, 'user2', '1111'))

# Вариант 3:

def pass_user_authorization_2(users_dict, lgn, psw):
    """
    Сложность константная O(1)  доминирующая
    """
    if users_dict.get(lgn): # O(1)
        if users_dict[lgn]['password'] == psw and users_dict[lgn]['activation'] is True:  # O(1)
            return 'authorization passed'  # O(1)
        elif users_dict[lgn]['password'] == psw and users_dict[lgn]['activation'] is False: # O(1)
            return 'the account is not activated! for activating your account click on the link below: '  # O(1)
        elif users_dict[lgn]['password'] != psw:
            return 'authorization failed! incorrect password!'  # O(1)
    else:
        return 'there is no such user!'  # O(1)


users_auth_2= {'user_1':{'password':'00000', 'activation': True},
               'user_2':{'password':'11111', 'activation': False}
              }

print(pass_user_authorization_2(users_auth_2, 'user_1', '00000'))
print(pass_user_authorization_2(users_auth_2, 'user_1', '11111'))
print(pass_user_authorization_2(users_auth_2, 'user_2', '11111'))


# Вывод: вариант 3 решения более эффективен, чем варианты 1 и  2, так как его сложность константная,
# и при росте числа пользователей ресурсозатратность не изменится в отличии от
# первых двух вариантов.