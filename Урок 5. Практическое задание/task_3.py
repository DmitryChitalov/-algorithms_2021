"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""

from timeit import timeit
from collections import deque
from random import randint

test_data = [1, 2, 3]
num_test = 888
simple_list = test_data.copy()
extend_data = list(range(randint(1, 100)))
deque_test = deque(test_data)

# Количество повторов для timeit
n = 1000


# 1. ------ Операции со списком -------

def list_insert():
    simple_list.insert(0, num_test)


def list_pop_left():
    simple_list.pop(0)


def list_extend_left():
    # Вариант 1 - очень долго выполняется
    # for i in extend_data:
    #     simple_list.insert(0, i)

    # Вариант 2 - самый простой
    nl = []
    nl.extend(extend_data)
    nl.extend(simple_list)
    simple_list.clear()
    simple_list.extend(nl)


def list_append():
    simple_list.append(num_test)


def list_pop_right():
    simple_list.pop()


def list_extend_right():
    simple_list.extend(extend_data)


# 2. ------ Операции со deque -------

def deque_insert():
    deque_test.appendleft(num_test)


def deque_pop_left():
    deque_test.popleft()


def deque_extend_left():
    deque_test.extendleft(extend_data)


def deque_append():
    deque_test.append(num_test)


def deque_pop_right():
    deque_test.pop()


def deque_extend_right():
    deque_test.extend(extend_data)


# --- Делаем замеры для списков
func_list = ['list_insert', 'list_pop_left', 'list_extend_left', 'list_append', 'list_pop_right', 'list_extend_right']
res_list_time = []
for func_name in func_list:
    res_list_time.append(timeit(f'{func_name}()', setup=f'from __main__ import {func_name}', number=n))


# --- Делаем замеры для deque
func_deque = ['deque_insert', 'deque_pop_left', 'deque_extend_left', 'deque_append', 'deque_pop_right', 'deque_extend_right']
res_deque_time = []
for func_name in func_deque:
    res_deque_time.append(timeit(f'{func_name}()', setup=f'from __main__ import {func_name}', number=n))


# --- Выводим результаты:
operations = ['append_left', 'pop_left', 'extend_left', 'append', 'pop_right', 'extend_right']
all_result = []
all_result = list(zip(operations, res_deque_time, res_list_time))
print(f'Количество повторов: ', n)
print('Операция                 Deque       List      Win   D/L % ')
for i in all_result:
    print(f'{i[0]:15.15}\t{round(i[1], 6):15.15}\t{round(i[2], 6):10.10}\t'
          f'\t{"d" if i[1] < i[2] else "L" }\t{round((i[1]/i[2]-1)*100, 3)}')


""" 
Выводы:
Утверждение о том, что если требуется случайный доступ к элементу, то быстрота здесь на стороне обычных списков,
полностью подтверждается в результате выполненных замеров.
Использование Deque более эффективен на задачах, которые предполагают добавление / извлечение данных
с начала списка (с левой стороны). Если массивы данных большие, то это очень актуально. 
При добавлении в конец deque может проигрывать спискам.
Ниже представлены результаты анализа, где данные выводы подтвержаются.


Количество повторов:  1 000
Операция                 Deque       List      Win   D/L % 
append_left    	       0.000175	  0.000705		d	-75.149
pop_left       	       0.000157	  0.000404		d	-61.06
extend_left    	       0.000329	  0.005342		d	-93.849
append         	       0.000188	  0.000176		L	6.648
pop_right      	       0.000226	  0.000148		L	52.362
extend_right   	       0.000209	  0.000172		L	21.478


Количество повторов:  1 000
Операция                 Deque       List      Win   D/L % 
append_left    	       0.000406	   0.00069		d	-41.151
pop_left       	       0.000138	  0.000447		d	-69.003
extend_left    	       0.001767	    0.3613		d	-99.511
append         	       0.000174	  0.000157		L	10.814
pop_right      	       0.000152	  0.000152		L	0.198
extend_right   	       0.001391	  0.003205		d	-56.591

Количество повторов:  1 000
Операция                 Deque       List      Win   D/L % 
append_left    	       0.000202	  0.000666		d	-69.683
pop_left       	        0.00018	  0.000411		d	-56.288
extend_left    	       0.001323	  0.485033		d	-99.727
append         	       0.000175	  0.000287		d	-38.974
pop_right      	        0.00018	  0.000194		d	-7.069
extend_right   	       0.001273	  0.003314		d	-61.586

Количество повторов:  1 000
Операция                 Deque       List      Win   D/L % 
append_left    	       0.000198	  0.000722		d	-72.615
pop_left       	       0.000143	  0.000385		d	-62.802
extend_left    	       0.000537	  0.102394		d	-99.476
append         	       0.000182	  0.000168		L	8.14
pop_right      	       0.000154	  0.000152		L	0.986
extend_right   	         0.0004	  0.000572		d	-30.075

Количество повторов:  10 000
Операция                 Deque       List      Win   D/L % 
append_left    	        0.00195	  0.052077		d	-96.256
pop_left       	       0.001459	  0.026105		d	-94.411
extend_left    	        0.00402	  5.509213		d	-99.927
append         	       0.001775	  0.002556		d	-30.585
pop_right      	       0.001498	  0.001625		d	-7.787
extend_right   	       0.004129	  0.007478		d	-44.776

Количество повторов:  20000
Операция                 Deque       List      Win   D/L % 
append_left    	       0.003747	  0.192689		d	-98.055
pop_left       	       0.002964	  0.163233		d	-98.184
extend_left    	       0.025519	246.846371		d	-99.99
append         	       0.003773	   0.01052		d	-64.135
pop_right      	       0.002948	   0.00311		d	-5.197
extend_right   	       0.025527	  0.067888		d	-62.398
"""