import random
import time

def fill_list(n): # O(N)
    l = []
    for i in range(n):
        a = random.randint(-10, 10)
        l.append(a)
    return l


def fill_dicttionary(n): #O(N)
    d = dict()
    for i in range(2*n):
        a = random.randint(10,20)
        b = random.randint(-10,10)
        d.update({str(a):b})
    return d


def push_at_position_list(l,item,n): #O(N)
    temp = l[n-1:]
    l = l[:n-1]
    l.append(item)
    l = l + temp
    return l

def push_at_dictionary(d,item): #O(1)
    d.update(item)
    return d

def del_from_list(l,item): #O(N)
    i = l[0]
    j = 0
    while i != item:
        j += 1
        i = l[j]
    del l[j]
    return l

def del_from_dictionary(d,item): #O(1)
    del d[str(item)]
    return d

#заполнение
f = time.time()
a = fill_list(100000)
m = time.time()
b = fill_dicttionary(100000)
e = time.time()

print(m - f) # 0.145
print(e - m) # 0.68

# заполнение списка с использованием таких функций быстрее в 2.5 раза


# добавление элемента
# поскольку нет необходимости добавлять элемент в словарь
# на конкретную позицию, при добавлении элемента в конец
# списка, это занимает значительно больше времени

f = time.time()
a = push_at_position_list(a,100,99995)
m = time.time()
b = push_at_dictionary(b,{"100":100})
e = time.time()

print(m - f) # 0.005
print(e - m) # 0.0

# удаление конкретного элемента
# поскольку удаление элемента сначала подразумевает его поиск
# то аналогично предыдущему пункту удаление из списка происходит
# значительно медленнее
f = time.time()
a = del_from_list(a,100)
m = time.time()
b = del_from_dictionary(b, 100)
e = time.time()

print(m - f) # 0.149
print(e - m) # 0.0

# при использовании бинарного поиска, получистся уменьшить
# сложность алгоритма удаления для списка до логарифмической
