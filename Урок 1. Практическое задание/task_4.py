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
Без выполнения пунктов 2 и 3 задание считается нерешенным.
Пункты 2 и 3 можно выполнить через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


def is_access_v1(lgn, pwd, users_db):
    """Верифицирует учетные данные и проверяет активацию профиля.
    Возвращает кортеж bool (log_verify, pwd_verify, is_active)."""
    # Перебор значений - сложность O(N)

    # перебираем все профили и проверяем по каждому
    for curr_lgn, curr_data in users_db.items():             # O(N)
        curr_pwd, is_active = curr_data[0], curr_data[1]     # O(1)
        if lgn == curr_lgn:  # нашли в БД профилей логин     # O(1)
            pwd_verify = True if pwd == curr_pwd else False  # O(1)
            return True, pwd_verify, is_active               # O(1)
    return False, False, is_active                           # O(1)


def is_access_v2(lgn, pwd, users_db):
    """Верифицирует учетные данные и проверяет активацию профиля.
    Возвращает кортеж bool (log_verify, pwd_verify, is_active)."""

    # Поиск по хеш-таблице - сложность O(1)
    curr_data = users_db.get(lgn)                           # O(1)

    # Если логина в БД учеток не нашлось
    if curr_data is None:                                   # O(1)
        return False, False, False                          # O(1)
    curr_pwd, is_active = curr_data[0], curr_data[1]        # O(1)
    pwd_verify = True if pwd == curr_pwd else False         # O(1)
    return True, pwd_verify, is_active                      # O(1)


def access_show(lgn_verify, pwd_verify, is_active):
    """Выводит в консоль информацию о результатах проверки учетки"""

    pwd_status = 'Корректный!' if pwd_verify else 'Не корректный!!!'
    active_status = "Активирована!" if is_active else "Необходима активация!!!"

    if lgn_verify:
        print(f'login: Существует!, password: {pwd_status}, '
              f'статус учетной записи: {active_status}')
    else:
        print(f'login: Не существует!!!')


if __name__ == '__main__':

#БЛОК ТЕСТИРОВАНИЯ
# ключи - логины, значения - (пароль, активация уч. записи)
    users_dict = {
        'user1': ('pwd_user1', False),
        'user2': ('pwd_user2', True),
        'user3': ('pwd_user3', False)
    }

    # проверяем сначала по существующим в БД пользователям
    for user, data in users_dict.items():
        user_pwd = data[0]  # выделяем пароль
        print(f'\nВерификация (2мя методами) пользователя {user}:')

        # итог верификации учетных данных
        lgn_ver, pwd_ver, is_act = is_access_v1(user, user_pwd, users_dict)
        access_show(lgn_ver, pwd_ver, is_act)
        lgn_ver, pwd_ver, is_act = is_access_v2(user, user_pwd, users_dict)
        access_show(lgn_ver, pwd_ver, is_act)

    # проверяем по еще несколько вариантов
    user, user_pwd = 'user666', 'pwd_user666'
    print(f'\nВерификация (2мя методами) пользователя {user}:')
    access_show(*is_access_v1(user, user_pwd, users_dict))
    access_show(*is_access_v2(user, user_pwd, users_dict))

    user, user_pwd = 'user1', 'df,dlLDS_KF'
    print(f'\nВерификация (2мя методами) пользователя {user}:')
    access_show(*is_access_v1(user, user_pwd, users_dict))
    access_show(*is_access_v2(user, user_pwd, users_dict))
