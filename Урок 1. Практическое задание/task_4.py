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


import random

lst = ['none active', 'active']

logins = ([
    {'user_1': 'Egor'},
    {'user_2': 'Makar'},
    {'user_3': 'Makar'},
    {'user_4': 'Egor'},
    {'user_5': 'Maksim'},
    {'user_6': 'Kolya'}])

passwords = ([
    {'user_1': 'ajjtgsg'},
    {'user_2': 'hfgjfjhsjf'},
    {'user_3': 'ghkdgkg'},
    {'user_4': 'ghjkdgk'},
    {'user_5': 'ghkdtkj4'},
    {'user_6': 'ghkghkdert'}])


access_to_activation = ([
    {logins[0].get('user_1'): lst[random.randint(0, 1)]},
    {logins[1].get('user_2'): lst[random.randint(0, 1)]},
    {logins[2].get('user_3'): lst[random.randint(0, 1)]},
    {logins[3].get('user_4'): lst[random.randint(0, 1)]},
    {logins[4].get('user_5'): lst[random.randint(0, 1)]},
    {logins[5].get('user_6'): lst[random.randint(0, 1)]}])


def accession_on_site(lst_passwords, lst_access_to_activation):

"""
	Сложность: O(n^2).

"""
    login_insert = int('Vvedite login')             #O(1)
    for i in range(len(lst_access_to_activation)):         #O(n)
        for key in lst_access_to_activation[i]:           #O(n)
            if login_insert == key:                        #O(1)
                if lst_access_to_activation[i].items() == 'active':           #O(1)
                    password_insert = int('Vvedite password')                  #O(1)
                    if lst_passwords[i].items() == password_insert:               #O(1)
                        return f'Privet, {login_insert}, dostup active'             #O(1)
                    elif lst_passwords[i].items() == password_insert:              #O(1)
                        return f'{login_insert}, parol ne vernyi'                  #O(1)
                elif lst_access_to_activation[i].items() == 'none active':          #O(1)
                    return 'Vash login ne active'                                    #O(1)
            elif login_insert != key:                                                  #O(1)
                return 'Takogo logina net'                                               #O(1)


accession_on_site(passwords, access_to_activation)

################################################################################

def authorization_site(users, user_name, user_password):

"""
	Сложность: O(1).

"""
    if users.get(user_name):                                 #O(1)
        if users[user_name]['password'] == user_password and users[user_name]['activation']:    #O(1)
            return f'Q, {user_name}, dostup active'                                              #O(1)
        elif users[user_name]['password'] == user_password and not users[user_name]['activation']:    #O(1)
            return f'Q, {user_name}, sorry dostup none active'                                         #O(1)
        elif users[user_name]['password'] != user_password:                                           #O(1)
            return f'Q, {user_name}, sorry password ne tot'                                            #O(1)
    else:
        return "Usera takogo net"                                                                     #O(1)


authorization_site(lst_users, lst_user_name, lst_user_password)
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""