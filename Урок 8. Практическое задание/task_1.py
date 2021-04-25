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


class Haffman():
    def __init__(self, str):
        self.str = str
        self.code_table = dict()
        self.sorted_element = deque()

    def haffman_sorted(self):
        count = Counter(self.str)
        sorted_element = deque(sorted(count.items(), key=lambda item: item[1]))
        if len(sorted_element) != 1:
            while len(sorted_element) > 1:
                sum = sorted_element[0][1] + sorted_element[1][1]
                comb = {0: sorted_element.popleft()[0],
                        1: sorted_element.popleft()[0]}

                for i, count in enumerate(sorted_element):
                    if sum > count[1]:
                        continue
                    else:
                        sorted_element.insert(i, (comb, sum))
                        break
                else:
                    sorted_element.append((comb, sum))
        else:
            summ = sorted_element[0][1]
            comb = {0: sorted_element.popleft()[0], 1: None}
            sorted_element.append((comb, summ))
        self.sorted_element = sorted_element[0][0]

    def haffman_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.haffman_code(tree[0], path=f'{path}0')
            self.haffman_code(tree[1], path=f'{path}1')

    def print_code(self):
        self.haffman_sorted()
        self.haffman_code(self.sorted_element)
        return " ".join(self.code_table.values())

    def insert_str(self, str):
        self.str = str


str = Haffman(input("Строка: "))
print(str.print_code())
