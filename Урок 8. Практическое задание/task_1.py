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

code_table = {}


class HaffCode:

    def __init__(self, simple_str):
        self.simple_str = simple_str
        self.tree = self.haff_tree()
        self.code = self.haff_code(self.tree)
        self.str = self.str_code()

    def haff_tree(self):
        count = Counter(self.simple_str)
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

    def haff_code(self, tree, path=''):
        if not isinstance(tree, dict):
            code_table[tree] = path
        else:
            self.haff_code(tree[0], path=f'{path}0')
            self.haff_code(tree[1], path=f'{path}1')
        return code_table

    def str_code(self, code_str=''):
        for i in self.simple_str:
            code_str += f'{self.code[i]} '
        return code_str


new_str = "beep boop beer!"
func = HaffCode(new_str)
print(func.str)
