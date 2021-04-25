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

#1ый вариант - O(n^2) - квадратичная
user_lst = [["bazuka", "3125$#$!!#", True],["Zaec", "%$#%FDS", False],["Volchara", "gfddw111QWERTy", True],
            ["BiCDuck", "ghh4FGDRR", False]]

def security_check(user_data_lst):
    for el in user_lst:
        if el[0] == user_data_lst[0] and el[1] == user_data_lst[1]:
            if el[2] == True:
                return "ok"
            else:
                print("Проблематика с доступом для этого аккаунта")
                return "not_ok"
        else:
            continue
    print("Проблематика с логином или паролем")
    return "not_ok"

user_answer = input("Приветствуем Вас в нашей системе. Для доступа к системе просим ввести Ваш логин и пароль: ")

system_answer = security_check(user_answer.split())

if system_answer == "ok":
    print("Добро пожаловать в систему")
elif system_answer == "not_ok":
    while True:
        user_answer = input("Желаете ли пройти регистрацию? Да/Нет: ")
        if user_answer.lower() == "нет":
            break
        elif user_answer == "да":
            user_answer = input("Введите логин и пароль через пробел: ")
            user_answer2 = user_answer.split()
            user_answer2.append(True)
            print(user_answer2)
            user_lst.append(user_answer2)
            print("Пользователь и пароль успешно добавлены. Добро пожаловать в систему")
            break
            
            
            
#2ой вариант решения: O(N) - линейная
user_dict_name_pass = {"Eren_s_Gori": "Mountains_UP", "Still_moving": "speedUP", "43nie_lives_better": "GOGO_black"}
user_dict_name_acs = {"Eren_s_Gori": True, "Still_moving": False, "43nie_lives_better": True}

def security_check(user_data_lst):
    Func_check = False
    for el in user_dict_name_pass:
        if el == user_data_lst[0]:
            if user_dict_name_pass[el] == user_data_lst[1]:
                if user_dict_name_acs[el] == True:
                    Func_check = True
    return Func_check
user_answer = input("Приветствуем Вас в нашей системе. Для доступа к системе просим ввести Ваш логин и пароль: ")

system_answer = security_check(user_answer.split())

if system_answer == True:
    print("Вход разрешен. Вы в системе")
else:
    while True:
        user_answer = input("Желаете ли пройти регистрацию? Да/Нет: ")
        if user_answer.lower() == "нет":
            break
        elif user_answer.lower() == "да":
            user_answer = input("Введите логин и пароль через пробел: ")
            user_answer2 = user_answer.split()
            user_dict_name_pass[user_answer2[0]] = user_answer2[1]
            user_dict_name_acs[user_answer2[0]] = True
            print(f"Пользователь и пароль успешно добавлены. Добро пожаловать в систему. \n "
                  f"For checking: 1st dict {user_dict_name_pass}\n and 2nd dict {user_dict_name_acs}")
            break

#!!!! Вывод: выбираем вариант решения - по сложности линейная, т.к. для исполнения квадратичной сложности затрачивается
# больше времени на исполнение.
