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
# Users DB
users = {
    "lge0617": {"password": "VLa;W1:K", "activated": 1},
    "bzc0579": {"password": "z}g!V)2k", "activated": 0},
    "pqb8530": {"password": "wH#$|4s?", "activated": 1},
    "hnz6513": {"password": "e9JBI<.5", "activated": 0},
    "tsh9357": {"password": "0;n~B'MP", "activated": 0},
    "ldw2123": {"password": "{(]K=F2l", "activated": 0},
    "kyk2459": {"password": "yzXw]|/>", "activated": 0},
    "boh0156": {"password": "wPNzA73F", "activated": 0},
    "imp3956": {"password": "^?u62]Vo", "activated": 1},
    "jvi7839": {"password": "]h|?XML:", "activated": 0},
}


def auth_v1(login: str, passwrd: str):
    """
    Обработка аутентификации. При необходимости предлагается активация, либо создание новой учётной записи.

    Сложность: O(1)

    ВЫВОД: Этот алгоритм, очевидно, эффективнее, потому что мы не используем цикл для поиска логина, а пользуемся
        встроенными функциями словаря, сложность которых константна.

    :param login: имя учётной записи
    :param passwrd: пароль
    :return: True при успешной аутентификации, иначе False
    """
    if login in users.keys() and users.get(login).get('password') == passwrd:
        if users.get(login).get('activated'):
            print(f"Welcome, {login}!")
            return True
        else:
            if input("Your account isn't actevated! Please write the word 'activate':") == 'activate':
                print(f"Welcome, {login}! Your account gracefully activated!")
                return True
            else:
                print("Failed activation! Come back later!")
                return False
    else:
        register = input(f"There is no login '{login}'! Are you agree to register as new user? (y/n)[n]: ") == 'y'
        if register:
            users[login] = {"password": passwrd, "activated": 0}
            print("Your account has created! Please, activate!")
            return False
        else:
            print("We haven't create an account for you!")
            return False


def auth_v2(login: str, passwrd: str):
    """
    Обработка аутентификации. При необходимости предлагается активация, либо создание новой учётной записи.

    Сложность: O(n)

    :param login: имя учётной записи
    :param passwrd: пароль
    :return: True при успешной аутентификации, иначе False
    """
    for user_login in users.keys():
        if login == user_login and users[login]['password'] == passwrd:
            if users[login]['activated']:
                print(f"Welcome, {login}!")
                return True
            else:
                if input("Your account isn't actevated! Please write the word 'activate':") == 'activate':
                    print(f"Welcome, {login}! Your account gracefully activated!")
                    return True
                else:
                    print("Failed activation! Come back later!")
                    return False
    else:
        register = input(f"There is no login '{login}'! Are you agree to register as new user? (y/n)[n]: ") == 'y'
        if register:
            users[login] = {"password": passwrd, "activated": 0}
            print("Your account has created! Please, activate!")
            return False
        else:
            print("We haven't create an account for you!")
            return False


if __name__ == '__main__':
    inpt = input("Enter your login and password separated by a space. For break enter ': br': ")
    login, pwd = inpt.split(' ')
    while inpt != ': br' and not auth_v2(login, pwd):
        inpt = input("Enter your login and password separated by a space. For break enter ': br': ")
        login, pwd = inpt.split(' ')
