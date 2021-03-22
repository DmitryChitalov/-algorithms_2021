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

#############################################################################################

def authorization_1(users_dict, user_name, password):
    """Функция проверяет существование пользователя, соответствие пароля и успешность прохождения авторизации.
    входные параметры:
    - словарь информации по учетным данным
    - имя пользователя
    - пароль

    Сложность: !!!. O(1) - константа.
    """
    if users_dict.get(user_name):                               # !!! O(1)
        if users_dict[user_name]['password'] == password:       # !!! O(1)
            if users_dict[user_name]['is_active'] == 'TRUE':    # !!! O(1)
                return 'access granted'                         # !!! O(1)
            else:
                return 'please activate your account'           # !!! O(1)
        else:
            return 'the password is incorrect'                  # !!! O(1)
    else:
        return 'the user does not exist'                        # !!! O(1)

#############################################################################################

def authorization_2(users_dict, user_name, password):
    """Функция проверяет существование пользователя, соответствие пароля и успешность прохождения авторизации.
    входные параметры:
    - словарь информации по учетным данным
    - имя пользователя
    - пароль

    Сложность: !!!. O(n) - линейная.
    """
    for key, value in users_dict.items():                   # !!! O(n)
        if key == user_name:                                # !!! O(1)
            if value['password'] == password:               # !!! O(1)
                if value['is_active'] == 'TRUE':            # !!! O(1)
                    return 'access granted'                 # !!! O(1)
                else:
                    return 'please activate your account'   # !!! O(1)
            else:
                return 'the password is incorrect'          # !!! O(1)
    else:
        return 'the user does not exist'                    # !!! O(1)

#############################################################################################
users_dict = {
    'kuznetsov': {'password':'qazwsx', 'is_active':'TRUE'},
    'sidorov': {'password':'werkwdkc', 'is_active':'TRUE'},
    'pupkin': {'password':';lbrtbuu', 'is_active':'TRUE'},
    'ivanov': {'password':'tttrrrqqq', 'is_active':'FALSE'},
    'petrov': {'password':'peace', 'is_active':'TRUE'},
    'noname': {'password':'', 'is_active':'FALSE'},
    'guest': {'password':'', 'is_active':'TRUE'}
}

print(authorization_1(users_dict,'kuznetsov','qazwsx'))
print(authorization_1(users_dict,'kuznetsov','qazwsx1'))
print(authorization_1(users_dict,'kuznetsov1','qazwsx1'))
print(authorization_1(users_dict,'ivanov','tttrrrqqq'))

print(authorization_2(users_dict,'kuznetsov','qazwsx'))
print(authorization_2(users_dict,'kuznetsov','qazwsx1'))
print(authorization_2(users_dict,'kuznetsov1','qazwsx1'))
print(authorization_2(users_dict,'ivanov','tttrrrqqq'))
