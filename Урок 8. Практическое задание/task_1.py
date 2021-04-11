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
from collections import Counter, deque, namedtuple
import heapq
from timeit import timeit

"""УРОЧНАЯ РЕАЛИЗАЦИЯ"""


def haffman_tree(s):
    count = Counter(s)
    sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))

    if len(sorted_elements) != 1:
        while len(sorted_elements) > 1:
            weight = sorted_elements[0][1] + sorted_elements[1][1]
            comb = {0: sorted_elements.popleft()[0],
                    1: sorted_elements.popleft()[0]}
            for i, _count in enumerate(sorted_elements):
                if weight > _count[1]:
                    continue
                else:
                    sorted_elements.insert(i, (comb, weight))
                    break
            else:
                sorted_elements.append((comb, weight))
    else:
        weight = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, weight))

    return sorted_elements[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


s = 'beep boop bear!'

haffman_code(haffman_tree(s))

for i in s:
    print(code_table[i], end=' ')
print()

time = timeit("haffman_code(haffman_tree(s))", globals=globals(), number=10000)
print(f'Время выполнения этого варианта кодировки - {time}')
# ------> 0.0849734

"""C ПРИМЕНЕНИЕМ НОВОЙ БИБЛИОТЕКИ"""

# Создаем классы для хранения структуры дерева


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):  # обход по дереву
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):   # функция для листьев
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))  # создаём список частоты символов
    heapq.heapify(h)  # преобразовываем его в кучу("эмбрион дерева")
    count = len(h)
    while len(h) > 1:  # осуществляем создание дерева, в принципе, почти, как на уроке
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)  # heappop возвращает и удаляет наименьший элемент кучи

        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))  # heappush - pop, но с сохранением инварианта

        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")

    return code


def main():
    s = 'beep boop bear!'
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(encoded)


print(f'Время выполнения этой кодировки - {timeit("main()", globals=globals(), number=1)}')  # -------> 3.0900000037e-05
"""
Вывод: c использованием встроенной функции на ТРИ порядка быстрее!!!!
"""
