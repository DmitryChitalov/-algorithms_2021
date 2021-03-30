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

import hashlib as hh
# universal password: testtest

user_list = {
    "vasiliy": "0cfcf7ed735fed225ecec79d4d38ec6e",
    "terkin": "0433f98198191d66f875c4c7657c71f7",
    "some_guy": "96d56f4a5dc544db34b91d72322e159b"
}

logged_in_user_list = []


def hash_it(login_str, pass_str):
    res = hh.md5((login_str + pass_str).encode())
    res_hash = res.hexdigest()
    return res_hash


def user_pass_gen():
    for k in user_list.keys():
        res = hh.md5((k+"testtest").encode())
        print(k, ":", res.hexdigest())
        hash_it(k, "testtest")

# user_pass_gen()


# get all logged in users
# complexity:
def getInUsers():
    return logged_in_user_list


# if user is logged in
# complexity:
def ifUserLoggedin(u_name):
    return u_name in logged_in_user_list


def loggin_function():
    flag = True
    while flag:
        u_login = input("Hello, who are you? (input your login): ")
        if u_login.lower() == "stop":
            flag = False
        elif u_login.lower() in logged_in_user_list:
            som_inp = input("You are already logged in the system, if you want out, type exit: ")
            if som_inp.lower() == "exit":
                logged_in_user_list.remove(u_login)
        elif u_login.lower() not in user_list.keys():
            answer = input("You are not in access list, do you want to create an account? (Yes/No): ")
            if answer.lower() == "yes" or answer.lower() == "y":
                flag2 = True
                while flag2:
                    u_pass1 = input("type in your password:")
                    u_pass2 = input("repeat you password please:")
                    # #### getpass not working properly, cannot echo off the console
                    # print("type in your password:")
                    # u_pass1 = getpass()
                    # print("repeat you password please:")
                    # u_pass2 = getpass()
                    if u_pass1.lower() == u_pass2.lower():
                        flag2 = False
                        user_list[u_login.lower()] = hash_it(u_login.lower(), u_pass1.lower())
                    else:
                        print("Something went wrong! your password do not match, please try again")
        else:
            u_pass = input("type in your password:")
            if hash_it(u_login.lower(), u_pass.lower()) == user_list[u_login.lower()]:
                logged_in_user_list.append(u_login.lower())
                # redirect for the rest of the app should be here
            else:
                print("Try again:")


loggin_function()

