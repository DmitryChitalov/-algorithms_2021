"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""
# Есть вариант оптимизации (используя скрипт из предыдущего дз), где необходимая информация записывается в файл
# а не в отдельную переменную

from memory_profiler import profile
import re
import requests


@profile
def parcing():
    URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    r = requests.get(URL)
    re_find = re.compile(r'(\d*[.]\d*[.]\d*[.]\d*).*\[(.*?)] .(\S*).(\S*).*(\d{3}).(\d+)')
    parsed_raw = re_find.findall(r.text)
    return parsed_raw


parcing()
# Результаты замеров parcing():
'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    64     26.9 MiB     26.9 MiB           1   @profile
    65                                         def parcing():
    66     26.9 MiB      0.0 MiB           1       URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    67     36.7 MiB      9.8 MiB           1       r = requests.get(URL)
    68     36.7 MiB      0.0 MiB           1       re_find = re.compile(r'(\d*[.]\d*[.]\d*[.]\d*).*\[(.*?)] .(\S*).(\S*).*(\d{3}).(\d+)')
    69     61.8 MiB     25.1 MiB           1       parsed_raw = re_find.findall(r.text)
    70     61.8 MiB      0.0 MiB           1       return parsed_raw
'''


@profile
def parcing_opt():
    URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    re_find = re.compile(r'(\d*[.]\d*[.]\d*[.]\d*).*\[(.*?)] .(\S*).(\S*).*(\d{3}).(\d+)')
    # Сохраняем логи не в оперативной памяти, а на жестком диске
    print(re_find.findall(requests.get(URL).text), file=open('log.txt', 'w'))
    return 'Done'


parcing_opt()
# Результаты замеров parcing_opt():
'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    39     30.6 MiB     30.6 MiB           1   @profile
    40                                         def parcing_opt():
    41     30.6 MiB      0.0 MiB           1       URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    42     30.6 MiB      0.0 MiB           1       re_find = re.compile(r'(\d*[.]\d*[.]\d*[.]\d*).*\[(.*?)] .(\S*).(\S*).*(\d{3}).(\d+)')
    43                                             # Сохраняем логи не в оперативной памяти, а на жестком диске
    44     31.0 MiB      0.4 MiB           1       print(re_find.findall(requests.get(URL).text), file=open('log.txt', 'w'))
    45     31.0 MiB      0.0 MiB           1       return 'Done'
'''

'''
Вывод:
Можно в принципе обходить дополнительные переменные, для экономии памяти, если они не нужны
'''