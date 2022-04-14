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
    d = {el[0]: el[1] for el in heap[0][1:]}
    return d


def huff_code(text, tree):
    res = ''
    for letter in text:
        res += tree[letter]
    return ' '.join([res[i:i+4] for i in range(0, len(res), 4)])


message = input(f'Введите сообщение для кодировки: ')

frequency = defaultdict(int)

for chars in message:
    frequency[chars] += 1

res_tree = huff_tree(frequency)
print(f'Частотный словарь: ', frequency)
print(f'Дерево с кодами: ', res_tree)

print(huff_code(message, res_tree))

# Результаты
# Введите сообщение для кодировки: Грокаем Алгоритмы
# Частотный словарь:  defaultdict(<class 'int'>, {'Г': 1, 'р': 2, 'о': 2, 'к': 1, 'а': 1, 'е': 1, 'м': 2, ' ': 1, 'А': 1, 'л': 1, 'г': 1, 'и': 1, 'т': 1, 'ы': 1})
# Дерево с кодами:  {'Г': '0000', 'а': '0001', 'г': '0010', 'е': '0011', 'и': '0100', 'к': '0101', 'л': '0110', 'т': '0111', 'м': '100', 'о': '101', 'р': '110', 'ы': '1110', ' ': '11110', 'А': '11111'}
# 0000 1101 0101 0100 0100 1110 0111 1011 1110 1100 0101 0111 0010 0011 1100 1110