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


# Получаем из дерева коды символов передаваемой строки.
def get_code(root, codes=None, code=''):
    if codes is None:
        codes = dict()
    if root is None:
        return
    if isinstance(root.value, str):
        codes[root.value] = code
        return codes
    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')
    return codes


# Строим дерево
def get_tree(string):
    string_count = Counter(string)
    if len(string_count) <= 1:
        node = Node(None)
        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)
        string_count = {node: 1}
    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]
        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])
        else:
            node.left = spam[0][0]
        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])
        else:
            node.right = spam[1][0]
        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]
    return [key for key in string_count][0]


# Кодируем строку полученными кодами
def coding(string, codes):
    res = ''
    for symbol in string:
        res += codes[symbol]
    return res


# Декодируем строку
def decoding(string, codes):
    res = ''
    i = 0
    while i < len(string):
        for code in codes:
            if string[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])
    return res


some_string = 'beep boop beer!'
tree = get_tree(some_string)
codes = get_code(tree)
coding_str = coding(some_string, codes)
decoding_str = decoding(coding_str, codes)
print(f'Коды символов: {codes}')
print('Первоначальная строка: ', some_string)
print('Закодированная строка: ', coding_str)
print('Декодированная строка: ', decoding_str)
