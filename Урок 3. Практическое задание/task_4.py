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


class Web_cache():
    def __init__(self):
        self.arr = {}

    def web_cache(self, web_1):
        if self.arr.get(self.translate(web_1)):
            return 'есть: ' + self.arr[self.translate(web_1)]
        self.arr[self.translate(web_1)] = web_1
        return "Нет"

    def translate(self, web_1):
        return hash('hell' + web_1)


web = Web_cache()
arr = ['https://yandex.ru/', 'https://www.google.ru/', 'https://www.opera.com/ru']
for i in arr:
    web.web_cache(i)
print(web.web_cache('https://yandex.ru/'))
print(web.web_cache('https://www.google.ru/'))
print(web.web_cache('https://www.opera.com/ru'))
print(web.web_cache('https://www.opera.com/rY'))
