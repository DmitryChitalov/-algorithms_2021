"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

******************************************************************************

Реализация через ООП на основе материала урока. (через Counter, deque)

Создан класс "Node" для создания узлов дерева,
содержащий информацию о правом и левом потомке

Создан класс "HaffmanCode" для кодирования строки:
- не хранит изначальную строку, сразу создавая словарь с
кодами и закодированную строку
- работает для строк из одного символа и вызывает ошибку при
попытке создать код из пустой строки
- методы класса реализованы как защищённые для ограничения доступа
- получить закодированную строку можно через свойство get_code_string
- получить изначальную строку можно через свойство encode
"""
from collections import Counter, deque


class Node:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


class HaffmanCode:

    def __init__(self, string):
        if not string:
            raise ValueError('невозможно создать код из пустой строки')
        self.__encode_dict = {}
        self.__create_code(self.__create_tree(string))
        self.__code_string = self.__create_code_string(string)

    def __create_code_string(self, string):
        return ' '.join(self.__encode_dict[ch] for ch in string)

    # создаём дерево для дальнейшей обработки
    def __create_tree(self, string):
        code_deque = deque(Counter(string).most_common())
        code_deque.reverse()

        # если элемент единственный, возвращаем дерево с 1 левым потомком
        if len(code_deque) == 1:
            return Node(code_deque[0][0])

        while len(code_deque) > 1:
            # считаем вес и создаём узел дерева
            weight = code_deque[0][1] + code_deque[1][1]
            node = Node(code_deque.popleft()[0], code_deque.popleft()[0])

            i = 0
            while i < len(code_deque):
                # если находим элемент с весом больше получившегося
                # вставляем до него
                if code_deque[i][1] >= weight:
                    code_deque.insert(i, (node, weight))
                    break
                i += 1
            else:
                # иначе добавляем в конец
                code_deque.append((node, weight))

        # возвращаем получившееся дерево
        return code_deque[0][0]

    # заполняем словарь символами и их кодами
    def __create_code(self, node, code=''):
        if isinstance(node, str):
            self.__encode_dict[node] = code
        else:
            self.__create_code(node.left, f'{code}0')
            # проверка на случай строки из 1 элемента
            try:
                self.__create_code(node.right, f'{code}1')
            except AttributeError:
                pass

    @property
    def get_code_string(self):
        return self.__code_string

    @property
    def encode(self):
        codes = self.__code_string.split()
        encode = []
        for code in codes:
            for ch, el in self.__encode_dict.items():
                if code == el:
                    encode.append(ch)
        return ''.join(encode)


if __name__ == '__main__':

    tree = HaffmanCode('beep boop beer!')
    print(tree.get_code_string)
    print(tree.encode)

    t1 = HaffmanCode('bbbbbb')
    print(t1.get_code_string)
    print(t1.encode)
