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

string = "beep boop beer!"
code_table = dict()


class Haff():
    def __init__(self, s):
        self.s = s
        self.code_table = dict()
        self.sorted_element = deque()

    def haf_sort(self):
        count = Counter(self.s)
        sorted_element = deque(sorted(count.items(), key=lambda item: item[1]))
        if len(sorted_element) != 1:
            while len(sorted_element) > 1:
                volume = sorted_element[0][1] + sorted_element[1][1]
                comb = {0: sorted_element.popleft()[0],
                        1: sorted_element.popleft()[0]}

                for i, val in enumerate(sorted_element):
                    if volume > val[1]:
                        continue
                    else:
                        sorted_element.insert(i, (comb, volume))
                        break
                else:
                    sorted_element.append((comb, volume))
        else:
            volume = sorted_element[0][1]
            comb = {0: sorted_element.popleft()[0], 1: None}
            sorted_element.append((comb, volume))
        self.sorted_element = sorted_element[0][0]

    def haf_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.haf_code(tree[0], path=f'{path}0')
            self.haf_code(tree[1], path=f'{path}1')

    def print_code(self):
        self.haf_sort()
        self.haf_code(self.sorted_element)
        return " ".join(self.code_table.values())

    def insert_str(self, s):
        self.s = s


my_object = Haff(string)
print(my_object.print_code())
