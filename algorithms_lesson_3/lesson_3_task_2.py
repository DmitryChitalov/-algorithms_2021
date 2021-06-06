import hashlib


def generate_hash(login, password):
    hash_obj = hashlib.sha256((login.encode() + password.encode()))
    hex_dig_res = hash_obj.hexdigest()
    return login, hex_dig_res


def get_hash():
    login = input('Enter your login: ')
    password = input('Enter your password: ')
    hash1 = generate_hash(login, password)
    print(f'The hash is {hash1}')

    login = input('Enter your login again: ')
    password = input('Enter your password again: ')
    hash2 = generate_hash(login, password)

    if hash1 == hash2:
        print('Correct data. Welcome')
    else:
        print('Wrong data! Try again.')


get_hash()
