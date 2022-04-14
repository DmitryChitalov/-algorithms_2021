"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуете:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.
   Операцию clear() не используем.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""


import pymysql
import time
import functools

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='******',
    db='library',
    charset='utf8mb4'
)
with connection.cursor() as cursor:
    sql = """ 
        SELECT id, firstname FROM users
        LIMIT 10
        """
    cursor.execute(sql)

val = cursor.fetchall()
connection.close()
# print(val)


def stopwatch(func):
    @functools.wraps(func)
    def timer(*args, **kwargs):
        t1 = time.perf_counter()
        vol = func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f'Result {func(*args, **kwargs)}\n running time {t2 - t1:0.9f} sec')
        return vol
    return timer


@stopwatch
def some_list(select):  # O(n)  Заполняем список и базы данных
    return [i for i in select]  # running time 0.000002400 sec


lst = some_list(val)


@stopwatch
def some_dict(select):  # O(n)  Заполням словарь из БД
    return {i[0]: i[1] for i in select}  # running time 0.000002800 sec


dct = some_dict(val)


@stopwatch
def vol_list(vol):  # O(1)  Получаем значение из списка
    return vol[7][1]  # running time 0.000000700 sec


vol_list(lst)


@stopwatch
def vol_dict(vol):  # O(1) Получаем значение из словаря
    return vol[8]  # running time 0.000000600 sec


vol_dict(dct)


@stopwatch
def count_list(vol):  # O(n) Колличество элементов в списке
    count = 0
    for i in vol:
        count += 1
    return count  # running time 0.000001300 sec


count_list(lst)


@stopwatch
def count_dict(vol):  # O(n) Колличество пар ключ значение
    count = 0
    for i in vol:
        count += 1
    return count  # running time 0.000001500 sec


count_dict(dct)

"""
 Судя по данным замера заполнение и перебор словаря занимает больше времени,
 так как для создани словаря идет расчет хэш таблицы,
 тем неменее доступ к данным занимает меньше времени,
 ведь для поиска в списке требуеться пересчет элементов что бы найти нужное значение
 в то время как в словаре можно получить доступ к элементу непосредственно через ключ.
"""
