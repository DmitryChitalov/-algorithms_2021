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
#описание в конце
from collections import Counter, deque

class BinaryTree:
    def __init__(self, root_weight, root_symbol=None):
        # self.root = root_obj root_obj=None,
        self.weight = root_weight
        self.root_symbol = root_symbol
        self.left_child = None
        self.right_child = None

    def insert_left(self, left_child):
        if self.left_child == None:
            self.left_child = BinaryTree(left_child)
        else:
            tree_obj = BinaryTree(left_child)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    def insert_right(self, right_child):
        if self.right_child == None:
             self.right_child = BinaryTree(right_child)
        else:
            tree_obj = BinaryTree(right_child)
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.root = obj

    def get_weight_val(self):
        return self.weight

    def get_symbol(self):
        return self.root_symbol

class HuffmanCode:

    def __init__(self, user_string):
        self.user_string = user_string
        self.code_table = dict()
        self.huffman_code(self.get_tree())

    def get_counter_symbol(self):
        symbol_freq = []
        for i, j in Counter(self.user_string).items():
            symbol_freq.append(BinaryTree(root_weight=j, root_symbol=i))
        return symbol_freq

    def sort_counter_value(self):
        return deque(sorted(self.get_counter_symbol(),
                            key=lambda element: element.weight))

    def get_tree(self):
        sort_bin_tree_collection = self.sort_counter_value().copy()
        if len(sort_bin_tree_collection) != 1:
            while len(sort_bin_tree_collection) > 1:
                new_elem = BinaryTree(root_weight=sort_bin_tree_collection[0].get_weight_val() + sort_bin_tree_collection[1].get_weight_val())
                new_elem.left_child = sort_bin_tree_collection.popleft()
                new_elem.right_child = sort_bin_tree_collection.popleft()
                for i, _count in enumerate(sort_bin_tree_collection):
                    if new_elem.weight > _count.weight:
                        continue
                    else:
                        sort_bin_tree_collection.insert(i, new_elem)
                        break
                else:
                    sort_bin_tree_collection.append(new_elem)
        return sort_bin_tree_collection[0]

    def huffman_code(self, tree, path=''):
        if tree.root_symbol:
            if path == '':
                self.code_table[tree.get_symbol()] = 0
            else:
                self.code_table[tree.get_symbol()] = path
        else:
            if tree.get_right_child():
                self.huffman_code(tree.get_left_child(), path=f'{path}0')
            if tree.get_left_child():
                self.huffman_code(tree.get_right_child(), path=f'{path}1')
        return self.code_table

    def get_string_code(self):
        res = ''
        for symbol in self.user_string:
            res += self.code_table[f'{symbol}']
        return res

    def decoding(self, code_string):
        res = ''
        i = 0
        codes_dict = self.code_table
        while i < len(code_string):
            for code in codes_dict:
                if code_string[i:].find(codes_dict[code]) == 0:
                    res += code
                    i += len(codes_dict[code])
        return res


if __name__ == '__main__':
    string = input("Введите строку: ")
    a_1 = HuffmanCode(string)
    print(f"Исходная строка:\n'{string}'")

    print(f"Таблица c кодами:\n{a_1.code_table}")

    code_str = a_1.get_string_code()
    print(f"Строка кода после кодирования:\n{code_str}")
    print(f"Декодированная строка:\n'{a_1.decoding(code_str)}'")

'''
За основу алгоритма был взят пример реализации алгоритма Хафмана из task_1.7 и вместо двоичного дерева на основе словаря
было использованно несколько измененное двоичное дерево на основе ООП из примера разобранного на уроке, так сказать суперкомбо )))) 
Алгоритм был переработан исходя из особеностей нового двоичного дерева. Алгоритм получлися менее понятным, хоть и рабочим.
'''