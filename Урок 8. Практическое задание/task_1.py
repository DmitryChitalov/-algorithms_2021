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
import collections


class Node:
    def __init__(self, root=None, frequency=None, letter=None, left=None, right=None, weight=0):
        self.root = root
        self.frequency = frequency
        self.letter = letter
        self.left = left
        self.right = right
        self.weight = weight

    def add_left(self, new_node):
        self.left = new_node

    def add_right(self, new_node):
        self.right = new_node

    def is_leaf(self):
        return (not self.right) & (not self.left)


def nodes_deque(str_):
    freq_table = collections.Counter(str_)
    return collections.deque(
        sorted([Node(frequency=elem[1], letter=elem[0])
                for elem in freq_table.items()], key=lambda item: item.frequency))


print(*[(elem.frequency, elem.letter) for elem in nodes_deque('beer bear bear')])


def build_haffman_tree(deque_):
    if len(deque_) != 1:
        while len(deque_) > 1:
            new_node = Node()
            elem = deque_.popleft()
            new_node.add_left(Node(frequency=elem.frequency, letter=elem.letter, left=elem.left, right=elem.right))
            elem = deque_.popleft()
            new_node.add_right(Node(frequency=elem.frequency, letter=elem.letter, left=elem.left, right=elem.right,
                                    weight=1))
            new_node.frequency = new_node.left.frequency + new_node.right.frequency
            for i in range(len(deque_)):
                if deque_[i].frequency < new_node.frequency:
                    continue
                else:
                    deque_.insert(i, new_node)
                    break
            else:
                new_node.weight = None
                deque_.append(new_node)

    return deque_[0]


code = dict()


def haffman_code(haffman_tree, path=''):
    if haffman_tree.is_leaf():
        code.update({haffman_tree.letter: path})
    else:
        haffman_code(haffman_tree.left, path=path + '0')
        haffman_code(haffman_tree.right, path=path + '1')
    return code


s = "beep boop beer!"
ht = build_haffman_tree(nodes_deque(s))
hc = haffman_code(ht)
print(ht)
print(haffman_code(ht))
for i in s:
    print(hc[i], end=' ')
