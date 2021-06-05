from uuid import uuid4
import hashlib
salt = uuid4().hex
obj = {}


def page_url(url):
    if obj.get(url):
        print("Данный адрес: ", url, "присутствует в кэше")
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        obj[url] = res
        print(obj)


page_url('https://www.vk.ru/')
page_url('https://www.vk.ru/')
page_url('https://www.gmail.com/')
page_url('https://www.gmail.com/')

