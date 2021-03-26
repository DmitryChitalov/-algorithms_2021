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
from collections import Counter, deque
import queue


class Node:
    def __init__(self, x, k=-1, l=None, r=None, c=''):
        self.freq = x
        self.key = k
        self.left = l
        self.right = r
        self.code = c

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_code(data):
    node_list = []
    que = queue.PriorityQueue()
    code_table = {}

    freq_table = Counter(data)
    freq_table = deque(sorted(freq_table.items(), key=lambda item: item[1]))

    # Huffman tree init
    for (k, v) in freq_table:
        node_list.append(Node(v, k))
        que.put(node_list[-1])

    # Huffman tree generate
    while que.qsize() > 1:
        node1 = que.get()
        node2 = que.get()
        node1.code = '1'
        node2.code = '0'
        nn = Node(node1.freq + node2.freq, l=node1, r=node2)
        node_list.append(nn)
        que.put(node_list[-1])

    # get Huffman code
    def get_huffman_code(p, code_str=[]):
        code_str.append(p.code)
        if p.left:
            get_huffman_code(p.left, code_str.copy())
            get_huffman_code(p.right, code_str.copy())
        else:
            code_table[p.key] = ''.join(code_str)

    get_huffman_code(node_list[-1])

    return code_table


def huffman_encodind(code_table, string):
    result = []
    for el in string:
        result.append(code_table[el])
    return ' '.join(result)


# строка для кодирования
s = "beep boop beer!"

# функция заполняет кодовую таблицу (символ-его код)
# {'b': '11', 'p': '101', 'r': '1001', '!': '1000', 'e': '01', 'o': '001', ' ': '000'}
for k, v in huffman_code(s).items():
    print(k, '-', v)

# закодированная строка
print(huffman_encodind(huffman_code(s), s))

