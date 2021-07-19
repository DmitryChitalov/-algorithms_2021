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


def huff_tree(freq):
    heap = [[weight, [char, '']] for char, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        for val in left[1:]:
            val[1] = '0' + val[1]
        for val in right[1:]:
            val[1] = '1' + val[1]
        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda x: (len(x[-1]), x))


s_string = 'Encode a String in Huffman Coding Using Python'

frequency = defaultdict(int)

for chars in s_string:
    frequency[chars] += 1

res_tree = huff_tree(frequency)

print("Char".ljust(10) + "Count".ljust(10) + "Huffman Code")
for el in res_tree:
    print(el[0].ljust(10) + str(frequency[el[0]]).ljust(10) + el[1])
