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
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(root, codes=dict(), code=''):
    if root is None:
        return
    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')

    return codes


def get_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        node = Node(None)

        if len(string_count) == 1:
            node.left = Node([j for j in string_count][0])
            node.right = Node(None)

        string_count = {node: 1}

    while len(string_count) != 1:
        node = Node(None)
        s = string_count.most_common()[:-3:-1]
        if isinstance(s[0][0], str):
            node.left = Node(s[0][0])
        else:
            node.left = s[0][0]
        if isinstance(s[1][0], str):
            node.right = Node(s[1][0])
        else:
            node.right = s[1][0]

        del string_count[s[0][0]]
        del string_count[s[1][0]]
        string_count[node] = s[0][1] + s[1][1]

    return [i for i in string_count][0]


def coding(string, codes):
    result = ''
    for n in string:
        result += codes[n]
    return result


my_string = input('Enter string to encode: ')
tree = get_tree(my_string)
codes = get_code(tree)
print('Code:', codes)
coding_str = coding(my_string, codes)
print('Encoded string: ', coding_str)
