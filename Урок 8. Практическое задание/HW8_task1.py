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


class Haffman:
    def __init__(self, text_string):
        self.text_string = text_string
        new_dict = dict()
        new_deque = deque()
        self.code = new_dict
        self.haffman_tree = new_deque

        print(self.text_string)

    def get_tree(self):
        count = Counter(self.text_string)
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
        print (sorted_elements[0][0])
        return sorted_elements[0][0]

    def get_code(self):
        way = ''
        code_dict = dict()
        current_tree = self.haffman_tree
        result_dict = self.call_code(code_dict, current_tree, way)
        self.code = result_dict
        print(self.code)

    def call_code(self, code_dict, current_tree, way):
        if not isinstance(current_tree, dict):
            code_dict[current_tree] = way
        else:
            self.call_code(current_tree[0], way=f'{way}0')
            self.call_code(current_tree[1], way=f'{way}1')
        return code_dict

    def change_string(self, new_string):
        self.string = new_string;
        self.haffman_tree = get_tree()
        self.code = get_code()

    def print_code(self):
        print(self.code)

    def print_tree(self):
        print(self.haffman_tree)


haffman_line = Haffman("Long live the Queen")
haffman_line.get_tree()
haffman_line.get_code()
haffman_line.print_tree()
haffman_line.print_code()


    