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

from collections import Counter, deque


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def create_huffman_tree(s):
    count = Counter(s)  # подсчет уникальных символов
    sorted_deque = deque(sorted(count.items(), key=lambda item: item[1]))  # сортируем символы
    del count  # освобождаем память
    if len(sorted_deque) != 1:
        while len(sorted_deque) > 1:
            weight = sorted_deque[0][1] + sorted_deque[1][1]  # складываем частоту двух первых элементов
            new_node = Node(left=sorted_deque.popleft()[0],
                            right=sorted_deque.popleft()[0])  # создаем новый узел с потомками
            for i, amount in enumerate(sorted_deque):  # ищем позицию для вставки узла
                if weight > amount[1]:
                    continue
                else:
                    sorted_deque.insert(i, (new_node, weight))
                    break
            else:
                sorted_deque.append((new_node, weight))  # в конце цикла добавляем в дек последний объединенный элемент
    else:
        weight = sorted_deque[0][1]
        new_node = Node(left=sorted_deque.popleft()[0])
        # если был передан только один символ, он добавляется в узел как левый потомок
        sorted_deque.append((new_node, weight))
    return sorted_deque[0][0]


code_table = dict()


def huffman_encoding(tree, code=''):
    if not isinstance(tree, Node):
        code_table[tree] = code
    else:
        huffman_encoding(tree.left, code=f'{code}0')  # рекурсивно находим код элемента
        huffman_encoding(tree.right, code=f'{code}1')


string = "beep boop beer!"

huffman_encoding(create_huffman_tree(string))
print(code_table)
for i in string:
    print(code_table[i], end=' ')
