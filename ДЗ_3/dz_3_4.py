from hashlib import sha256
from pprint import pprint

dict_cache = {}


def url_cache(url: str):
    salted = 'my_salt'
    hash_obj = sha256(salted.encode() + url.encode()).hexdigest()

    if hash_obj in dict_cache:
        # Получаем url из словаря
        print(dict_cache.get(hash_obj))
    else:
        # Записываем url в словарь
        dict_cache[hash_obj] = url
        print("url записан в словарь")


if __name__ == '__main__':
    url_cache("https://yandex.ru/")
    url_cache("https://www.google.com/")
    url_cache("https://mail.ru/")
    url_cache("https://gb.ru/education")
    url_cache("https://yandex.ru/")

    pprint(dict_cache)
