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
"""
Для реализации кодировки я использовал пример из интернета, который показался мне наиболее интересным.
Этот же пример есть в примерах решения задания. Существенное изменение, которое я внес, это отделил от функции
по созданию дерева (def create_tree) инициализацию словаря с кодировкой символов в отдельную функцию (def dict_oop). 
Сделано это ради того, чтобы использовать помимо этого способа кодировки, способ, основанный на рекурсии (def recur).
"""
from collections import Counter, namedtuple
import heapq


class Parent(namedtuple('Parent', ['left', 'right'])):
    # для объекта класса Parent метод walk осматривает имеющихся левого и правого потомка, записывая свой путь
    # в переменную acc
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    # для объекта класса Leaf метод walk извлекает хранящийся в нем символ и добавляет его в словарь, в значении
    # сохраняя путь по которому он добирался до него
    def walk(self, code, acc):
        code[self.char] = acc or '0'  # '0', если строка состоит из одного символа


def create_tree(s):
    # создаем список и заполняем его объектами класса Leaf
    # частотой повторения (freq),символами (lett), а также уникальным числом len(my_heap)
    # счетчик len(my_heap) необходим, чтобы объект heapq мог в дальнейшем использовать его для сортировки элементов по
    # приоритету. Без этого уникального счетчика len(my_heap) при одиннаковых частотах возникала ошибка(в то же
    # время счетчик может быть любым уникальным числом, постепенно увеличивающимся).
    my_heap = []
    for lett, freq in Counter(s).items():
        my_heap.append((freq, len(my_heap), Leaf(lett)))
    # сортируем список с помощью heapq.heapify()
    heapq.heapify(my_heap)
    count = len(my_heap)
    # циклом while создаем полноценное дерево
    while len(my_heap) > 1:
        # берем два листа с минимальной частотой, удаляем их из my_heap
        freq1, cou_1, left = heapq.heappop(my_heap)
        freq2, cou_2, right = heapq.heappop(my_heap)
        # объединяем эти два листа в поддерево, добавляем его обратно в my_heap, меняя счетчик частоты на сумму их
        # частот; увеличиваем счетчик count
        heapq.heappush(my_heap, (freq1 + freq2, count, Parent(left, right)))
        count += 1
    return my_heap


def dict_oop(root):
    code = {}
    # запускаем метод walk, реализованный в обоих классах
    root.walk(code, '')
    # возвращаем словарь, в котором хранится кодировка символов
    return code


def recur(let, root, way=''):
    # возвращаем путь, когда добрались до нужного листа
    if isinstance(root, Leaf) and root.char == let:
        return way or '0'  # '0', если строка состоит из одного символа
    # если в данный момент находимся в родительском узле, то рекурсивно вызываем функцию для проверки
    # правого и левого потомка
    elif isinstance(root, Parent):
        return recur(let, root[0], way + '0') or recur(let, root[1], way + '1')


def main(my_str):
    # кодировка реализована двумя способами
    # функция huffman_code(my_str) с помощью массива создает бинарное дерево из объектов Parent и Leaf
    #
    my_heap = create_tree(my_str)
    print(f'Дерево: {my_heap}')
    # проверка, что объект my_heap состоит хотя бы из одного символа
    if my_heap:
        root = my_heap[0][2]
        del my_heap
        # 1 способ
        # 1 функция использует возможности ООП, с помощью созданного метода walk он инициализирует словарь и проходя
        # по дереву запоминает значение для символа в кодировке, сохраняя его в словарь
        code = dict_oop(root)
        encoded_dict = ''.join(code[letter] for letter in my_str)
        # 2 способ
        # 2 Функция использует рекурсивный обход по дереву, пока не встречает в нем необходимый символ, после этого
        # возвращает код-путь до него
        encoded_rec = ''.join(recur(i, root) for i in my_str)

        for i in sorted(code):
            print(f'{i} : {code[i]}')
        print(f'Закодировано с помощью ОПП и словаря: {encoded_dict}.')
        print(f'Закодировано  с помощью рекурсивной функциии: {encoded_rec}.')


if __name__ == "__main__":
    my_str = 'метод Хаффмана'
    main(my_str)
