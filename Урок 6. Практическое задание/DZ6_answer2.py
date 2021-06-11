"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""
# Использование библиотеки zlib для сжатия длинных текстовых строк, совместно с модулем pickle

import zlib, memory_profiler, pickle

'''
# Код для формирования файлов с хранением списка из набора слов 1-го тома Войны и Мира в не сжатом и сжатом состоянии.
f = open('voyna-i-mir-tom-1.txt', 'r')
war_and_peace_words = f.read().split(' ')

war_and_peace_words_bytes = []
for i in war_and_peace_words:
    war_and_peace_words_bytes.append(zlib.compress(i.encode('utf-8'), level=-1))

f1 = open('list_not_compr.txt', 'wb')
pickle.dump(war_and_peace_words, f1)

f2 = open('list_compr.txt', 'wb')
pickle.dump(war_and_peace_words_bytes, f2)
'''

# Загрузка информации из файлов-хранилищ
f1 = open('list_not_compr.txt', 'rb')
war_and_peace_words = pickle.load(f1)


# f2 = open('list_compr.txt', 'rb')
# war_and_peace_words_bytes = pickle.load(f2)


@memory_profiler.profile()
def lenlen(df):
    for i in df:
        len(i)


lenlen(war_and_peace_words)
# lenlen(war_and_peace_words_bytes)

'''
Результаты замеров:
Список с не сжатой информации
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    36     31.1 MiB     31.1 MiB           1   @memory_profiler.profile()
    37                                         def lenlen(df):
    38     31.1 MiB      0.0 MiB      128505       for i in df:
    39     31.1 MiB      0.0 MiB      128504           len(i)

Список сжатой информации
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    34     27.5 MiB     27.5 MiB           1   @memory_profiler.profile()
    35                                         def lenlen(df):
    36     27.5 MiB      0.0 MiB      128505       for i in df:
    37     27.5 MiB      0.0 MiB      128504           len(i)
    
Видно, что произошло снижение потребления памяти, т.к. необходимо загружать меньшее количество информации.
Способ весьма специфичный, но в приниципе рабочий.
'''
