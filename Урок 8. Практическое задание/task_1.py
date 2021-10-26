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


# Используем heapq — Алгоритм очереди кучи

import heapq
from collections import Counter, namedtuple


# Класс "ветвей"
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


# Класс "листьев"
class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"



def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    # Преобразум список h в кучу на месте за линейное время
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        # извлекаем два последовательных минимальных элемента из кучи
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        #  Помещаем значение, сохраняя инвариантность кучи
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code



def main():
    s = input("Введите строку для кодирования: ")
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(f'Кол-во символов: {len(code)}, Длина кода Хаффмана: {len(encoded)}')
    for ch in sorted(code):
        print(f'Символ: {ch}, Код: {code[ch]}')
    print(f'Код Хаффмана: {encoded}')



if __name__ == "__main__":
    main()

"""
Работает при нулевой строке:
Введите строку для кодирования: 
Кол-во символов: 0, Длина кода Хаффмана: 0

Работает при одном символе: 
Введите строку для кодирования: a
Кол-во символов: 1, Длина кода Хаффмана: 1
Символ: a, Код: 0
0

"""