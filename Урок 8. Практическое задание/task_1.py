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


class Node:
    def __init__(self, frequency):
        self.left = None
        self.right = None
        self.father = None
        self.frequency = frequency

    def is_left(self):
        return self.father.left == self


def create_nodes(frequency_list):
    """
    Создание листьев ноды.
    """
    return [Node(frequency) for frequency in frequency_list]


def create_huffman_tree(nodes):
    """
    Создание дерева.
    """
    queue = nodes[:]

    while len(queue) > 1:
        queue.sort(key=lambda item: item.frequency)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.frequency + node_right.frequency)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)

    queue[0].father = None
    return queue[0]


def huffman_encoding(nodes, root):
    """
    Кодируем строку.
    """
    huffman_code = [""] * len(nodes)

    for i in range(len(nodes)):
        node = nodes[i]
        while node != root:
            if node.is_left():
                huffman_code[i] = "0" + huffman_code[i]
            else:
                huffman_code[i] = "1" + huffman_code[i]
            node = node.father

    return huffman_code


def encode_str(text, char_frequency, codes):
    """
    Кодируем строку.
    """
    ret = ""
    for char in text:
        i = 0
        for item in char_frequency:
            if char == item[0]:
                ret += codes[i]
            i += 1

    return ret


def decode_str(huffman_str, char_frequency, codes):
    """
    Декодируем строку.
    """
    ret = ""
    while huffman_str != "":
        i = 0
        for item in codes:
            if item in huffman_str and huffman_str.index(item) == 0:
                ret += char_frequency[i][0]
                huffman_str = huffman_str[len(item):]
            i += 1

    return ret


if __name__ == '__main__':

    text = "Это оригинальная строка!!!!"

    char_frequency = list(Counter(text).items())

    nodes = create_nodes([x[1] for x in char_frequency])
    root = create_huffman_tree(nodes)
    codes = huffman_encoding(nodes, root)

    huffman_str = encode_str(text, char_frequency, codes)
    origin_str = decode_str(huffman_str, char_frequency, codes)

    print("Оригинальная строка: " + text)
    print("Кодированная строка: " + huffman_str)
    print("Раскодированная строка: " + origin_str)

"""
Оригинальная строка: Это оригинальная строка!!!!
Кодированная строка: 111000111001101000110111100111011100110101011110111111101010000010100001011110110010110010100100100100
Раскодированная строка: Это оригинальная строка!!!!
"""
