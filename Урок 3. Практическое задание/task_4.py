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
    """кэширование урлов"""

    def __init__(self):
        self._cache_dict = dict()

    def _get_hash(self, url):
        """вычисление хеша УРЛа"""
        return hashlib.sha256(url.encode() + "salt".encode()).hexdigest()

    def _add_url(self, url):
        """запись хешированного УРЛа в кэш"""
        self._cache_dict.update({self._get_hash(url): url})

    def open_url(self, url):
        """возвращает урл есле он есть в кеше, в противном случае - возвращает УРЛ
        (в реальных условиях выполнялась бы загрузга странички)
        """
        record = self._cache_dict.get(self._get_hash(url))
        if record:
            print(f"Возвращаем запись из кэша: {record}\nхеш записи: "
                  f"{self._get_hash(self._get_hash(url))}")
        else:
            self._add_url(url)
            print(f"Новая запись добавлена в кэш: {url}")


cache = Cache()
cache.open_url("https:\\\\vk.com")
cache.open_url("https:\\\\vk.com")
cache.open_url("https:\\\\mail.ru")
cache.open_url("https:\\\\vk.com")
cache.open_url("https:\\\\mail.ru")
cache.open_url("https:\\\\mail.ru")
cache.open_url("https:\\\\google.com")
