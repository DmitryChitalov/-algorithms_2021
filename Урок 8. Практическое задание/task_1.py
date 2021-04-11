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
    def __init__(self, current_frequency, node_key=-1, left_child=None, right_child=None, character=''):
        self.frequency = current_frequency
        self.key = node_key
        self.left = left_child
        self.right = right_child
        self.code = character

    def __lt__(self, other):
        return self.frequency < other.frequency


def huffman_code(source_string):
    priority_queue = queue.PriorityQueue()
    table_with_codes = {}
    list_with_nodes = []

    def get_codes(parent, code_string=[]):
        code_string.append(parent.code)
        if parent.left:
            get_codes(parent.left, code_string.copy())
            get_codes(parent.right, code_string.copy())
        else:
            table_with_codes[parent.key] = ''.join(code_string)

    table_with_chars_stats = Counter(source_string)
    table_with_chars_stats = deque(sorted(table_with_chars_stats.items(), key=lambda item: item[1]))

    for (x, y) in table_with_chars_stats:
        created_node = Node(y, x)
        list_with_nodes.append(created_node)
        priority_queue.put(created_node)

    while priority_queue.qsize() > 1:
        node_1 = priority_queue.get()
        node_2 = priority_queue.get()
        node_1.code = '1'
        node_2.code = '0'
        new_node = Node(node_1.frequency + node_2.frequency, left_child=node_1, right_child=node_2)
        list_with_nodes.append(new_node)
        priority_queue.put(new_node)

    get_codes(list_with_nodes[-1])

    return table_with_codes


def huffman_encode(code_table, string):
    result = []
    for element in string:
        result.append(code_table[element])
    return ' '.join(result)


test_string = "Do geese see God"
print(huffman_encode(huffman_code(test_string), test_string))
"""
0101 011 11 1001 00 00 101 00 11 101 00 00 11 0100 011 1000

Решение собрано из кусков и переработано.
"""