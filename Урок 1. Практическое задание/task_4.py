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


accounts_dict = {'activated': {'a': 1, 'b': 2, 'c': 3}, 'not_activated': {'d': 4, 'e': 5, 'f': 6}}

"""
O(n), тк все проверки со сложностью O(1), а перебор по словарю со сложностью O(n)
"""
def autentification_1(login, password, accounts_dict_1):
    for key, value in accounts_dict_1.items():
        if login in value and key == 'activated':
            if value[login] == password:
                print("You are able to use the service!")
                break
            if value[login] != password:
                print("Incorrect password!")
                break
        if login not in value and key == 'not_activated':
            print("Account not activated. You should activate it.")
        print("No such user!")
        break

# проверка
# autentification_1('a', 1, accounts_dict)
# autentification_1('a', 2, accounts_dict)
# autentification_1('t', 1, accounts_dict)



"""
O(n^2) потому что два цикла (вложенные), каждый O(n)
"""

def autentification_2(login, password, accounts_dict_2):
    for key, value in accounts_dict_2.items():
        for i in value:
            if i == login and key == 'activated':
                if value[i] == password:
                    print("You are able to use the service!")
                    break
                if value[i] != password:
                    print("Incorrect password!")
                    break
            if i == login and key == 'not_activated':
                print("Account not activated. You should activate it.")
                break
        print("No such user!")
        break
# проверка
# autentification_2('a', 1, accounts_dict)
# autentification_2('a', 2, accounts_dict)
# autentification_2('t', 1, accounts_dict)


# 1) 2 решения сверху
# 2) оценено над каждой из функций
# 3) первое решение эффективнее, так как линейная функция возрастает медленнее, чем квадратичная (которая образуется
#    во второй функции из-за вложенного цикла)