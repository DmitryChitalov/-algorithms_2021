"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from timeit import default_timer
from memory_profiler import memory_usage, profile
from pympler import asizeof

def dec_tm(fn):
    def fn_wrap(*args,**kwargs):
        tm_s = default_timer()
        mem_s = memory_usage()
        res = fn(*args,**kwargs)
        mem_e = memory_usage()
        tm_e = default_timer()
        print(f"\nprofile: {fn.__name__}")
        print(f"\tMemory: {(mem_e[0] - mem_s[0]):0.6f} ")
        print(f"\tTime: {(tm_e - tm_s):0.6f} ")
        return res
    return fn_wrap
#------- Пример 1 -----------------------
print("--  Пример 1  Json.dumps ------------------------------")
import json

@dec_tm
@profile
def fill_dict_json(num):
    dct = {f"name {i}": i for i in range(num)} # +13.9 MiB создание словаря
    dump = json.dumps(dct)                       # +2.9 MiB сериализация словаря
    del dct                                    # -14.3 MiB удаление словаря
    return json.loads(dump)                     # +13.6 MiB восстановление словаря из дампа


dct = fill_dict_json(100000)

print(f"Load dict {len(dct)}: {asizeof.asizeof(dct)}")
'''
Исспользование Json снижает нагрузку на память после сериализации объекта Dict
'''
while(1):
    pass
#------- Пример 2 -----------------------
print("--  Пример 2  Class __slots__ VS Class dict() ------------------------------------")
import string
import random

class UserOnDict:
    '''
    Класс на основе dict()
    '''
    def __init__(self,nik,psw,email):
        self._nik = nik
        self._psw = psw
        self._email = email
    
    def __str__(self):
        return f"{self._nik}:{self._email}"

class UserOnSlot:
    '''
    Класс на основе __slots__
    '''
    __slots__=('_nik','_psw','_email')
    def __init__(self,nik,psw,email):
        self._nik = nik
        self._psw = psw
        self._email = email
    
    def __str__(self):
        return f"{self._nik}:{self._email}"

#--------------------------------------------------------------------------------
def dict_fab(*arg):
    nik = arg[0]
    return UserOnDict(nik,arg[1],f"{nik}@email.du")

def slot_fab(*arg):
    nik = arg[0]
    return UserOnSlot(nik,arg[1],f"{nik}@email.du")

@dec_tm
@profile
def fill_users(numb,fn):
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    def psw_gen():
        psw =''
        for i in range(16):
            psw += random.choice(chars)
        return psw
    def nik_gen():
        letters = string.ascii_lowercase
        nik = ''.join(random.choice(letters) for i in range(8)) 
        return nik    

    return [fn(nik_gen(),psw_gen()) for n in range(numb)]
#----------------------------------------------------------------------------------------
usersSlot = fill_users(100,slot_fab)
print(f"List SlotUser {len(usersSlot)} элементов:{asizeof.asizeof(usersSlot)}")  
usersDict = fill_users(100,dict_fab)
print(f"List DictUser {len(usersDict)} элементов:{asizeof.asizeof(usersDict)}")   
'''
Применение __slots__ позволило сократить потребление памяти

profile: Класс на основе словаря
        Time: 1.573517
List DictUser 1000 элементов:385192

        Time: 16.673549
List DictUser 10000 элементов:3847792

profile: Класс на основе __slots__ = []
        Time: 1.601371
List SlotUser 1000 элементов:281024

        Time: 16.734592
List SlotUser 10000 элементов:2807624

'''

#------- Пример 3 -----------------------
print("--  Пример 3  generator -----------------------------------")
from itertools import islice

def fib_list(n):
    fb = [0, 1,]
    for i in range(2, n):
        fb.append(fb[i-1] + fb[i-2])
    return fb
@dec_tm
@profile
def fib_list_test(n,pos):
    fb = fib_list(n)    
    return fb[pos] 

def fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
@dec_tm
@profile
def fib_gen_test(n,pos):
    fb = fib_gen(n)    
    return next(islice(fb, pos, None))



lst_pos = fib_list_test(100000,6000)
#print(f"List: {lst_pos}")
fib_pos = fib_gen_test(100000,6000)
#print(f"Generator: {fib_pos}")
'''
Исспользование generator даёт выигрышь в памяти

Поиск 6.000-го числа фибоначи из 100.000 массива
profile: List
        Memory use: 484.4 MiB
        Memory: 2.589844
        Time: 0.627699

profile: Generator
        Memory use: 23.6 MiB
        Memory: 0.000000
        Time: 0.233216
'''