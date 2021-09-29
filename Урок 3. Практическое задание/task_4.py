from hashlib import sha256
from uuid import uuid4


class UrlCache:
    def __init__(self):
        self.urls_table = {}
        self.salt = str((uuid4())).encode('utf-8')

    def check_url(self, url):
        if not self.urls_table.get(self.hash(url)):
            return self.add_cache(url)
        return self.hash(url)

    def hash(self, url):
        return sha256(self.salt + url.encode('utf-8')).hexdigest()

    def add_cache(self, url):
        self.urls_table[self.hash(url)] = url
        return f"Страница {url} добавлена в кэш"


if __name__ == '__main__':
    url_cache = UrlCache()
    print(url_cache.check_url("gb.ru"))
    print(url_cache.check_url("google.com"))
    print(url_cache.check_url("yandex.ru"))
    print(url_cache.check_url("gb.ru"))
    print(url_cache.check_url("google.com"))
    print(url_cache.check_url("wiki.com"))
    print(url_cache.check_url("yandex.ru"))
    print(url_cache.urls_table)
