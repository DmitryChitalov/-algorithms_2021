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


# Функция линейная, согласно нотации О большого: сложность - O(n)
def authentication(profiles, login, password):
    for key, value in profiles.items():
        if key == login:
            if value['password'] == password and value['activation']:
                return "Welcome!"
            elif value['password'] == password and not value['activation']:
                return "This user is not activated, please retry"
            elif value['password'] != password:
                return "The password is incorrect, please retry"
    return "This user is not signed up"


user_list = {
    'Paul': {'password': '111', 'activation': True},
    'Andrew': {'password': '222', 'activation': True},
    'John': {'password': '333', 'activation': True},
    'Tom': {'password': '444', 'activation': False},
    'Ford': {'password': '555', 'activation': False}
    }

print(authentication(user_list, input('Enter your login: '), input('Enter your password: ')))
