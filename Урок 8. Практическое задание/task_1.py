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

line = input('Введите строку для кодирования по Хаффману: ')
while not len(line):
    line = input('Пустая строка в кодировании не нуждается. Введите строку: ')

print('Исходная строка:', line)

freq = deque(Counter(line).most_common()[::-1])
print('Упорядоченные частоты символов:', *freq)


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


while len(freq) > 1:
    c1 = freq.popleft()
    c2 = freq.popleft()
    little_tree = Node(c1[0], c2[0]), c1[1] + c2[1]
    for i in range(len(freq)):
        if freq[i][1] >= little_tree[1]:
            freq.insert(i, little_tree)
            break
    else:
        freq.append(little_tree)


def h_tree(node, ans=''):
    if type(node) is str:
        return {node: ans} if ans else 0
    l = node.left
    r = node.right

    res = {}

    res.update(h_tree(l, ans + '0'))
    res.update(h_tree(r, ans + '1'))

    return res


coding_table = h_tree(freq[0][0]) if type(freq[0][0]) is Node else {freq[0][0]: '0'}

print('Таблица кодирования:')
for i, j in coding_table.items():
    print(f'{i} - {j}')
res = ''

for i in line:
    res += coding_table[i]

print('Закодированная строка:', res)

words = ''

while len(res) > 0:
    for i, j in coding_table.items():
        if j == res[:len(j)]:
            words += i
            res = res[len(j):]
print('Раскодированная строка:', words)

'''
Как-то так)
Вроде все работает. На пустых строках и строках из 1 элемента - проверено.
РАскодирование тоже работает.
'''
