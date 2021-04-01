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

# 1
user_data = [{'login': 'admin', 'password': '1', 'state': 0}, {'login': 'admin1', 'password': '1', 'state': 1}]


def check_ath(login, password):
    res = [user['login'] for user in user_data if user['login'] == login and user['state'] == 0]
    if len(res) > 0:
        return 0
    else:
        res = [user['login'] for user in user_data if user['login'] == login and user['password'] == password]
        if len(res) > 0:
            return 1
        else:
            return -1

def active_user(login, new_password):
    for i, value in enumerate(user_data):
        print(value['login'])
        if value['login'] == login:
            user_data[i]['state'] = 1
            user_data[i]['password'] = new_password


while True:
    login = input("Enter login:")
    password = input("Enter Password:")
    if check_ath(login, password) == 0:
        new_password = input("Enter new password:")
        active_user(login, new_password)
    if check_ath(login, password) == 1:
        print ('login success')
        break
    if check_ath(login, password) == -1:
        print('Login/password wrong')
        print('Repeat enter login and password ')
