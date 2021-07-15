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

"""
    решил взять и разобрать кодировку из интернета, мне она показалась более понятной
"""
import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", 'right'])):  # Класс для узлов дерева
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")  # acc - код который мы накопили спускаясь от корня до данного узла
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):  # Класс для листьев
    def walk(self, code, acc):
        code[self.char] = acc or "0"  # or '0' нужен на случай если на вход подали только 1 символ


def huffman_encode(s):
    h = []  # создаем список и наполняем его нашими элементами как листьями
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)  # преобразовываем список в кучу
    # count необходим для heappush, без него в случае 2 одинаковых по количеству
    # элемментов она начинает сравнивать строку с классом
    count = len(h)
    while len(h) > 1:  # строим узлы пока есть хотябы 2 элемента
        freq1, _count1, left = heapq.heappop(h)  # доставем элемент с минимальной частотой
        freq2, _count2, right = heapq.heappop(h)  # и следующий за ним с минимальной частотой
        # создаем новый элемент равный сумме частот двух взятых
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = dict()
    # Обходим дерево только если есть строки, на случай если на вход подали пустую строку
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def main(): # запрашиваем строку и кодируем её
    s = input()
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s) # соединяем код в 1 строку
    print(len(code), len(encoded)) # выводим сперва сколько всего символов закодировано, затем длинну кода
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch])) # выводим код каждого символа
    print(encoded) # выводим конечный код

if __name__ == '__main__':
    main()
