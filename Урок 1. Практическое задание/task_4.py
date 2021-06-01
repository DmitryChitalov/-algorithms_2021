""" Домашнее задание к уроку №1 курс Алгоритмы и структуры данных на Python
    студент: Максим Сапунов Jenny6199@yandex.ru
    27.05.2021
"""


# Задание 4.
#    Для этой задачи:
#    1) придумайте 2-3 решения (не менее двух)
#    2) оцените сложность каждого решения в нотации О-большое
#    3) сделайте вывод, какое решение эффективнее и почему
#    Сама задача:
#    Пользователи веб-ресурса проходят аутентификацию.
#    В системе хранятся логин, пароль и отметка об активации учетной записи.
#    Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
#    При этом его учетка должна быть активирована.
#    А если нет, то польз-лю нужно предложить ее пройти.
#    Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
#    Для реализации хранилища можно применить любой подход,
#    который вы придумаете, например, реализовать словарь.
#    Примечание:
#    Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
#    через строки документации в самом коде.
#    Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
#   Задание творческое. Здесь нет жестких требований к выполнению.


class Variant1:
    """ Представление процедуры регистрации пользователя в системе
    Сложность выражений данного алгоритма на большем его протяжении константная, лишь при переборе значений
    словаря сталкиваемся с линейной сложностью. Таким образом общая сложность данного варианта O(N).
    """

    user_db = {
        'Maksim': ['test001', True],
        'Oleg': ['test002', False],
        'Michail': ['test003', True]
    }

    @staticmethod
    def get_login():
        """Функция аутентификации пользователя"""
        print('\033[31m Hi, everywhere!\n For continue - please, Sign_In or Register: ')
        print('\033[0m Enter Your name, than press Enter', end=' : ')
        login = input()
        if login in Variant1.user_db.keys():
            print(f'Welcome back, {login}!')
            if Variant1.check_status(login):
                Variant1.get_password(login)
            else:
                print('You need to get access from system administrator!')
                return
        else:
            print(f'\033[31m {login}, you are not in user list. Please, get registration.')
            Variant1.get_registration()

    def get_password(login: str):
        """Функция проверки пароля"""
        i = 1
        while i < 4:
            print('\033[31m Insert password', end=' : ')
            password = input()
            if password == Variant1.user_db[login][0]:
                print('\033[33m Correct password!')
                break
            else:
                print(f'\033[31m Wrong pass! Try again. Attempt: {3 - i}')
                i += 1
                continue
        if i == 4:
            Variant1.user_db[login][1] = False
            print('Too many failure in password. Your account was blocked.\nSend to system administrator')

    def check_status(login: str):
        """Функция проверки статуса учетной записи"""
        if Variant1.user_db[login][1]:
            print('\033[35mAccess guarantee!')
            return True
        else:
            print('\033[31mAccess denied!\033[0m\nTry connect to system administrator.')
            return False

    @staticmethod
    def get_registration():
        """ Функция регистрации нового пользователя. После вненсения пользовательских данных
            создается неактивная учетная запись, до подтверждения системным администратором.
        """
        login = input('Insert name : ')
        user_password, confirm_password = '+', '-'
        while user_password != confirm_password:
            user_password = input('Password : ')
            confirm_password = input('Confirm password :')
        phone = input('Phone : ')
        email = input('E-mail :')
        Variant1.user_db[login] = [user_password, False, phone, email]
        print('\033[36mRegistration complete!\nThan wait message from system administrator to get access.')
        Variant1.get_login()


if __name__ == '__main__':
    Variant1.get_login()
