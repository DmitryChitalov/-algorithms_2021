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

# общая сложность О(n)
def user_avtorization(users, user_name , user_pasword ):
    for key, value in users.items():
        if key == user_name:
            if ['pasword'] == user_pasword and value['active']:
                return "Доступ активирован"
            elif ['pasword'] == user_pasword and not value['active']:
                return "Пройдите авторизацию"
            elif value['pasword'] != user_pasword:
                return "Не верный пароль"
    return "Пользователя не существует"



#общая сложность О(1)
def user_avtorization2(users, user_name , user_pasword ):
    if users.get(user_name):
        if users[user_name]['pasword'] == user_pasword and users[user_name]['active']:
            return "Доступ активирован"
        elif users[user_name]['pasword'] == user_pasword and not users[user_name]['activ']:
            return "Пройдите авторизацию"
        elif users[user_name]['pasword'] != user_pasword:
            return "Не верный пароль"
    else:
        return "Пользователя не существует"
