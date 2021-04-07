"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""


#время appendleft deque  0.0
#время appendleft list  0.001001596450805664
#----------------------------------------------------------
#время append deque  0.0
#время append list  0.0
#----------------------------------------------------------
#время pop deque  0.0
#время pop list  0.0
#----------------------------------------------------------
#время popleft deque  0.0
#время popleft list  0.0009987354278564453
#----------------------------------------------------------
#время extend в deque  0.01351165771484375
#время extend в list  0.012002229690551758
#----------------------------------------------------------
#  используя колекцию deque можно увидеть разницу при различных оперциях,
# что время выполнения быстрее, при маленьких данных разницы нет, но при достаточно больших разница ощютима




from collections import deque
import time



my_list = []
for i in range(1, 1000000):
    my_list.append(i)

my_list_deque = deque(my_list)




start_time = time.time()
my_list_deque.appendleft(99999)
end_time = time.time()
print('время appendleft deque ', end_time - start_time)

start_time = time.time()
my_list.insert(0, 99999)
end_time = time.time()
print('время appendleft list ', end_time - start_time)

print('----------------------------------------------------------')
start_time = time.time()
my_list_deque.append(99999)
end_time = time.time()
print('время append deque ', end_time - start_time)

start_time = time.time()
my_list.append(99999)
end_time = time.time()
print('время append list ', end_time - start_time)

print('----------------------------------------------------------')


start_time = time.time()
my_list_deque.pop()
end_time = time.time()
print('время pop deque ', end_time - start_time)

start_time = time.time()
my_list.pop()
end_time = time.time()
print('время pop list ', end_time - start_time)

print('----------------------------------------------------------')


start_time = time.time()
my_list_deque.popleft()
end_time = time.time()
print('время popleft deque ', end_time - start_time)

start_time = time.time()
my_list.remove(1)
end_time = time.time()
print('время popleft list ', end_time - start_time)

print('----------------------------------------------------------')

new_my_list = my_list

start_time = time.time()
my_list_deque.extend(new_my_list)
end_time = time.time()
print('время extend в deque ', end_time - start_time)

start_time = time.time()
my_list.extend(new_my_list)
end_time = time.time()
print('время extend в list ', end_time - start_time)

print('----------------------------------------------------------')