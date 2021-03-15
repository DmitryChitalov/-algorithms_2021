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

import hashlib
import random
import string


def create_random_password(length=12):
    symbols = string.ascii_letters + string.digits + '!#$!&_+-?@^_^' * 2
    password = ''.join(random.choice(symbols) for _ in range(length))
    password_hash = hashlib.md5(password.encode('UTF-8')).hexdigest()
    return password, password_hash


def check_user(dt, login, password):
    """
    O(1)?
    :param dt:
    :param login:
    :param password:
    :return:
    """
    if dt.get(login):
        if dt[login]['password'] == hashlib.md5(password.encode(
                'UTF-8')).hexdigest():  # O(1) + O(1) + (не нашел в сети сложность формирования хэша) = O(1)?
            if dt[login]['active']:  # O(1)
                print(f'Приветствуем Вас, {login}!')
            else:
                if input(f'{login} неактивен, доступ запрещен. Хотите активировать? Y/N: ').lower() == 'y':
                    dt[login]['active'] = True  # O(1)
                    print(f'Учетная запись активирована!\nПриветствуем Вас, {login}!')
                else:
                    print('Досвидания!')
        else:
            print('Указанная пара login/password не совпадают, попробуйте еще раз!')
    else:
        print('Пользователь отсутствует.')


def check_user_second(dt, login, password):
    """
    O(N)
    :param dt:
    :param login:
    :param password:
    :return:
    """
    for row in dt:  # O(N)
        if row == login:
            print(row)
            if dt[row]['password'] == hashlib.md5(password.encode('UTF-8')).hexdigest():
                if dt[login]['active']:  # O(1)
                    print(f'Приветствуем Вас, {login}!')
                else:
                    if input(f'{login} неактивен, доступ запрещен. Хотите активировать? Y/N: ').lower() == 'y':
                        dt[login]['active'] = True  # O(1)
                        print(f'Учетная запись активирована!\nПриветствуем Вас, {login}!')
                    else:
                        print('Досвидания!')
                return
            else:
                print('Указанная пара login/password не совпадают, попробуйте еще раз!')

    print('Пользователь отсутствует.')


def main():
    """
    check_user будет эффективнее т.к использует штатный функционал работы с индексами, а работа с индексами в нотации O-большое равна O(1)
    в отличии от цикла, который равнен O(n)
    :return:
    """
    dt = {}
    for row in range(random.randint(4, random.randint(5, 15))):
        pwd, pwd_h = create_random_password()
        dt[f'user{row}'] = {'password': pwd_h, 'active': True if random.randint(0, 1) else False}
        print(
            f"user{row}: password: {pwd}")  # Для более удобной проверки преподавателю не нарушая базовые правила безопасности по хранению паролей
    print(dt, end='\n')
    login, password = input('Введите, пожалуйста, логин: ').lower(), input('Введите, пожалуйста, пароль: ')
    check_user(dt, login, password)
    check_user_second(dt, login, password)


main()
