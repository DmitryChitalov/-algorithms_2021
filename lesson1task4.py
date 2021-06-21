profiles = {
    'user1':{'password': '1111', 'status':True},
    'user2':{'password': '2222', 'status':True},
    'user3':{'password': '3333', 'status':False},
    'user4':{'password': '4444', 'status':True},
    'user5':{'password': '5555', 'status':False},
}

#решение 1 o(n)
def authentication(profiles, user, password):
    for key, value in profiles.items():
        if key == user:
            if value['password'] == password and ['status']:
                return 'Welcome!'
            elif value['password'] != password:
                return 'Wrong password!'
            elif value['password'] == password and not value['status']:
                return 'Please activate your account'

    return "User doesn't exist"

print(authentication(profiles, 'user2', '2222'))


#решение2 o(1)
def authentication_1(profiles, user, password):
    if user in profiles:
        if profiles[user]['password'] == password and profiles[user]['status']:
            return 'Welcome!'
        elif profiles[user]['password'] == password and not profiles[user]['status']:
            return 'Please activate your account'
        elif profiles[user]['password'] != password:
            return 'Wrong password!'


print(authentication_1(profiles, 'user2', '1111'))

#второе решение эффективнее, так как не зависит от длины словаря