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

from collections import Counter, namedtuple
import heapq


class Node(namedtuple("Node", ["left", "right"])):
   def walk(self, code, acc):
       self.left.walk(code, acc + "0")
       self.right.walk(code, acc + "1")


class Leaf(namedtuple("leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    [(_freq, _count, root)] = h
    code = {}
    root.walk(code, "")
    return code


def main():
    s = input("Введите вашу фразу: ")
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(f"Исходная строка: {s}")
    print(f"Закодированная строка: {encoded}")


if __name__ == "__main__":
    main()
