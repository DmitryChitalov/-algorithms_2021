"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

users = {'user_1': {'password': '1234', 'activated': True},
         'user_2': {'password': '2345', 'activated': True},
         'user_3': {'password': '3456', 'activated': False},
         'user_4': {'password': '4567', 'activated': True},
         'user_5': {'password': '5678', 'activated': False},
         'user_6': {'password': '6789', 'activated': False},
         'user_7': {'password': '7890', 'activated': True}}


def authentication_1(users_dict, user_login, user_password):  # Сложность  O(n)
    for u, i in users_dict.items():
        if u == user_login:
            if (i.get('password') == user_password) and i.get('activated'):
                return 'Доступ разрешён!'
            elif (i.get('password') == user_password) and not i.get('activated'):
                return 'В доступе отказано! Активируйте учётную запись!'
        else:
            return 'В доступе отказано! Не верный пароль.'
    else:
        return 'В доступе отказано! Не верный логин.'


def authentication_2(users_dict, user_login, user_password):  # Сложность  O(n^2)
    for u in users_dict.keys():
        if u == user_login:
            for i in users_dict.values():
                if (i.get('password') == user_password) and i.get('activated'):
                    return 'Доступ разрешён!'
                elif (i.get('password') == user_password) and not i.get('activated'):
                    return 'В доступе отказано! Активируйте учётную запись!'
            else:
                return 'В доступе отказано! Не верный пароль.'
    else:
        return 'В доступе отказано! Не верный логин.'



print(authentication_1(users, 'user_1', '1234'))
print(authentication_2(users, 'user_1', '1234'))
print(authentication_2(users, 'user_3', '3456'))

#  Первое решение эффективней, т.к. сложность его решения в нотации О-большое меньше.
