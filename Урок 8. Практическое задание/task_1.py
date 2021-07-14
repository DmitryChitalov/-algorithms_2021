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
"""Хаффман через коллекции"""

from collections import Counter, deque, defaultdict


def haffman_tree(s):
    counter = Counter(s)
    sorted_el = deque(sorted(counter.items(), key=lambda item: item[1]))
    if len(sorted_el) != 1:
        while len(sorted_el) > 1:
            weight = sorted_el[0][1] + sorted_el[1][1]
            comb = {0: sorted_el.popleft()[0],
                    1: sorted_el.popleft()[0]}
            for i, _counter in enumerate(sorted_el):
                if weight <= _counter[1]:
                    sorted_el.insert(i, (comb, weight))
                    break
                else:
                    continue
            else:
                sorted_el.append((comb, weight))
    else:
        weight = sorted_el[0][1]
        comb = {0: sorted_el.popleft()[0], 1: None}
        sorted_el.append((comb, weight))
    return sorted_el[0][0]


code_table = defaultdict()  # Изменил на использование defaultdict


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


print('Хаффман через коллекции:', end=' ')
s = "beep boop beer!"
print(s, '\n')
haffman_code(haffman_tree(s))
# Изменил вывод  соответствия кода для каждого символа
for c in sorted(code_table):  # алфавитном порядке работает функция sorted()
    print(f'{c}: {code_table[c]}')  # соответствие: символ и соответствующий ему код

print('')

"""Хаффман через ООП"""


class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def nodes(self):
        return self.left, self.right

    def __str__(self):
        return f'{self.left}_{self.right}'  # изменил на f-строки


def huffman_code_tree(node, left=True, bin_string=''):
    if type(node) is str:
        return {node: bin_string}
    l, r = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, f'{bin_string}0'))
    d.update(huffman_code_tree(r, False, f'{bin_string}1'))
    return d


print('Хаффман через ООП:', end=' ')
string = 'beep boop beer!'
print(string, '\n')

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    key1, c1 = nodes[-1]
    key2, c2 = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

for char, frequency in sorted(freq):  # алфавитном порядке работает функция sorted()
    print(f'{char}: {huffmanCode[char]}')  # соответствие: символ и соответствующий ему код
