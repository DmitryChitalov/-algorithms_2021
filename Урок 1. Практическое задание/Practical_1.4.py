
data_dict = {'James': ['snake666', True], 'Linda': ['starcraft2', True],
             'David': ['david777', False], 'Karen': ['karen123', False],
             'Daniel': ['dani111', False], 'Ashley': ['top5', True]}


def check_account(login, password):
    """Difficult: O(n) """
    if login in data_dict.keys():  # O(n)
        if data_dict[login][0] == password:
            if data_dict[login][1] == True:
                return 'you have successfully logged in'
            else:
                return 'activate your account'
        else:
            return 'you entered the wrong password'
    else:
        return 'you entered the wrong login'


print(check_account('Ashley', 'top5'))


####################################################################################################


def check_account_2(login, password):
    """Difficult: O(1)
     Это решение будет эффективней так как сложность равняется константе
     """
    if data_dict[login][0] == password:
        if data_dict[login][1] == True:
            return 'you have successfully logged in'
        else:
            return 'you should activate your account'
    else:
        return 'you entered the wrong password'


try:
    print(check_account_2('james'.title(), 'snake66'))
except KeyError:
    print('you entered the wrong login')