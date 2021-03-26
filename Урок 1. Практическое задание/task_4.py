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
# O(1)
users = {'Maga': ['123', True],
         'Baga': ['124', False]
         }


def user_auth_1(login, password):
    if users.get(login):
        return users[login][0] == password and users[login][1]

    return False


print(user_auth_1('Maga', '123'))
print(user_auth_1('Baga', '124'))

# ############################################################################################
# O(n)
users_2 = [{'Name': 'Vasya', 'Password': 123, 'Authorization': True},
           {'Name': 'Dusya', 'Password': 123, 'Authorization': False}]


def user_auth_2(Name):
    for i in users_2:
        if Name == i['Name']:
            if i['Authorization']:
                return "Вы вошли"
            else:
                if input('Введите пароль') == i['123']:
                    i['Hello'] = 'True'
                    return "Отлично"
                else:
                    return "Не верный пароль"
    return "Необходимо зарегестрироваться"


print(user_auth_2('Vasya'))
print(user_auth_2('Dusya'))

'''Первое решение является более эффективным так как сложность такого алгоритма константная, а значит быстрее'''
