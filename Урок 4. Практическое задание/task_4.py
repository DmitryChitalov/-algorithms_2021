"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""


from timeit import timeit
from collections import Counter


array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3(array):
    return max(zip((array.count(elem) for elem in set(array)), set(array))) 


def func_4(array):
    return Counter(array).most_common()[0]


def func_5(array):
    elem = max(array, key=array.count)
    return elem, array.count(elem)

print(array.count(3))
print(func_1())
print(func_2())
print(f'''Чаще всего встречается число {func_3(array)[1]}, \
оно появилось в массиве {func_3(array)[0]} раз(а)''')
print(f'''Чаще всего встречается число {func_4(array)[0]}, \
оно появилось в массиве {func_4(array)[1]} раз(а)''')
print(f'''Чаще всего встречается число {func_5(array)[0]}, \
оно появилось в массиве {func_5(array)[1]} раз(а)''')


print(f'''Время выполнения func_1
==>>{timeit(
        'func_1()',
        globals=globals(),
    )}
# ''', end='\n')

print(f'''Время выполнения func_2
==>>{timeit(
        'func_2()',
        globals=globals(),
    )}
# ''', end='\n')

print(f'''Время выполнения func_3
==>>{timeit(
        'func_3(array)',
        globals=globals(),
    )}
# ''', end='\n')

print(f'''Время выполнения func_4
==>>{timeit(
        'func_4(array)',
        globals=globals(),
    )}
# ''', end='\n')

print(f'''Время выполнения func_5
==>>{timeit(
        'func_5(array)',
        globals=globals(),
    )}
''', end='\n')


# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
#                                                                  
# Время выполнения func_1                                          
# ==>>1.1605923460001577                                        
# # 
# Время выполнения func_2                                        
# ==>>1.518638622999788                                         
# # 
# Время выполнения func_3                                         
# ==>>1.4992159610001181                                          
# # 
# Время выполнения func_4                                      
# ==>>2.1902988339998046                                        
# # 
# Время выполнения func_5                    
# ==>>0.8993356219998532                             
# # 
# 
# 
