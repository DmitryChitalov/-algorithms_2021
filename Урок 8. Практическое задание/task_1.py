"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!
 версию алгоритма. Разрешается и приветствуется изменение имен переменных,
 выбор других коллекций, различные изменения и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к
решению.
"""
import heapq
from collections import Counter, namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_encode(string):
    hc = []
    for char, freq in Counter(string).items():
        hc.append((freq, len(hc), Leaf(char)))
    heapq.heapify(hc)
    count = len(hc)
    while len(hc) > 1:
        freq_1, count_1, left = heapq.heappop(hc)
        freq_2, count_2, right = heapq.heappop(hc)
        heapq.heappush(hc, (freq_1 + freq_2, count, Node(left, right)))
        count += 1
    code = dict()

    if hc:
        [(_freq, _count, root)] = hc
        root.walk(code, '')
    return code


def main():
    s = input('Введите строку для кодировки: \n')
    code = huffman_encode(s)
    encoded = ''.join(code[char] for char in s)
    print(len(code), len(encoded))
    for char in sorted(code):
        print(f'{char}: {code[char]}')
    print(encoded)


if __name__ == '__main__':
    main()

"""
Сначала создаем класс для узлов дерева, затем класс для листьев, далее идет 
функция реализации алгоритма Хаффмана.
функция main выполняет роль клиентского кода.
"""