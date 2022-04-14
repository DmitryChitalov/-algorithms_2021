from uuid import uuid4
import hashlib
salt = uuid4().hex
obj = {}


def pages(url):
    if obj.get(url):
        print("Данный адрес: ", url, "присутствует в кэше")
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        obj[url] = res
        print(obj)


pages('https://www.adidas.ru/')
pages('https://www.adidas.ru/')
pages('https://www.adidas.ru/')