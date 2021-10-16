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

from collections import deque


class BTNode:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"[left=<{str(self.left)}>, right=<{str(self.right)}>, value={str(self.value)}]"


def hoffman_encode(s: str):

    alphabet = set(s)
    freq = dict(sorted({c: s.count(c) for c in alphabet}.items(), key=lambda item: item[1], reverse=True))
    que = deque()

    for key, val in freq.items():
        que.append(BTNode(val, key))

    while len(que) > 1:
        left = que.pop()
        right = que.pop()
        if left.right is None and right.right is None:
            que.append(BTNode(left.value + right.value, left.left, right.left))
        elif left.right is None and right.right is not None or left.right is not None and right.right is None:
            que.append(BTNode(left.value + right.value,
                              left.left if left.right is None else right.left,
                              right if left.right is None else left))
        else:
            que.append(BTNode(left.value + right.value, left, right))

        que = sorted(que, key=lambda q: q.value, reverse=True)

    encoder_dict = {}

    def char_code_builder(q: BTNode, path=[]):

        path.append('0')
        if isinstance(q.left, BTNode):
            char_code_builder(q.left, path)
        else:
            encoder_dict[q.left] = ''.join(path)
        path.pop()

        path.append('1')
        if isinstance(q.right, BTNode):
            char_code_builder(q.right, path)
        else:
            encoder_dict[q.right] = ''.join(path)
        path.pop()

    char_code_builder(que.pop())
    # print(encoder_dict)
    return ''.join([encoder_dict[ch] for ch in s])


# hoffman_encode('beep boop beer!')
print(hoffman_encode('beep boop beer!'))
