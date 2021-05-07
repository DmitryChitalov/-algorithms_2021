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
import collections


class Node:
    """Класс 'Узел' для построения бинарного дерева Хаффмана"""

    def __init__(self, frequency=None, letter=None):
        self.frequency = frequency  # частота символа в тексте
        self.letter = letter  # символ
        self.left = None
        self.right = None

    def add_left(self, new_node):
        """Добавление левого ребенка"""
        self.left = new_node

    def add_right(self, new_node):
        """Добавление правого ребенка"""
        self.right = new_node

    def is_leaf(self):
        """Проверка, является ли узел листом, т.е. не имеет потомков """
        return (not self.right) & (not self.left)


def build_nodes_deque(str_):
    """Функция строит сортированную деку из строки,
    элементами которой являются объекты класса Node.
    Сортриовка по возрастанию частоты вхождения симовла в строку"""
    freq_table = collections.Counter(str_)
    return collections.deque(
        sorted([Node(frequency=elem[1], letter=elem[0])
                for elem in freq_table.items()], key=lambda item: item.frequency))


def build_haffman_tree(deque_):
    """Функция строит дерево Хаффмана, из входящей деки.
    возвращает дерево Хафмана
    """
    if len(deque_) != 1:
        while len(deque_) > 1:
            new_node = Node()
            elem = deque_.popleft()
            new_node.add_left(elem)
            elem = deque_.popleft()
            new_node.add_right(elem)
            new_node.frequency = new_node.left.frequency + new_node.right.frequency
            for i in range(len(deque_)):
                if deque_[i].frequency < new_node.frequency:
                    continue
                else:
                    deque_.insert(i, new_node)
                    break
            else:
                deque_.append(new_node)

    return deque_[0]


code = dict()  # Словарь в который будем складывать таблицу кодирования символов


def build_haffman_code(haffman_tree, letter_code=''):
    """заполняем словарь кодирования. Он будет иметь вид:
    {'cимвол' : код символа, ...}
    Рекурсивно обходим дерево, елси идем по левой ветви, добавляем к коду "0",
    иначе - "1"
    """
    if haffman_tree.is_leaf():
        code.update({haffman_tree.letter: letter_code})  # Если дошли до листа, добавляем элемент в словарь
    else:
        # Рекурсивные вызовы:
        build_haffman_code(haffman_tree.left, letter_code=letter_code + '0')
        build_haffman_code(haffman_tree.right, letter_code=letter_code + '1')
    return code


s = "beep boop beer!"

print(f"Кодируем текст: '{s}'")
print("Частота символов в тексе: ")
print(*[(elem.frequency, elem.letter) for elem in build_nodes_deque(s)])
haffman_tree = build_haffman_tree(build_nodes_deque(s))
haffman_code = build_haffman_code(haffman_tree)
print("Таблица кодирования: ")
print(haffman_code)
print("Закодированная строка: ")
for i in s:
    print(haffman_code[i], end=' ')
