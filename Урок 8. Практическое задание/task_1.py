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
from collections import Counter
import heapq


class HuffmanTree:
    def __init__(self, root):
        self.root = root
        self.convert = {}

    def walk(self):
        return self._walk(self.root)

    def _walk(self, curr_node, path=''):
        if not curr_node.is_leaf:
            self.convert[curr_node.val] = path

        else:
            self._walk(curr_node.left_child, path=f'{path}0')
            self._walk(curr_node.right_child, path=f'{path}1')

    @property
    def get_dict(self):
        return self.convert


class Node:
    def __init__(self, freq, val=None, rc=None, lc=None):
        self.val = val
        self.right_child = rc
        self.left_child = lc
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq

    def __str__(self):
        return f'{self.freq}'

    @property
    def is_leaf(self):
        return self.right_child and self.left_child


def Huffman_code(data):
    freq = sorted(dict(Counter(data)).items( ), key=lambda i: i[1])
    freq = [(i[1], i[0]) for i in freq]
    heap = []
    for i in freq:
        node = Node(i[0], val=i[1])
        heapq.heappush(heap, (node.freq, node))

    while len(heap) > 1:
        freq, val = heapq.heappop(heap)
        freq1, val1 = heapq.heappop(heap)
        new_node = Node(freq1 + freq, lc=val, rc=val1)
        heapq.heappush(heap, (new_node.freq, new_node))

    code = HuffmanTree(heap[0][1])
    code.walk( )
    return code.get_dict


if __name__ == '__main__':
    data_in = input( )
    print(Huffman_code(data_in))
    for l in data_in:
        print(Huffman_code(data_in)[l], end=' ')
