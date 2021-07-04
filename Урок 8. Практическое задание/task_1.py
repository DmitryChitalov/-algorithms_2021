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


class Huffman:
    def __init__(self, string):
        self.string = str(string)
        self.table = {}

    def tree(self):
        arr = deque(sorted(Counter(self.string).items(), key=lambda x: x[1]))
        if len(arr) > 1:
            while len(arr) > 1:
                amount = arr[0][1] + arr[1][1]
                node = {0: arr.popleft()[0],
                             1: arr.popleft()[0]}
                for index, arguments in enumerate(arr):
                    if amount > arguments[1]:
                        continue
                    else:
                        arr.insert(index, (node, amount))
                        break
                else:
                    arr.append((node, amount))
        else:
            amount = arr[0][1]
            node = {0: arr.popleft()[0], 1: None}
            arr.append((node, amount))
        return arr[0][0]

    def code_table(self, tree, path=''):
        if not isinstance(tree, dict):
            self.table[tree] = path
        else:
            self.code_table(tree[0], path=f'{path}0')
            self.code_table(tree[1], path=f'{path}1')
        return self.table

    def encoding(self):
        encoded_string = ''
        for i in self.string:
            encoded_string += self.table[i] + ' '
        return encoded_string

    def decoding(self):
        decoded_string = ''
        for item in self.encoding().split(' '):
            for key, value in self.table.items():
                if value == item:
                    decoded_string += key
        return decoded_string


string = Huffman("beep boop beer!")

print('Словарь:', string.code_table(string.tree()))
print('Кодированная строка:', string.encoding())
print('Раскодированная строка:', string.decoding())

"""
вывод
Словарь: {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
Кодированная строка: 00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001 
Раскодированная строка: beep boop beer!
"""
