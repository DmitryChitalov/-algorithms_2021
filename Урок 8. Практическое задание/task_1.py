from collections import Counter
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


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def haffman_tree(string):
    dictionary = Counter(string)
    if len(dictionary) <= 1:
        return
    while True:
        node = Node(None)
        less_count = dictionary.most_common()[:-3:-1]
        if len(dictionary) == 1:
            node.left = Node([key for key in dictionary][0])
            node.right = Node(None)
            break
        if isinstance(less_count[0][0], str):
            node.left = Node(less_count[0][0])
        else:
            node.left = less_count[0][0]
        if isinstance(less_count[1][0], str):
            node.right = Node(less_count[1][0])
        else:
            node.right = less_count[1][0]
        del dictionary[less_count[0][0]]
        del dictionary[less_count[1][0]]
        dictionary[node] = less_count[0][1] + less_count[1][1]
    return [key for key in dictionary][0]


def code(node, bits=None, bit=''):
    if node is None:
        return
    if bits is None:
        bits = dict()
    if isinstance(node.value, str):
        bits[node.value] = bit
        return bits
    code(node.left, bits, bit + '0')
    code(node.right, bits, bit + '1')
    return bits


def coding(string, bits):
    result = ''
    for symbol in string:
        result += bits[symbol]
    return result


def decoding(string, bits):
    result = ''
    i = 0
    while i < len(string):
        for bit in bits:
            if string[i:].find(bits[bit]) == 0:
                result += bit
                i += len(bits[bit])
    return result


usr_str = 'beep boop beer!'
tree = haffman_tree(usr_str)
coding_str = coding(usr_str, code(tree))
decoding_str = decoding(coding_str, code(tree))
print(f'Original string : {usr_str}\n'
      f'Encoded string : {coding_str}\n'
      f'Decoded string : {decoding_str}\n')

# 0011111010100001101110101000111110001001  Сжата методом из примера на вебинаре
# 0011110110100010110101101000111110011000  Сжато этим метадом
# Вроде все верно, но они разные. Не совсем понял почему
