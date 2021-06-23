"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

import hashlib
from datetime import datetime
import time


class UrlCache:
    cache = {}
    maximum = 50

    def __init__(self):
        self.set_max_cache()            # Контроль макимального числа инициализируется вместе с новым экземпляром

    def get_hash(self, url):
        salt = 'hash'
        result = bytes(f"{url}{salt}", encoding='utf-8')
        result = hashlib.sha3_256(result).hexdigest()
        return result

    def check_url(self, url):
        key = self.get_hash(url)
        if key not in self.cache:
            self.cache.update({key: {'url': url, 'update_datetime': datetime.now(), 'object': 'json_linc'}})

    def show_cache(self):
        print(f'Всего в кэше элементов: {len(self.cache)}')
        for key, el in self.cache.items():
            print(f'{key}: url:{el["url"]}; update_datetime:{el["update_datetime"]}')
        print('*' * 30)

    def clear_cache(self):
        count = len(self.cache)
        self.cache.clear()
        print(f'Cache clear. Cleared {count} rows')

    def get_len_cache(self):
        print(f'Всего записей: {len(self.cache)}')

    def set_max_cache(self, maximum=50):
        self.maximum = maximum
        if len(self.cache) == self.maximum:
            to_dell_max_time = datetime.now()
            key_to_dell = ''
            print(to_dell_max_time)
            for key, el in self.cache.items():
                if to_dell_max_time > el["update_datetime"]:
                    to_dell_max_time = el["update_datetime"]
                    key_to_dell = key
            self.cache.pop(key_to_dell)


if __name__ == '__main__':

    #  Добавляем единичную запись, проверяем число записей
    UrlCache().check_url('https://gb.ru/lessons/145595/homework')
    UrlCache().get_len_cache()

    #  Смотрим что есть в кэше. Получаем таблицу
    UrlCache().show_cache()

    # создаем url  и инициализируем экземпляры класса. с небольшой паузой, чтобы было отличие во времени инициализации
    for i in range(49):
        time.sleep(0.1)
        url = f'https://samara.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p={i}&region=4966'
        UrlCache().check_url(url)

    #  Добавляем единичную  повторяющуюся запись, проверяем число записей
    UrlCache().check_url('https://gb.ru/lessons/145595/homework')
    UrlCache().get_len_cache()
    #     Число записей не изменилось. Проверим состав записей
    #  Смотрим что есть в кэше
    UrlCache().show_cache()
    # повторяющаяся запись не включена в кэш.

    #  Добавляем единичную уникальную запись, проверяем число записей, уникальная запись добавляется в конец очереди.
    UrlCache().check_url('https://ria.ru/')
    UrlCache().get_len_cache()

    #  Смотрим что есть в кэше. Контроль числа записей работает.
    UrlCache().show_cache()

    # Очистим кэш. Посмотрим число записей. Все записи удалены.
    UrlCache().clear_cache()
    UrlCache().get_len_cache()



