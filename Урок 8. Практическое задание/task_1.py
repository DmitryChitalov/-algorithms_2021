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


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(root, codes=None, code=''):
    if codes is None:
        codes = dict()

    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')

    return codes


def get_tree(string):
    string_count = Counter(string)  # считаем частоты символов

    # если строка была пуста или состояла из одного и того же символа,
    # формируем узел дерева, который будет являться и его корнем
    if len(string_count) <= 1:
        node = Node(None)

        # если строка состояла из одного и того же символа, то добавляем его
        # в левое поддерево, для формирования ддп в правое поддерево добавляем пустой узел
        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)

        # переопределяем массив частот символов, формируем его лишь из построенного дерева
        string_count = {node: 1}

    # если в строке изначально было > 1 одинакового символа, либо массив частот состоит более чем из
    # двух символов и/или деревьев с пустым корнем
    while len(string_count) != 1:
        # формируем узел дерева и выбираем 2 наиболее редких элемента массива частот
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]

        # если выбранные элементы - символы, то добавляем их в качестве узлов дерева,
        # иначе выбранный элемент уже сам является деревом с пустым корнем =>
        # добавляем его в соответствующее поддерево
        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])
        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])
        else:
            node.right = spam[1][0]

        # из массива частот удаляем выбранные элементы и добавляем в него новый - сформированное
        # дерево с пустым узлом и частотой, равной сумме частот выбранных элементов
        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]

    # в результате массив частот состоит лишь из дерева с пустым корнем, возвращаем ссылку на него
    # в словаре string_count в данный момент ссылка является ключом словаря, а итоговая суммарная частота - значением
    return [key for key in string_count][0]


def coding(string, codes):
    res = ''

    for symbol in string:
        res += codes[symbol]

    return res


def decoding(string, codes):
    res = ''
    i = 0

    while i < len(string):

        for code in codes:

            if string[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])

    return res


my_string = 'beep boop beer!'
tree = get_tree(my_string)

codes = get_code(tree)
print(f'Шифр: {codes}')

coding_str = coding(my_string, codes)
print('Сжатая строка: ', coding_str)

decoding_str = decoding(coding_str, codes)
print('Исходная строка: ', decoding_str)

if my_string == decoding_str:
    print('Успешно!')
else:
    print('Ошибка!')
