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
"""Хаффман через коллекции"""

from collections import Counter, deque
from memory_profiler import profile
from timeit import timeit
import string
import random


def id_generator(num):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(num))


def haffman_tree(s):
    # Считаем уникальные символы.
    # Counter({'e': 4, 'b': 3, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1})
    counter = Counter(s)
    # Сортируем по возрастанию количества повторений.
    # deque([('r', 1), ('!', 1), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
    # deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
    sorted_elements = deque(sorted(counter.items(), key=lambda item: item[1]))
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
            comb = {0: sorted_elements.popleft()[0],
                    1: sorted_elements.popleft()[0]}

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
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, weight))
    # sorted_elements - deque([({0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}, 15)])
    # {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
    # словарь - дерево
    return sorted_elements[0][0]


def my_haffman_tree(s):
    '''
    переделал построение дерева с дека на обычнй список, получил скорость хоже на 20 процентов,
    по памяти получилось так же на любой длине строки
    0.1048603
    0.1278903
    '''
    counter = Counter(s)
    sorted_elements = list(sorted(counter.items(), key=lambda item: item[1]))

    if len(sorted_elements) != 1:
        while len(sorted_elements) > 1:
            new_dict = dict()
            count = 0
            for i, value in enumerate(sorted_elements):
                if i > 1:
                    break
                new_dict[i] = value[0]
                count += value[1]
            item = (new_dict, count)

            sorted_elements.pop(0)
            sorted_elements.pop(0)

            for i, _count in enumerate(sorted_elements):
                if count > _count[1]:
                    continue
                else:
                    sorted_elements.insert(i, item)
                    break
            else:
                sorted_elements.append(item)
    else:
        count = sorted_elements[0][1]
        new_dict = {0: sorted_elements.pop(0)[0], 1: None}
        sorted_elements.append((new_dict, count))
    return sorted_elements[0][0]


code_table = dict()
my_code_table = dict()


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


def my_haffman_code(tree, path=''):
    # Если элемент не словарь, значит мы достигли самого символа
    # и заносим его, а так же его код в словарь (кодовую таблицу).
    if not isinstance(tree, dict):
        my_code_table[tree] = path
    # Если элемент словарь, рекурсивно спускаемся вниз
    # по первому и второму значению (левая и правая ветви).
    else:
        my_haffman_code(tree[0], path=f'{path}0')
        my_haffman_code(tree[1], path=f'{path}1')


@profile()
def memory_haffman_code():
    haffman_code(haffman_tree(s))


@profile()
def memory_my_haffman_code():
    my_haffman_code(haffman_tree(s))


# строка для кодирования
s = "beep boop beer!"
# s = id_generator(50000)

# функция заполняет кодовую таблицу (символ-его код)
# {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}

haffman_code(haffman_tree(s))
my_haffman_code(my_haffman_tree(s))

# code_table - {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}

# выводим коды для каждого символа
for i in s:
    print(code_table[i], end=' ')
print("")
for i in s:
    print(my_code_table[i], end=' ')
print()

print(timeit("haffman_code(haffman_tree(s))", globals=globals(), number=10000))
print(timeit("haffman_code(my_haffman_tree(s))", globals=globals(), number=10000))

memory_haffman_code()
memory_my_haffman_code()
