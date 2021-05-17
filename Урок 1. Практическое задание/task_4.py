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
# Вариант 1
logins = ["aura94", "sova98", "sweety984", "somebody366", "maylie965", "onlygirls567"]  # O(1)
passwords = ["hgfcvbhjgv5125", "qwsxdcxsde874521", ";lllkmk8lknm", "hgvbnhgv85", "hgvnmjhgv842", "fcvbhjuhgfv"]  # O(1)
if_activated = [True, False, False, True, True, False]  # O(1)


def user_authentication(login, password):
    if login in logins:  # O(n)
        if password in passwords and logins.index(login) == passwords.index(password):  # O(n)
            if if_activated[passwords.index(password)]:  # O(1)
                print("Вы вошли в систему")  # O(1)
            else:
                print("Для входа в систему активируйте учетную запись")  # O(1)
        else:
            print("Неверный пароль. Попробуйте еще раз")  # O(1)
    else:
        print("Пользователя с таким логином нет в системе. Зарегистрируйтесь")  # O(1)


user_authentication("aura94", "hgfcvbhjgv5125")  # O(n)
user_authentication("sova98", "qwsxdcxsde874521")  # O(n)
user_authentication("somebody366", "dfghjmnbvf52541")  # O(n)
user_authentication("onlygirls666", "jhgfvbnjhgb52145")  # O(n)

# Вариант 2
authentication = [["aura94", "hgfcvbhjgv5125"], ["sova98", "qwsxdcxsde874521"],
                  ["sweety984", ";lllkmk8lknm"], ["somebody366", "hgvbnhgv85"],
                  ["maylie965", "hgvnmjhgv842"], ["onlygirls567", "fcvbhjuhgfv"]]  # O(1)


def user_aut(data):
    if data[0] in [n for row in authentication for n in row]:  # O(n^3)
        if data[1] in [n for row in authentication for n in row]:  # O(n^3)
            if data[2]:  # O(n)
                print("Вы вошли в систему")  # O(1)
            else:
                print("Активируйте учетную запись")  # O(1)
        else:
            print("Неверный пароль. Попробуйте еще раз")  # O(1)
    else:
        print("Пользователь не найден. Зарегистрируйтесь")  # O(1)


user_aut(["maylie965", "fcvbhjuhgfv", False])  # O(n)
user_aut(["somebody366", "hgvbnhgv85", True])  # O(n)
user_aut(["sweety984", ";hgbnjuhg", True])  # O(n)
user_aut(["sweety999", ";lllkmk8lknm", False])  # O(n)


"""
Вариант 1 будет наиболее эффективным, так как общая сложность у него О(n), в то время как у Варианта 2 - O(n^3)
"""