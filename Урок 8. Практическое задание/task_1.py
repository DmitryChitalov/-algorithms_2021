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


class HuffmanCoding:
    def __init__(self, input_string):
        self.input_string = input_string
        self.code_table = dict()

    def huffman_tree(self):
        count = Counter(self.input_string)
        sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
        if len(sorted_elements) != 1:
            while len(sorted_elements) > 1:
                weight = sorted_elements[0][1] + sorted_elements[1][1]
                nodes = {0: sorted_elements.popleft()[0],
                         1: sorted_elements.popleft()[0]}
                for i, val in enumerate(sorted_elements):
                    if weight > val[1]:
                        continue
                    else:
                        sorted_elements.insert(i, (nodes, weight))
                        break
                else:
                    sorted_elements.append((nodes, weight))
        else:
            weight = sorted_elements[0][1]
            nodes = {0: sorted_elements.popleft()[0], 1: None}
            sorted_elements.append((nodes, weight))
        return sorted_elements[0][0]

    def huffman_code_table(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.huffman_code_table(tree[0], path=f'{path}0')
            self.huffman_code_table(tree[1], path=f'{path}1')
        return self.code_table

    def huffman_code(self):
        code_str = ''
        lst = []
        for i in self.input_string:
            code_str += self.code_table[i]
        while code_str != '':
            lst.append(code_str[0:4])
            code_str = code_str[4:]
        return ' '.join(lst)


test_string = HuffmanCoding("beep boop beer!")

print(test_string.huffman_tree())
print(test_string.huffman_code_table(test_string.huffman_tree()))
print(test_string.huffman_code())


