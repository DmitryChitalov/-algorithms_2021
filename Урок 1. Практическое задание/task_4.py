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
"""первй алгоритм лучше т.к. получение элемента быстрее, чем прохождение по всёму списку пользователей"""
user_data = {"adm": ["111", 1, 1],
             "user": ["111", 1, 0],
             "guest": ["111", 0, 0],
             "login": ["password", 'activate', 'auntefication']  # что где
             }

# 1  O(1)
# password  O(1)
def pass_ok(login, password):
    # print(login, password)
    return 1


# activate O(1)
def activ_proverka(login, flag_activ):
    if flag_activ == 0:
        print(f'пользователь {login} не прошёл активацию!\nhttps://...')
        return 0
    elif flag_activ == 1:
        return 1
    else:
        print("error")
        return -1


# auntefication  O(1)
def auten_proverca(login, flag_aut):
    if flag_aut == 1:
        print(f"пользователь {login} уже вошел в систему!")
        return 1
    elif flag_aut == 0:
        print(f"разрещить вход {login}.")
        return 0
    else:
        print("error")
        return -1

# 1 алгоритм O(1)
while True:
    # login_pass = input("Введите логин и пароль ч/з пробел")  # adm user guest
    login_pass = "guest 111"
    login_pass_list = login_pass.split()
    if pass_ok(login_pass_list[0], login_pass_list[1]) == 1:
        if 1 == activ_proverka(login_pass_list[0], user_data[login_pass_list[0]][1]):
            if 1 == auten_proverca(login_pass_list[0], user_data[login_pass_list[0]][2]):
                pass

    break
print()

# 2 алгоритм O(n)
while True:
    # login_pass2 = input("Введите логин и пароль ч/з пробел")  # adm user guest
    login_pass2 = "adm 111"
    login_pass_list2 = login_pass2.split()
    for i in user_data:
       if i == login_pass_list2[0]:
           if user_data[i][0] == login_pass_list2[1]:
               if user_data[i][1] == 1:
                   #print("активирован")
                   if user_data[i][2] == 0:
                       print(f"Вход {login_pass_list2[0]}.")
                       break
                   else:
                       print(f"пользователь {login_pass_list2[0]} уже вошел в систему!")
                       break

               else:
                   print(f"f'пользователь {login_pass_list2[0]} не прошёл активацию!\nhttps://...'")
                   break
           else:
               print("пароль не тот!")
               break
       else:
           continue

    break