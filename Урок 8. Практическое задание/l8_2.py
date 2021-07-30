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
from collections import Counter
from recordclass import recordclass
# Сделаю оговорку к выполнению задания. Согласно информации в кодировании Хаффамана
# «Битовые значения ветвей, исходящих от корня, не зависят от весов потомков». А, значит, соблюдать принцип, чтобы
# больша суммарная масса разветвления всегда была справа необязательно. Достаточно просто сооединять листья и узлы
# одной ступени, пока ступень позволяет соединять попарно элементы.
"""То есть для принципа Хаффмана кодирование букв из строки «Hello world!» будет принимать такой вид.
('H', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1), ('!', 1), ('o', 2), ('l', 3)
   ('H' + 'e', 2)      (' ' + 'w', 2)     ('r' + 'd', 2)      ('!' + 'o', 3)
        ('H' + 'e' + ' ' + 'w', 4)            ('r' + 'd' + '!' + 'o', 5)
               ('H' + 'e' + ' ' + 'w' + 'r' + 'd' + '!' + 'o', 9)
                           ('H' + 'e' + ' ' + 'w' + 'r' + 'd' + '!' + 'o' + 'l', 12)

H — 0000, e — 0001, ' ' — 0010, w — 0011, r — 0100, d — 0101, ! — 0110, o — 0111, l — 1
Я не очень понимаю, насколько оправдано сокращение числа символов в кодировке, чтобы ради этого усложнять реализацию. 
Поэтому ниже будет два способа. Первый — согласно пояснению, второй — согласно методу, показанному на вебинаре."""
# Способ первый
sentence = 'Hello world!'
letters = sorted(Counter(sentence).items(), key=lambda item: item[1])
tree = [letters[i][0] for i in range(len(letters))]

while len(tree) > 1:
    b = []
    for i in range(1, len(tree), 2):
        merge = (tree[i - 1]), (tree[i])
        b.append(list(merge))
    if len(tree) % 2 == 1:
        b.append(tree[-1])
    tree = b
tree = tree[0]
codes = dict()


def code(tree_, path=''):

    if len(tree_) == 1:
        codes[tree_] = path
    else:
        code(tree_[0], path=f'{path}0')
        code(tree_[1], path=f'{path}1')


print(tree)
'''[[[['H', 'e'], [' ', 'w']], [['r', 'd'], ['!', 'o']]], 'l']'''
code(tree)
print(codes)
'''{'H': '0000', 'e': '0001', ' ': '0010', 'w': '0011', 'r': '0100', 'd': '0101', '!': '0110', 'o': '0111', 'l': '1'}'''
for i in sentence:
    print(codes[i], end=' ')
print()
'''0000 0001 1 1 0111 0010 0011 0111 0100 1 0101 0110'''


class Huffman:  # Способ второй с использованием ООП и recordClass.

    def __init__(self, string):
        self.string = string
        self.root = []
        self.symbols = dict()
        self.huffman_text = ''

    def tree(self):

        self.root.clear()

        letters_ = sorted(Counter(self.string).items(), key=lambda item: item[1])

        cell = recordclass(f'cell', 'into_cell mass')

        for i in range(len(letters_)):
            cell_ = cell(letters_[i][0], letters_[i][1])
            self.root.append(cell_)

        while len(self.root) > 1:
            first, second = self.root.pop(0), self.root.pop(0)
            new_cell = cell([first.into_cell, second.into_cell], first.mass + second.mass)
            self.root.append(new_cell)

            for i in range(len(self.root) - 1):
                if self.root[-1].mass <= self.root[i].mass:

                    self.root.insert(i, self.root.pop(-1))
                    break

        self.root = self.root[0].into_cell

        def coding(tree_, path=''):

            if len(tree_) == 1:
                self.symbols[tree_] = path
            else:
                coding(tree_[0], path=f'{path}0')
                coding(tree_[1], path=f'{path}1')

        self.symbols.clear()
        coding(self.root)

    def __str__(self):
        Huffman.tree(self)
        self.huffman_text = ''
        a = ''
        for i in self.string:
            a = f'{a}{self.symbols[i]} '
        self.huffman_text = a[:-1]
        return f'Исходный текст: {self.string}\nЗакодированный текст: {self.huffman_text}'


example = Huffman(sentence)

print(example.root, example.symbols)  # Заполнение инциилизируется либо через .tree(), либо print() → [] {}
print(example)
'''Исходный текст: Hello world!
Закодированный текст: 1110 1111 10 10 00 1100 1101 00 0110 10 0111 010'''
print(example.symbols)
'''{'o': '00', '!': '010', 'r': '0110', 'd': '0111', 'l': '10', ' ': '1100', 'w': '1101', 'H': '1110', 'e': '1111'}'''
print(example.string)
'''Hello world!'''
print(Huffman('Ехал Грека через реку. Видит Грека в реке рак. Сунул в реку руку Грека. Рак за руку Греку — цап.'))

