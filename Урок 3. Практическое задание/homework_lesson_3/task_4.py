import hashlib

url = input('url')

cache = {'10dd6e016c6ddd709c730ea8db557c20a6e5a2558d5b73178bc68797bbb22e19': 'gb.ru'}


def chek_url(u):
    hash_u = hashlib.sha256(u.encode()).hexdigest()
    if hash_u in cache.keys():
        return True
    else:
        return {hash_u: u}


chek_url(url)

try:
    cache.update(chek_url(url))
except TypeError:
    print("Данный адрес уже присутствует в кеше")

print(cache)