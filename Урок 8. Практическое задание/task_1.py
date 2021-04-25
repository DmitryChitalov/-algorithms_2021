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
        self.__str = str
        self.__code_table = dict()
        self.__sorted_el = deque()

    def __haffman_sorted(self):
        count = Counter(self.__str)
        sorted_el = deque(sorted(count.items(), key=lambda item: item[1]))
        if len(sorted_el) != 1:
            while len(sorted_el) > 1:
                sum = sorted_el[0][1] + sorted_el[1][1]
                comb = {0: sorted_el.popleft()[0],
                        1: sorted_el.popleft()[0]}

                for i, count in enumerate(sorted_el):
                    if sum > count[1]:
                        continue
                    else:
                        sorted_el.insert(i, (comb, sum))
                        break
                else:
                    sorted_el.append((comb, sum))
        else:
            sum = sorted_el[0][1]
            comb = {0: sorted_el.popleft()[0], 1: None}
            sorted_el.append((comb, sum))
        self.__sorted_el = sorted_el[0][0]

    def __haffman_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.__code_table[tree] = path
        else:
            self.__haffman_code(tree[0], path=f'{path}0')
            self.__haffman_code(tree[1], path=f'{path}1')

    def print_code(self):
        self.__haffman_sorted()
        self.__haffman_code(self.__sorted_el)
        return " ".join(self.__code_table.values())

    def insert_str(self, str):
        self.__str = str


str = Haffman("Some string!")
print(str.print_code())
str.insert_str("Interesting string")
print(str.print_code())
"""
Создал класс, 
при создании объекта вводим строку. Код которой можно получить вызвав метотд print_code()
Вызвав метот insert_str() можно ввести новую строку
"""