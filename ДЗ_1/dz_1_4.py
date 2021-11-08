"""
    Словарь logpasses содержит: {логин: [пароль, признак активации аккаунта]}
"""

logpasses = {
    'Log01': ['pass001', True],
    'Log02': ['pass011', True],
    'Log03': ['pass021', True],
    'Log04': ['pass031', True],
    'Log05': ['pass041', False],
    'Log06': ['pass051', True],
    'Log07': ['pass061', True],
    'Log08': ['pass071', True],
    'Log09': ['pass081', False],
    'Log10': ['pass091', True],
    'Log11': ['pass101', True],
    'Log12': ['pass111', True],
    'Log13': ['pass121', False],
    'Log14': ['pass131', True],
    'Log15': ['pass141', True],
}

"""
    1-й подход, сложность составляет O(N), т.к. здесь происходит простой перебор.
"""
def chek_user1(log, password):
    for key in logpasses:
        is_user_in = False
        if log == key:
            is_user_in = True
            break

    if is_user_in:
        user_pass_activated = logpasses.get(log)
    else:
        user_pass_activated = None

    if user_pass_activated is None:
        print("данный пользователь отсутствуют в базе")
    else:
        if not user_pass_activated[1]:
            print("Пожалуйста, пройдите активацию")
        else:
            if password == user_pass_activated[0]:
                print("Доступ разрешен!")
            else:
                print("Введен неверный пароль!")


chek_user1('Log14', 'pass131')

"""
    2-й подход, сложность составляет O(1), т.к. здесь получаем значение из словаря напрямую.
"""
def chek_user2(log, password):
    user_pass_activated = logpasses.get(log)

    if user_pass_activated is None:
        print("данный пользователь отсутствуют в базе")
    else:
        if not user_pass_activated[1]:
            print("Пожалуйста, пройдите активацию")
        else:
            if password == user_pass_activated[0]:
                print("Доступ разрешен!")
            else:
                print("Введен неверный пароль!")


chek_user2('Log13', 'pass121')
