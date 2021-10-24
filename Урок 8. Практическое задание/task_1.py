"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""


import heapq
from collections import defaultdict


def huffman_code(freq):
    h = [[weight, [char, '']] for char, weight in freq.items()]
    heapq.heapify(h)
    while len(h) > 1:
        left = heapq.heappop(h)
        right = heapq.heappop(h)
        for i in left[1:]:
            i[1] = '0' + i[1]
        for i in right[1:]:
            i[1] = '1' + i[1]
        heapq.heappush(h, [left[0] + right[0]] + left[1:] + right[1:])
    return sorted(heapq.heappop(h)[1:], key=lambda x: (len(x[-1]), x))


str_huffman = 'String for Huffman Code'

frequency = defaultdict(int)

for chars in str_huffman:
    frequency[chars] += 1

res_tree = huffman_code(frequency)

print("Char".ljust(10) + "Count".ljust(10) + "Huffman Code")
for el in res_tree:
    print(el[0].ljust(10) + str(frequency[el[0]]).ljust(10) + el[1])
