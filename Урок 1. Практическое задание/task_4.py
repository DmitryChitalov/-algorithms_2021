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

user_data = {"aura768": {"password": "sxcvbjuytfcv85", "if_activated": True},
             "sova677": {"password": "jhgfdxcbjgf8749", "if_activated": False},
             "sweety296": {"password": "qwdedswdxs874584", "if_activated": True},
             "flower90": {"password": "jhgfcvbjh85", "if_activated": False},
             "guitar564": {"password": "pollkjhglk9876", "if_activated": True},
             "bomb945": {"password": "ytredcvhjk89652", "if_activated": False}}


# Вариант 1


def authentication(user_bd, login, password):
    if user_bd.get(login):
        if user_bd[login]["password"] == password \
                and user_bd[login]["if_activated"]:
            return "Вы успешно вошли в систему"
        elif not user_bd[login]["if_activated"]:
            return "Для входа активируйте учетную запись"
        elif user_bd[login]["password"] != password:
            return "Пароль введен не верно. Повторите попытку"
    else:
        return "Пользователь не найден. Зарегистрируйтесь"


# Вариант 2


def authentication_2(user_bd, login, password):
    for key, value in user_bd.items():
        if key == login:
            if value["password"] == password and value["if_activated"]:
                return "Вы вошли в систему"
            elif not value["if_activated"]:
                return "Активируйте учетную запись"
            elif value["password"] != password:
                return "Пароль введен не верно. Повторите попытку"

    return "Пользователь не найден. Зарегистрируйтесь"


print(authentication(user_data, "bomb945", "ytredcvhjk89652"))
print(authentication_2(user_data, "bomb945", "ytredcvhjk89652"))
print(authentication(user_data, "aura768", "sxcvbjuytfcv85"))
print(authentication_2(user_data, "sweety296", "qwdedswdxs874584"))
print(authentication(user_data, "somthing768", "oiuyfdcgvhj"))
print(authentication_2(user_data, "mary8765", "poiklok;l85"))
print(authentication(user_data, "guitar564", "uygfvbuhg52"))
print(authentication_2(user_data, "aura768", "kjhgbnmkj"))


"""
Вариант 1 будет эффективнее, так как имеет константную сложность O(1) из-за отсутствия сложных алгоритмов, в то время 
как вариант 2 имеет сложность линейную O(n), так как содержит цикл 
"""