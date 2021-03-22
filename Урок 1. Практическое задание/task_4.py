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

# Сложность: O(1)


def user_logon_1(user_dict):
    user_login = input("Insert Your login: ").lower()
    if user_dict.get(user_login) and user_dict[user_login][0] == 1:
        user_pass = input("Insert Your password: ")
        if user_dict[user_login][1] == user_pass:
            print("Welcome!")
        else:
            print("Invalid password!")
    elif user_dict.get(user_login) and user_dict[user_login][0] == 0:
        print("Your account is disabled!")
    else:
        print("User not found!")


# Сложность: O(n)


def user_logon_2(user_dict):
    user_login = input("Insert Your login: ").lower()
    user_not_found = True
    for i in user_dict:
        if i == user_login and user_dict[user_login][0] == 1:
            user_not_found = False
            user_pass = input("Insert Your password: ")
            if user_dict[user_login][1] == user_pass:
                print("Welcome!")
            else:
                print("Invalid password!")
        elif i == user_login and user_dict[user_login][0] == 0:
            user_not_found = False
            print("Your account is disabled!")
    if user_not_found:
        print("User not found!")


db_user = {"alex": [1, "12345678"],
           "sam": [0, "qwerty1"],
           "terminator": [1, "Qld@8v%bne"]}

user_logon_1(db_user)
print()
user_logon_2(db_user)

"""
Вывод:
Первый вариант является предпочтительным, так как он является константным в О-нотации.
Его скорость не будет зависеть от размерность входных данных.
Во втором варианте присутствует цикл for с переменной, который подразумевает линейность в О-нотации.
"""