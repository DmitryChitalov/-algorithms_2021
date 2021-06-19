from uuid import uuid4
from hashlib import sha256

url_dict = {}
salt = uuid4().hex


def cash():
    url = input('Введите url: ')
    if url == 'stop':
        return url_dict

    hash_url = sha256(url.encode() + salt.encode()).hexdigest()

    if hash_url in url_dict.values():
        print('Такая ссылка уже введена')
        return cash()
    else:
        url_dict[url] = hash_url
        return cash()


print(cash())
