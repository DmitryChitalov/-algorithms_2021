"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""


"""1. Инструмент tracemalloc. Он является частью системной библиотеки Python. 
По большому счету, tracemalloc используется для создания снимков Python памяти."""

"""2. Для дальнейшего анализа объектов в памяти можно создавать дамп-кучу в определенных строках программы, 
    используя muppy"""
from pympler import muppy, summary

all_objects = muppy.get_objects()
sum1 = summary.summarize(all_objects)
summary.print_(sum1)
dataframes = [ao for ao in all_objects if isinstance(ao, pd.DataFrame)]
for d in dataframes:
    print(d.columns.values)
    print(len(d))
