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
users1 = ({'username':'user1','password':'pass1','active':'yes'},
         {'username':'user2','password':'pass2','active':'no'},
         {'username':'user3','password':'pass3','active':'yes'})

# Решение 1 O(n)
def auth1(login,password):
    for i in users1: # O(n)
        if i['username'] == login and i['active'] == 'yes' and i['password'] == password: # O(1)
            print('Аутентификация успешна!')
            break
        if i['username'] == login and i['active'] == 'no':  # O(1)
            print('Вам необходимо активировать учетную запись!')
            break
        else:
            print('Неверный логин или пароль!')
            break

# Решение 2 O(1) - Лучшее решение, т.к. константная сложность лучше, чем !

users2 = {'user1': {'password': 'pass1', 'active': True},
         'user2': {'password': 'pass2', 'active': False},
         'user3': {'password': 'pass3', 'active': True}}

def auth2():
    login = input('Login: ')
    password = input('Password: ')
    if users2.get(login) is None:
        return print("Login doesn't find!")
    else:
        passwd = users2.get(login).get('password')
        active = users2.get(login).get('active')
        if passwd == password:
            if active == True:
                return print('Logon success!')
            else:
                return print('Account not activated!')
        else:
            return print('Incorrect password!')

auth1('user1','pass1')
auth2()
