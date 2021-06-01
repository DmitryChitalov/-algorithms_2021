"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете усложнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.
Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib, pickle, uuid


def url_cache_from_hdd(cache_file='DZ3_answer4_url_cache.txt'):
    '''
    Загрузка кэша сохраненного на диске
    '''
    try:
        f = open(cache_file, 'rb')
        ram_memory_cache = pickle.load(f)
    except:
        ram_memory_cache = {}
    return ram_memory_cache


def url_cache_load_on_hdd(ram_memory_cache, cache_file='DZ3_answer4_url_cache.txt'):
    '''
    Выгрузка кэша на диск
    '''
    f = open(cache_file, 'wb')
    pickle.dump(ram_memory_cache, f)
    f.close()


def clear_hdd_cache(cache_file='DZ3_answer4_url_cache.txt'):
    '''
    Очитска кэша на диске
    '''
    f = open(cache_file, 'wb')
    f.close()

#не совсем понятно как организовать соль. Ведь мы ничего не вводим кроме url, а генерировать случайное число не вариант, т.к. для одного url будем получать два хэша
def url_cache_add(url, ram_memory_cache):
    '''
    Добавление в кэш в оперативной памяти
    '''
    url_hash = hashlib.md5(bytes(url, encoding='utf-8')).hexdigest()
    if url_hash not in ram_memory_cache.keys():
        ram_memory_cache[url_hash] = url
        print('записан в кэш: ' + url)
    else:
        print('уже есть в кэше: ' + url)
    return ram_memory_cache

def url_cache_del(url_hash, ram_memory_cache):
    '''
    Удаление из кэша оперативной памяти по хэшу
    '''
    del_elem = ram_memory_cache[url_hash]
    del ram_memory_cache[url_hash]
    print('удален из кэша: ' + del_elem)
    return ram_memory_cache

ram_memory_cache1 = url_cache_from_hdd()                                    #создание кэша в оперативной памяти из сохраненного кэша

url_list = ['https://yandex.ru/',                                           #список ссылок для кэша
            'https://yandex.ru/images/?utm_source=main_stripe_big',
            'https://yandex.ru/news/?utm_source=main_stripe_big',
            'https://translate.yandex.ru/?utm_source=main_stripe_big',
            'https://yandex.ru/'
            ]

for i in url_list:                                                          #наполнение кэша ссылками
    url_cache_add(i, ram_memory_cache1)

url_cache_del('30b7df27e9f842b33cf9e517c98a075e', ram_memory_cache1)        #удаление https://yandex.ru/ по хэшу из кэша
url_cache_load_on_hdd(ram_memory_cache1)                                    #сохранение кэша на диск

f = open('DZ3_answer4_url_cache.txt', 'rb')
ram_memory_cache = pickle.load(f)
print(ram_memory_cache)                                                     #просмотр соддержимого сохраненнго кэша
clear_hdd_cache()                                                           #очистка кэша на диске
