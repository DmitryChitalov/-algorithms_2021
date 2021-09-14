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


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def branch(self):
        return self.left, self.right


def haffman_tree(node, code=""):  # Нахождение кода элемента с помощью рекурсии
    if type(node) is str:
        return {node: code}
    l, r = node.branch()
    res = {}
    # 0 - налево, 1 - направо
    res.update(haffman_tree(l, f'{code}0'))
    res.update(haffman_tree(r, f'{code}1'))
    return res


text = "beep boop beer!"
print(f'Исходная строка: {text}')
count = Counter(text)  # Подсчёт частоты символов
tree = count.items()
del count

while len(tree) > 1:
    tree = sorted(tree, key=lambda item: item[1])  # Сортировка символов по частоте
    char1, count1 = tree[0]
    char2, count2 = tree[1]
    tree = deque(tree[2:])
    tree.appendleft((Node(char1, char2), count1 + count2))

del char1, char2, count1, count2
code_table = haffman_tree(tree[0][0])  # Таблица кодов элементов
del tree

coded = [code_table[char] for char in text]  # Список символов в закодированном виде

print(f'Закодированная строка: {"".join(coded)}')
