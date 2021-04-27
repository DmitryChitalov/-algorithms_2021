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


class TreeHaff:
    def __init__(self, int_str):
        self.int_str = int_str
        self.bin_cod = dict()
        self.code_make(self.tree_make())

    def count_sym(self):
        return Counter(self.int_str)

    def value_sort(self):
        return deque(sorted(self.count_sym().items(), key=lambda x: x[1]))

    def tree_make(self):
        val = self.value_sort().copy()
        if len(val) != 1:
            while len(val) > 1:
                mass = val[0][1] + val[1][1]
                join_elem = {0: val.popleft()[0],
                             1: val.popleft()[0]}
                for i, el in enumerate(val):
                    if mass > el[1]:
                        continue
                    else:
                        val.insert(i, (join_elem, mass))
                        break
                else:
                    val.append((join_elem, mass))
        else:
            mass = val[0][1]
            join_elem = {0: val.popleft()[0], 1: None}
            val.append((join_elem, mass))
        return val[0][0]

    def code_make(self, tr, path=''):
        if not isinstance(tr, dict):
            self.bin_cod[tr] = path
        else:
            self.code_make(tr[0], path=f'{path}0')
            self.code_make(tr[1], path=f'{path}1')

    def get_string_code(self):
        bin_str = ''
        for i in self.int_str:
            bin_str += self.bin_cod[i]
        return bin_str


if __name__ == '__main__':
    test_str = 'to be or not to be that is the question'
    haf = TreeHaff(test_str)
    print(f'Готовое дерево:\n{haf.tree_make()}')
    print(f'{50 * "*"}')
    print(f'Словарь "бинарников":\n{haf.bin_cod}')
    print(f'{50 * "*"}')
    print(f'Строка "бинарников":\n{haf.get_string_code()}')
