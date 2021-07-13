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


# Решил попробовать второй путь, через ООП
from collections import Counter, deque


# листок будет хранить значения и вес, может иметь двух детей, если является узлом
class Leaf:
    def __init__(self, pair):
        self.symbol = pair[0]
        self.weight = pair[1]
        self.children = {}

    def create_children(self, left, right):
        self.children['left'] = left
        self.children['right'] = right

    def __repr__(self):
        return f'weight: {self.weight}, symbol: {self.symbol}'


# дерево принимает фразу при инициализации
class Tree:
    def __init__(self, phrase):
        c = Counter(phrase)
        # строим и сортируем наш дек из листьев
        self.weights = deque([Leaf(value) for value in sorted(c.items(), key=lambda x: (x[1]))])
        self.codes = {} # аттрибут для хранения итоговых кодов

        while len(self.weights) > 1:
            left_leaf = self.weights.popleft()
            right_leaf = self.weights.popleft()
            total_weight = left_leaf.weight + right_leaf.weight
            parent = Leaf((None, total_weight))
            parent.create_children(left_leaf, right_leaf)
            for position, el in enumerate(self.weights):
                if el.weight >= total_weight:
                    self.weights.insert(position, parent)
                    break
            else:
                self.weights.append(parent)

        self.root = self.weights[0]     # оставшийся элемент и будет наш корень
        self.get_codes()    # сразу же построим коды

    # функция для извлечения кодов, которую мы вызываем рекурсивно
    def get_codes(self, leaf=None, code=''):
        if leaf is None:
            leaf = self.root
        if not leaf.children:
            self.codes[leaf.symbol] = code
            return
        self.get_codes(leaf=leaf.children['left'], code=code + '0')
        self.get_codes(leaf=leaf.children['right'], code=code + '1')




my_tree = Tree('beep boop beer!')
# итоговый результат: {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}

