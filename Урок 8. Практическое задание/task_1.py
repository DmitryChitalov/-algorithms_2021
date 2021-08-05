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
import heapq  # Взял очередь с приоритетом, потому что так удобнее работать с частотами символов, по сути это

# двоичная куча.
"""Получилось не совсем честно, я делал уже реализацию этого алгоритма на другом обучении. Приведу данный код, 
добавив комментарии """


class Node(namedtuple('Node', ['left', 'right'])):  # структура и перегруженный метод обхода внутренного узла дерева
    def walk(self, code, acc):  # асс тут - префикс кода, который мы накопили, спускаясь от узла к листу
        self.left.walk(code, acc + '0')  # спускаемся в левого потомка, добавляя 0 к префиксу
        self.right.walk(code, acc + '1')  # спускаемся в правого потомка, добавляя 1 к префиксу


class Leaf(namedtuple('Leaf', ['char'])):  # структура и перегруженный метод обхода листа, хранящий символ
    def walk(self, code, acc):
        code[self.char] = acc or '0'  # запишем в словарь построенный код для данного символа или 0 для пустых строк


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))  # создаем список пар символов и их частот. len тут только чтобы уйти от
        # сравнения последнего компонента в очереди

    heapq.heapify(h)  # Сбрасываем его в очередь с приоритетами
    count = len(h)
    while len(h) > 1:  # Пока в очереди есть хотя бы два элемента
        freq1, _count1, left = heapq.heappop(h)  # достает из кучи элемент с МИНИМАЛЬНОЙ частотой
        freq2, _count2, right = heapq.heappop(h)  # следующий элемент с МИНИМАЛЬНОЙ частотой
        heapq.heappush(h, (freq1 + freq2, count, Node(left,
                                                      right)))  # обратно закидываем элемент, частота которого равна
        # сумме частот минимальных элементов, а значение - новый внутренний узел
        count += 1

    code = {}
    if h:  # Проверим, есть ли что обходить в очереди
        [(_freq, _count, root)] = h  # нам нужен только корень, остальное не нужно
        root.walk(code, '')  # пробегаем в соотствествии с методами, заполняя словарь, который надо вернуть
    return code  # Получим словарь с символами и их кодами


if __name__ == '__main__':
    s = 'Wrap your head around something'
    code = huffman_encode(s)
    encoded = ''.join([code[ch] for ch in s])
    print(encoded)

# Вывод
# 10110111100010111010110000010110111101001111000000100101000011110010110101010010101100100111010100011011011111100101011101
