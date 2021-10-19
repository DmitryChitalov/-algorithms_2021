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

# для первого варианта
lst_1 = {'user_1': {'login': 'иван', 'password': '123', 'account_activation': 'n'},
         'user_2': {'login': 'мария', 'password': '456', 'account_activation': 'y'},
         'user_3': {'login': 'роман', 'password': '523', 'account_activation': 'y'}}
# для второго варианта
lst_2 = ['иван', '123', 'n',
         'мария', '456', 'y',
         'роман', '523', 'y']


def key_search(dictionary):    # сложность квадратичная O(n^2)
    user_name = input('Введите имя пользователя: ')
    account_number = 0
    for key in dictionary:    # O(n)
        account_number = account_number + 1
        if user_name.lower() == dictionary[key]['login']:    # O(1)? (а dictionary[key]['login'] не O(n) разве?)
            print(user_name)
            if dictionary[key]['account_activation'] == 'n':    # O(1)
                print('ваш аккуант не активирован! Доступ к ресурсу заблокирован.')
                account_activation = input("Хотите активировать аккуант? (y/n)")
                if account_activation.lower() in ('y', 'yes', 'да'):    # O(n)
                    account_password = input('Для подтверждения активации введите пароль')
                    if account_password == ictionary[key]['password']:
                        print('Ваш аккуант активирован, открыт доступ к ресурсу')
                    else:
                        print('Введённый пароль не совпадает с паролем в БД.')
                elif account_activation.lower() in ('n', 'no', 'нет'):
                    print('Не хотите, как хотите')
            elif dictionary[key]['account_activation'] == 'y':
                print('Ваш аккуант актирован. Доступ к ресурсу открыт.')
        elif user_name.lower() != dictionary[key]['login'] and len(dictionary) == account_number:
            print('аккуант с именем ', user_name, ' не найден')


def through_cycle(dictionary):    # сложность квадратичная O(n^2)
    account_user = input('Введите имя пользователя: ').lower()
    if dictionary.count(account_user):    # O(n)
        index_element = dictionary.index(account_user)    # O(1)
        if dictionary[index_element + 2] == 'n':    # O(1)
            print('ваш аккуант не активирован! Доступ к ресурсу заблокирован.')
            account_activation = input("Хотите активировать аккуант? (y/n) ").lower()
            if account_activation in ('y', 'yes', 'да'):    # O(n)
                account_password = input('Для подтверждения активации введите пароль ')
                if account_password == dictionary[index_element + 1]:    # O(1)
                    print('Ваш аккуант активирован, открыт доступ к ресурсу')
                else:
                    print('Введённый пароль не совпадает с паролем в БД.')
            elif account_activation in ('n', 'no', 'нет'):    # O(n)
                print('Не хотите, как хотите')
        elif dictionary[index_element + 2] == 'y':    # O(1)
            print('Ваш аккуант актирован. Доступ к ресурсу открыт.')
    elif not dictionary.count(account_user):    # O(n)
        print('аккуант с именем ', account_user, ' не найден')


key_search(lst_1)
through_cycle(lst_2)


"""если правильно обозначил сложность (в чём сильно сомневаюсь), 
то обе функции равнозначны по сложности - квадротичные
"""
