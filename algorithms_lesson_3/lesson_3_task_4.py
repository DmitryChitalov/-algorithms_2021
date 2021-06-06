from uuid import uuid4
import hashlib


class Web():
    def __init__(self, url):
        self.url = url
        self.url_checking(url)

    def url_checking(self, url):
        salt = uuid4().hex
        if hash_table.get(url):
            print(f'This web page {url} is already in the hash table')
        else:
            hash_table[url] = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
            print(f'The page {url} has been added to the hash table')


hash_table = {}
url_1 = Web('https://www.multitran.com/')
url_2 = Web('https://www.multitran.com/')
url_3 = Web('https://pixabay.com/ru/')
url_4 = Web('https://pixabay.com/ru/')
