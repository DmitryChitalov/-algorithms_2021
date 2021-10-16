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


from collections import Counter, deque, namedtuple
from heapq import heappop, heappush, heapify


class HuffmanCode:

    table = {}
    memory_for_tree = {}

    def __init__(self, data):
        self.data = data

    def create_tree(self, show=False):
        sorted_frequency_analysis = deque(sorted(Counter(self.data).items(), key=lambda item: item[1]))
        data = sorted_frequency_analysis
        if len(data) != 1:
            while len(data) > 1:

                weight = data[0][1] + data[1][1]
                branch = {'left': data.popleft()[0],
                          'right': data.popleft()[0]}

                for num, weight_branch in enumerate(data):
                    if weight > weight_branch[1]:
                        continue
                    else:
                        data.insert(num, (branch, weight))
                        break
                else:
                    data.append((branch, weight))
        else:
            weight = data[0][1]
            branch = {'left': sorted_elements.popleft()[0], 'right': None}
            data.append((branch, weight))

        if show:
            print(data[0][0])
        self.memory_for_tree = data[0][0]
        return data[0][0]

    def create_table(self, tree={}, path=''):
        if not tree:
            tree = self.memory_for_tree
        if not isinstance(tree, dict):
            self.table[tree] = path
        else:
            self.create_table(tree['left'], path=f'{path}0')
            self.create_table(tree['right'], path=f'{path}1')

    def encode(self, show=False):
        result = ''.join([self.table[el] for el in self.data])
        if show:
            print(result)
        return result

    def decode(self, show=False):
        result = []
        current_ch = ''
        for encrypted_ch in self.data:
            current_ch += encrypted_ch
            for decrypted_ch in self.table:
                if self.table.get(decrypted_ch) == current_ch:
                    result.append(decrypted_ch)
                    current_ch = ""
                    break

        result = ''.join(result)

        if show:
            print(result)
        return result

    def show_table(self):
        for el, num in self.table.items():
            print(el, ':', num)


if __name__ == '__main__':

    example = HuffmanCode('загадка Жака Фреско')
    example.create_tree()
    example.create_table()
    example.show_table()
    example.encode(show=True)

    example = HuffmanCode('000010000110011011110001011110111100010100010111010110111111100')
    example.table = {'з': '0000', 'г': '0001', ' ': '001', 'Ф': '0100', 'р': '0101', 'д': '0110',
                     'Ж': '0111', 'а': '10', 'о': '1100', 'е': '11010', 'с': '11011', 'к': '111'}
    example.decode(show=True)
