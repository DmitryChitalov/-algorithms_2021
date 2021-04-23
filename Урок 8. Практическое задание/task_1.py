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
from collections import Counter
from collections import namedtuple


# класс для ветвей дерева - внутренних узлов; у них есть потомки
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        # чтобы обойти дерево нам нужно:
        self.left.walk(code, acc + "0")  # пойти в левого потомка, добавив к префиксу "0"
        self.right.walk(code, acc + "1")  # затем пойти в правого потомка, добавив к префиксу "1"


# класс для листьев дерева, у него нет потомков, но есть значение символа
class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"  # если строка длиной 1 то acc = "", для этого случая установим значение acc = "0"


def huffman_encode(s):
    elements = []
    for ch, frequency in Counter(s).items():
        elements.append(
            (frequency, Leaf(ch)))
    elements = deque(sorted(elements, key=lambda element: element[0]))
    while len(elements) > 1:
        freq1, left = elements.popleft()
        freq2, right = elements.popleft()
        weight = freq1 + freq2
        for i, count in enumerate(elements):
            if weight > count[0]:
                continue
            else:
                elements.insert(i, (weight, Node(left, right)))
                break
        else:
            elements.append((weight, Node(left, right)))
    code = {}
    if elements:
        [(_, root)] = elements
        root.walk(code, "")  # обойдем дерева от корня и заполним словарь для получения кода
    return code


# функция декодирования исходной строки по кодам Хаффмана
def huffman_decode(encoded, code):
    s_list = []
    enc_ch = ""
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                s_list.append(dec_ch)
                enc_ch = ""
                break
    return "".join(s_list)


if __name__ == "__main__":
    s = "beep boop beer!"
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(f"закодированная сторока: {encoded}")
    print("Коды символов:")
    for ch in code:
        print(f"{ch} : {code[ch]}")
    print(f"Раскодированная сторока:{huffman_decode(encoded, code)}")
