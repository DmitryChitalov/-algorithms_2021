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


class HaffmanTree:

    def __init__(self, words):
        self.count_elements = Counter(words)

    def sorted_tree(self):
        sorted_elements = deque(sorted(self.count_elements.items(), key=lambda item: item[1]))
        return sorted_elements

    def create_tree(self):
        sorted_elements = self.sorted_tree()
        if len(sorted_elements) != 1:
            while len(sorted_elements) > 1:
                weight = sorted_elements[0][1] + sorted_elements[1][1]
                comb = {0: sorted_elements.popleft()[0],
                        1: sorted_elements.popleft()[0]}
                for i, _count in enumerate(sorted_elements):
                    if weight > _count[1]:
                        continue
                    else:
                        # Вставляем объединенный элемент
                        sorted_elements.insert(i, (comb, weight))
                        break
                else:
                    sorted_elements.append((comb, weight))
        else:
            weight = sorted_elements[0][1]
            comb = {0: sorted_elements.popleft()[0], 1: None}
            sorted_elements.append((comb, weight))
        return sorted_elements[0][0]


class HaffmanCode(HaffmanTree):

    def __init__(self, words):
        self.count_elements = Counter(words)
        self.tree = self.create_tree()

    def create_code(self):
        code_table = dict()
        tree = self.tree

        def haffman_code(tree, path=''):
            # Если элемент не словарь, значит мы достигл
            # и заносим его, а так же его код в словарь
            if not isinstance(tree, dict):
                code_table[tree] = path
            # Если элемент словарь, рекурсивно спускаемс
            # по первому и второму значению (левая и пра
            else:
                haffman_code(tree[0], path=f'{path}0')
                haffman_code(tree[1], path=f'{path}1')
        haffman_code(tree)
        return code_table

    def __str__(self):
        return '; '.join([f'{i}: {j}' for i, j in self.create_code().items()])


if __name__ == '__main__':
    a = HaffmanTree('beep boop beer!')
    b = HaffmanCode('beep boop beer!')
    print(a)
    print(b)
