import hashlib
from uuid import uuid4


def hash_url(url):
    salt = uuid4().hex
    if url in hash_dict:
        return print("Такая страница уже существует")
    else:
        hash_dict[url] = hashlib.md5(salt.encode() + url.encode()).hexdigest()
        return hash_dict


hash_dict = {}
print(hash_url('https://gb.ru'))
