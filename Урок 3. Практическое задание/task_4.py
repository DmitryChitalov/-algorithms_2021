"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
import hashlib


class Cache:
    """кэширование урлов
    Предполагается следующий воркфло:
    Пользователь запрашивает урл. Ищем его в кэше.
    Если по урлу хеш найден, то запрашиваем по данному хешу контент страницы в БД или в другом хранилище.
    Извлекаем контент сранички.
    Если по заданному урлу не найден хеш в кэше, тогда загружаем страничку из сети и сохраняем хеш
    контента в кэш как {url:hash} и в БД сохраняется {hash: контент стр}
    """

    def __init__(self):
        self._cache_dict = dict()

    def _get_hash(self, url):
        """вычисление хеша УРЛа"""
        return hashlib.sha256(url.encode() + "salt".encode()).hexdigest()

    def _add_url(self, url):
        """запись хешированного УРЛа в кэш"""
        self._cache_dict.update({url: self._get_hash(url)})

    def open_url(self, url):
        """возвращает урл если он есть в кэше, в противном случае - возвращает УРЛ
        (в реальных условиях выполнялась бы загрузга странички)
        """
        hash_ = self._cache_dict.get(url)
        if hash_:
            print(f"Возвращаем запись из кэша: {url}\nхеш записи: "
                  f"{hash_}")
        else:
            self._add_url(url)
            print(f"Новая запись добавлена в кэш: {url} : {self._cache_dict.get(url)}")


cache = Cache()
cache.open_url("https://vk.com")
print("-" * 100)
cache.open_url("https://vk.com")
print("-" * 100)
cache.open_url("https://mail.ru")
print("-" * 100)
cache.open_url("https://vk.com")
print("-" * 100)
cache.open_url("https://mail.ru")
print("-" * 100)
cache.open_url("https://mail.ru")
print("-" * 100)
cache.open_url("https://google.com")
