"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика)
"""

"""
Попытался использовать Cython.
Собрал из task_2_hello.pyx экстеншн (файл task_2_hello.cp37-win32.pyd), который только создает переменную
с типом данных int и выдает ее размер в байтах.

В файле task_2_starter.py происходит создание аналогичной переменной, но полностью питоном. После этого выводится
результат сравнение размеров этих переменных.

size of int in python (asizeof):  16
size of int in python (getsizeof):  14
size of int in cython:  4

Можно сделать вывод, что cython создает переменные меньшего рамера, что значительно уменьшает размер потребляемой
памяти приложением.
"""