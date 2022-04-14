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
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def checking(self, code, acc):
        self.left.checking(code, acc + "0")
        self.right.checking(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def checking(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    priority_queue = []
    cont = Counter(s)
    for ch, frequency in cont.items():
        priority_queue.append((frequency, len(priority_queue), Leaf(ch)))
    heapq.heapify(priority_queue)
    count = len(priority_queue)
    while len(priority_queue) > 1:
        frequency1, _count1, left = heapq.heappop(priority_queue)
        frequency2, _count2, right = heapq.heappop(priority_queue)

        heapq.heappush(priority_queue, (frequency1 + frequency2, count, Node(left, right)))
        count += 1
    code = {}
    if priority_queue:
        [(_num, _count, root)] = priority_queue
        root.checking(code, "")
    return code


def huffman_decode(encoded, code):
    dec_list = []
    enc_ch = ""
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                dec_list.append(dec_ch)
                enc_ch = ""
                break
    return "".join(dec_list)


def main():
    str = input('Введите строку: ')
    code = huffman_encode(str)
    encoded = "".join(code[ch] for ch in str)
    for ch in sorted(code):
        print(f'Символ {ch} - код {code[ch]}')
    print(f'Код строки: {encoded}')
    print(f'Раскодированная строка: {huffman_decode(encoded, code)}')


if __name__ == "__main__":
    main()
