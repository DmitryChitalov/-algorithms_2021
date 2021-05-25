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
"""
from random import randint


def user_activation(user_dict):
    """
    сложность O(N)
    Можно прийти к константе, если ограничить кол-во попыток ввода
    """
    while not user_dict['is_activated']:
        random_number = randint(10000, 99999)
        print(f'КОД АКТИВАЦИИ: {random_number}')
        user_input = int(input('Для активации введите изображенное число: '))
        if user_input == random_number:
            user_dict['is_activated'] = True
            print('Учетная запись активирована. Теперь вы можете начать работу с системой')
        else:
            print('Вы ввели неправильное число. Попробуйте снова')


def check_user_activation(user_dict: dict):
    """
    сложность O(1)
    """
    if not user_dict['is_activated']:
        print('Ваша учётная запись Не активирована!')
        return False
    else:
        print('Ваша учётная запись активирована! Можно продолжить работу с системой')
        return True


def authentication(users_data: dict):
    """
    сложность O(N)
    """
    print('У вас три попытки')
    count = 3                                                       # O(1)
    while count != 0:                                               # O(1)
        login = input('Введите имя пользователя: ')                 # O(1)
        if login in users_data.keys():                              # O(1)
            password = input('Введите пароль: ')                    # O(1)
            if password in users_data[login].values():              # O(1)
                if check_user_activation(users_data[login]):        # O(1)
                    print('Welcome')                                # O(1)
                    break                                           # O(1)
                else:                                               # O(1)
                    print('Предлагаю активировать учётную запись!') # O(1)
                    user_activation(users_data[login])              # O(N)
            else:
                print('Неверный пароль!')
        else:
            count -= 1
            print(f'Неверное имя пользователя! Осталось попыток: {count}')


users_dict = \
    {
        'Dave':
            {
                'password': 'mypassword',
                'e-mail': 'my_email@myhost.my',
                'is_activated': False
            },
        'Jameson':
            {
                'password': 'myverystrongpassword)',
                'e-mail': 'is_it_my_email@onmyhost.my',
                'is_activated': True
            }
    }


authentication(users_dict)


def login_in(user_dict: dict):
    """
     Сложность О(1)
    """
    user_login = input('Введите имя пользователя: ')
    if user_dict.get(user_login) and user_dict[user_login][1]:
        user_password = input('Введите пароль: ')
        if user_dict[user_login][0] == user_password:
            print("Welcome!")
        else:
            print("Invalid password!")
    elif user_dict.get(user_login) and not user_dict[user_login][1]:
        print('Ваша учётная запись Не активирована!')
        if len(input('Для активации введите любой символ: ')) > 0:
            user_dict[user_login][1] = True
            print('Активация выполнена!')
        else:
            print('Видимо оно вам не нужно...')
    else:
        print("Вы ввели неверное имя пользователя")


user_data = {
    'Dave': ['mypassword', False],
    'Jameson': ['myverystrongpassword', True]
}

login_in(user_data)

# Вывод:
# По расчётам вторая функция предпочительнее, но внешний вид решения мне не нравится.
# Первый алгоритм, при некторой доработке можно привести к сложности О(1)
