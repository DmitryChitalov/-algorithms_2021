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
import heapq
from collections import Counter, namedtuple


# Из всех вариантов мне понравился этот. Лаконичный.


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, a):
        self.left.walk(code, a + "0")
        self.right.walk(code, a + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, a):
        code[self.char] = a or "0"


def huffman(s):
    t = []
    for ch, freq in Counter(s).items():
        t.append((freq, len(t), Leaf(ch)))
    heapq.heapify(t)
    count = len(t)
    while len(t) > 1:
        freq1, _count1, left = heapq.heappop(t)
        freq2, _count2, right = heapq.heappop(t)
        heapq.heappush(t, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if t:
        [(_freq, _count, root)] = t
        root.walk(code, "")
    return code


def first():
    s = input("Введите строку, которую необходимо закодировать: ")
    code = huffman(s)
    coded = "".join(code[ch] for ch in s)
    print(f"В строке {len(code)} уникальных символов, каждому символу соответствует код: ")
    for ch in sorted(code):
        print(f"'{ch}' - {code[ch]}")
    print(f"Закодированная строка, длиной {len(coded)} знаков: {coded}.")


first()
