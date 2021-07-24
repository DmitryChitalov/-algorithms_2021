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
from heapq import heapify, heappop, heappush


class Tree(namedtuple("Tree", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_code_table(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, count1, left = heappop(h)
        freq2, count2, right = heappop(h)
        heappush(h, (freq1+freq2, count, Tree(left, right)))
        count += 1
    code = {}
    if h:
        [(freq, count, root)] = h
        root.walk(code, "")
    return code


def transformed_string(s, table):
    encoded_text = ''.join(table[char] for char in s)
    return encoded_text


coded_string = input('Введите строку для кодирования: ')
code_table = huffman_code_table(coded_string)
encoded_str = transformed_string(coded_string, code_table)
print(code_table)
print(encoded_str)

"""
Способ решения подсмотрен по ссылке http://e-postulat.ru/index.php/Postulat/article/viewFile/617/638
Мне очень понравилось использование модуля heapq, жаль на лекциях не припомню его использование. По факту он нужен 
для упрощения поиска минимальных значений, так как heappop() по умолчанию удаляет из списка и возвращает минимальный 
элемент списка. Можно было искать каждый раз минимальное значение и суммировать, но так решение лаконичнее.
Класс дерево и класс листок по сути вспомогательные и нужны только для получения таблицы кодирования
"""