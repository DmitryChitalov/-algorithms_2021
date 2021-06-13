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
users_auth = {('fghfj47', 'gdhsjg5*'): 'aсtivated', ('fgth781', 'ghdh783#'): 'aсtivated',
              ('fghjw', 'FGvj56+9'): 'aсtivated', ('aljd5', '$e6tHJJG'): 'non-aсtivated',
              ('yhxa88', 'TjjsdT-4%'): 'aсtivated', ('Fghf-11', 'gkfY*iT1!'): 'non-aсtivated'}


def pass_user_authorization(dict_obj, tuple_obj):
    """
    Сложность линейная O(N) доминирующая
    """
    keys_lst = dict_obj.keys()  # O(1)
    if tuple_obj in keys_lst:  # O(N) ЗАВИСИТ ОТ ДЛИНЫ СПИСКА
        if dict_obj[tuple_obj] == 'aсtivated':  # O(1)
            return 'authorization passed'  # O(1)
        else:
            return 'the account is not activated! for activating your account click on the link below: '  # O(1)
    else:
        return 'authorization failed! incorrect login or password!'  # O(1)


print(pass_user_authorization(users_auth, ('fgth781', 'ghdh783#')))
print(pass_user_authorization(users_auth, ('fghfj47', 'ghdgh7*')))
print(pass_user_authorization(users_auth, ('aljd5', '$e6tHJJG')))

# Вариант 2:
users_auth_2 = [[{'fgw': 'F+9'}, 'aсtivated'], [{'a5': '*9G'}, 'non-aсtivated']]


def pass_user_authorization_1(list_obj, lgn=input('enter your login: '), psw=input('enter your password: ')):
    """
    Сложность квадратичная O(N^2)  доминирующая
    """
    for i in range(len(list_obj)):  # O(N^2)  для вложенных циклов
        for l, p in list_obj[i][0].items():
            if l == lgn and p == psw:  # O(1)
                if list_obj[i][1] == 'aсtivated':  # O(1)
                    return 'authorization passed'  # O(1)
                else:
                    return 'the account is not activated! for activating your account click on the link below: '  # O(1)

    return 'authorization failed! incorrect login or password!'  # O(1)


print(pass_user_authorization_1(users_auth_2))

# Вывод: вариант 1 решения более эффективен, чем вариант 2, так как его сложность линейная,
# и при росте числа пользователей затраты ресурсов сервера будут расти прямо пропорционально их числу, а во 2 варианте -
# затраты ресурсов сервера будут расти прямо пропорционально квадрату их числа.

