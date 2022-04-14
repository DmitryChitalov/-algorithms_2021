from uuid import uuid4
import hashlib


salt = uuid4().hex
cache_dict = {}


def save_in_cache(url):
    make_hash_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if cache_dict.get(url):
        return f'Ссылка "{url}" уже в кэше.'
    else:
        cache_dict[url] = make_hash_url
        return f'Ссылка "{url}" успешно сохранена в кэш.'


print(save_in_cache('https://geekbrains.ru/'))
print(save_in_cache('https://www.youtube.com/'))
print(save_in_cache('https://geekbrains.ru/'))
