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


class Node(namedtuple('Node', ['left', 'right'])):

    def walk(self, code, acc):

        self.left.walk(code, acc + '0')

        self.right.walk(code, acc + '1')


class Desk(namedtuple('Desk', ['symbol'])):

    def walk(self, code, acc):

        code[self.symbol] = acc or '0'


def huffman(s):

    bd = []

    for sym, f in Counter(s).items():

        bd.append((f, len(bd), Desk(sym)))

    heapify(bd)

    cnt = len(bd)

    while len(bd) > 1:

        f1, _cnt1, left = heappop(bd)

        f2, _cnt2, right = heappop(bd)

        heappush(bd, (f1 + f2, cnt, Node(left, right)))

        cnt += 1

    code = {}

    if bd:

        [(_f, _cnt, root)] = bd

        root.walk(code, '')

    return code


s = input('Введите текст: ')

code = huffman(s)

encoded = ''.join(code[sym] for sym in s)

print(f'Код по Хаффману: {encoded}\n')

for sym in sorted(code):

    print(f'{sym} : {code[sym]}')


def decode(encode, input_code):

    arr = []

    encoded_char = ""

    for i in encode:

        encoded_char += i

        for j in input_code:

            if code.get(j) == encoded_char:

                arr.append(j)

                encoded_char = ""

                break

    return "".join(arr)


print(f'\nДекодирование: {decode(encoded, code)}')