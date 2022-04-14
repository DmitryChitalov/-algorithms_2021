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

# Вариант 1 (с доработкой)

from collections import Counter, deque


def haffman_tree(s):
    # Считаем уникальные символы.
    # Counter({'e': 4, 'b': 3, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1})
    count = Counter(s)
    # Сортируем по возрастанию количества повторений.
    # deque([('r', 1), ('!', 1), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
    # deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
    sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
    # Проверка, если строка состоит из одного повторяющего символа.
    if len(sorted_elements) != 1:
        # Цикл для построения дерева
        while len(sorted_elements) > 1:
            # далее цикл объединяет два крайних левых элемента
            # Вес объединенного элемента (накопленная частота)
            # веса - 2, 4, 4, 7, 8, 15
            weight = sorted_elements[0][1] + sorted_elements[1][1]
            # Словарь из 2 крайних левых элементов, попутно вырезаем их
            # из "sorted_elements" (из очереди).
            # comb - объединенный элемент
            '''
            {0: 'r', 1: '!'}
            {0: {0: 'r', 1: '!'}, 1: 'p'}
            {0: ' ', 1: 'o'}
            {0: 'b', 1: {0: ' ', 1: 'o'}}
            {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}
            {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
            '''
            comb = {1: sorted_elements.popleft()[0],
                    0: sorted_elements.popleft()[0]}

            # Ищем место для ставки объединенного элемента
            for i, _count in enumerate(sorted_elements):
                if weight > _count[1]:
                    continue
                else:
                    # Вставляем объединенный элемент
                    # deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
                    sorted_elements.insert(i, (comb, weight))
                    break
            else:
                # Добавляем объединенный корневой элемент после
                # завершения работы цикла

                sorted_elements.append((comb, weight))
            '''
            deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
            deque([(' ', 2), ('o', 2), ('b', 3), ({0: {0: 'r', 1: '!'}, 1: 'p'}, 4), ('e', 4)])
            deque([('b', 3), ({0: ' ', 1: 'o'}, 4), ({0: {0: 'r', 1: '!'}, 1: 'p'}, 4), ('e', 4)])
            deque([({0: {0: 'r', 1: '!'}, 1: 'p'}, 4), ('e', 4), ({0: 'b', 1: {0: ' ', 1: 'o'}}, 7)])
            deque([({0: 'b', 1: {0: ' ', 1: 'o'}}, 7), ({0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}, 8)])
            deque([({0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}, 15)])
            '''
    else:
        # приравниваемыем значение 0 к одному повторяющемуся символу
        weight = sorted_elements[0][1]
        comb = {1: sorted_elements.popleft()[0], 0: None}
        sorted_elements.append((comb, weight))
    # sorted_elements - deque([({0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}, 15)])
    # {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
    # словарь - дерево
    return sorted_elements[0][0]


code_table = dict()


# tree - {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
def haffman_code(tree, path=''):
    # Если элемент не словарь, значит мы достигли самого символа
    # и заносим его, а так же его код в словарь (кодовую таблицу).
    if not isinstance(tree, dict):
        code_table[tree] = path
    # Если элемент словарь, рекурсивно спускаемся вниз
    # по первому и второму значению (левая и правая ветви).
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


# строка для кодирования
s = "moloko"

# функция заполняет кодовую таблицу (символ-его код)
# {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
haffman_code(haffman_tree(s))

# code_table - {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}

# Добавил вывод для соответствие кода для каждого символа
for ch in sorted(code_table):  # обойдем символы в словаре в алфавитном порядке с помощью функции sorted()
    print("{}: {}".format(ch, code_table[ch]))  # выведем символ и соответствующий ему код

for i in s:
    print(code_table[i], end='')
print()



# Вариант 2 с ООП

from collections import Counter


class BinaryTree:
    def __init__(self, root_obj='root', weight=0):
        # корень
        self.root = root_obj
        self.weight = weight
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def get_full_tree(self, path='', code_table={}):
        if isinstance(self.left_child, BinaryTree):
            self.left_child.get_full_tree(f'{path}0', code_table)
        else:
            code_table[self.left_child] = f'{path}0'
        if isinstance(self.right_child, BinaryTree):
            self.right_child.get_full_tree(f'{path}1', code_table)
        else:
            code_table[self.right_child] = f'{path}1'
        return code_table


def get_tree(left, right):
    tree = BinaryTree(weight=left[1]+right[1])
    tree.left_child = left[0]
    tree.right_child = right[0]
    return tree


s = input("Введите строку: ")  #"beep boop beer!"
print(f'Строка для кодирования: {s}')
count = Counter(s)
freq_list = sorted(count.items(), key=lambda x: x[1], reverse=True)
print(f'частотный словарь {freq_list}')
while len(freq_list) > 1:
    min_1 = freq_list.pop()
    min_2 = freq_list.pop()
    tree = get_tree(min_1, min_2)
    min_union = (tree, tree.weight)
    freq_list.append(min_union)
    freq_list = sorted(freq_list, key=lambda x: x[1], reverse=True)

code_table = freq_list[0][0].get_full_tree()
print(f'Таблица кодов {code_table}')
print('Шифровка: ', " ".join(list(map(lambda x: code_table[x], s))))










































# import heapq  # модуль для работы с мин. кучей из стандартной библиотеки Python
# from collections import Counter  # словарь в котором для каждого объекта поддерживается счетчик
# from collections import namedtuple
#
# # добавим классы для хранения информации о структуре дерева
# # воспользуемся функцией namedtuple из стандартной библиотеки
# class Node(namedtuple("Node", ["left", "right"])):  # класс для ветвей дерева - внутренних узлов; у них есть потомки
#     def walk(self, code, acc):
#         # чтобы обойти дерево нам нужно:
#         self.left.walk(code, acc + "0")  # пойти в левого потомка, добавив к префиксу "0"
#         self.right.walk(code, acc + "1")  # затем пойти в правого потомка, добавив к префиксу "1"
#
# class Leaf(namedtuple("Leaf", ["char"])):  # класс для листьев дерева, у него нет потомков, но есть значение символа
#     def walk(self, code, acc):
#         # потомков у листа нет, по этому для значения мы запишем построенный код для данного символа
#         code[self.char] = acc or "0"  # если строка длиной 1 то acc = "", для этого случая установим значение acc = "0"
#
# def huffman_encode(s):  # функция кодирования строки в коды Хаффмана
#     h = []  # инициализируем очередь с приоритетами
#     for ch, freq in Counter(s).items(): # постоим очередь с помощью цикла, добавив счетчик, уникальный для всех листьев
#         h.append((freq, len(h), Leaf(ch)))  # очередь будет представлена частотой символа, счетчиком и самим символом
#     heapq.heapify(h)  # построим очередь с приоритетами
#     count = len(h) # инициализируем значение счетчика длиной очереди
#     while len(h) > 1:  # пока в очереди есть хотя бы 2 элемента
#         freq1, _count1, left = heapq.heappop(h)  # вытащим элемент с минимальной частотой - левый узел
#         freq2, _count2, right = heapq.heappop(h)  # вытащим следующий элемент с минимальной частотой - правый узел
#         # поместим в очередь новый элемент, у которого частота равна суме частот вытащенных элементов
#         heapq.heappush(h, (freq1 + freq2, count, Node(left, right))) # добавим новый внутренний узел у которого
#                                                                      # потомки left и right соответственно
#         count += 1  # инкрементируем значение счетчика при добавлении нового элемента дерева
#     code = {}  # инициализируем словарь кодов символов
#     if h:  # если строка пустая, то очередь будет пустая и обходить нечего
#         [(_freq, _count, root)] = h  # в очереди 1 элемент, приоритет которого не важен, а сам элемент - корень дерева
#         root.walk(code, "")  # обойдем дерева от корня и заполним словарь для получения кодирования Хаффмана
#     return code  # возвращаем словарь символов и соответствующих им кодов
#
# def main():
#     s = input('Введите строку, которую надо закодировать: ')  # читаем строку длиной  до 10**4
#     code = huffman_encode(s)  # кодируем строку
#     encoded = "".join(code[ch] for ch in s)  # отобразим закодированную версию, отобразив каждый символ
#                                              # в соответствующий код и конкатенируем результат
#     print(f'Число символов строки: {len(code)} и длина закодированной строки: {len(encoded)}')  # выведем число символов и длину закодированной строки
#     for ch in sorted(code): # обойдем символы в словаре в алфавитном порядке с помощью функции sorted()
#         print("{}: {}".format(ch, code[ch]))  # выведем символ и соответствующий ему код
#     print(f'Закодированная строка {encoded}')  # выведем закодированную строку
#
# if __name__ == "__main__":
#     main()


# def huffman_decode(encoded, code):  # функция декодирования исходной строки по кодам Хаффмана
#     sx =[]  # инициализируем массив символов раскодированной строки
#     enc_ch = ""  # инициализируем значение закодированного символа
#     for ch in encoded:  # обойдем закодированную строку по символам
#         enc_ch += ch  # добавим текущий символ к строке закодированного символа
#         for dec_ch in code:  # постараемся найти закодированный символ в словаре кодов
#             if code.get(dec_ch) == enc_ch:  # если закодированный символ найден,
#                 sx.append(dec_ch)  # добавим значение раскодированного символа к массиву раскодированной строки
#                 enc_ch = ""  # обнулим значение закодированного символа
#                 break
#     return "".join(sx)  # вернем значение раскодированной строки


# def test(n_iter=100):  # добавим тест для проверки алгоритма
#     import random  # нам понадобится генератор случайных чисел
#     import string  # модуль для работы со строками, чтобы получить значения символов по их коду
#
#     # сгененрируем строку из ascii-символов
#     for i in range(n_iter):  # тест включает краевые случаи с пустой строкой и строкой из 1 символа
#         length = random.randint(0, 32)  # сгеренируем код символа
#         s = "".join(random.choice(string.ascii_letters) for _ in range(length)) # получим символ по коду и добавим к строке
#         code = huffman_encode(s)  # выполним кодирование строки
#         encoded = "".join(code[ch] for ch in s)  # получим закодированную строку
#         assert huffman_decode(encoded, code) == s  # раскодируем строку и сравним ее с исходной строкой