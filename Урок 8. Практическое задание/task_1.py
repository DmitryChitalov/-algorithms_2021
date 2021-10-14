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

code_table = {}

class HaffCode:
    def __init__(self, some_str):
        self.some_str = some_str
        # tree дерево полученное из метода haff_tree
        self.tree = self.haff_tree()
        # code - таблица кодировок полученная из метода haff_code
        self.code = self.haff_code(self.tree)

    # метод получения дерева
    def haff_tree(self):
        # получаем словарь count с количеством элементов
        count = Counter(self.some_str)
        # сортируем элементы по возрастанию(по частоточности)
        sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
        if len(sorted_elements) != 1:       # проверяем можно ли разбить на 2 ветки
            while len(sorted_elements) > 1:
                # weight - стоимость(вес) двух первых(слева) элементов
                weight = sorted_elements[0][1] + sorted_elements[1][1]
                # comb объединяет два элемента одного веса,
                # но распределяет по разным веткам 0 и 1
                comb = {0: sorted_elements.popleft()[0],
                        1: sorted_elements.popleft()[0]}
                # объединяем элементы
                for i, _count in enumerate(sorted_elements):
                    if weight > _count[1]:
                        continue
                # вставляем объединенные элементы в дек
                    else:
                        sorted_elements.insert(i, (comb, weight))
                        break
                else:
                    # вставляем мини-дерево в словарь
                    sorted_elements.append((comb, weight))
        else:   # если элемент нельзя распределить, то отправляем его в левую ветку 0
            weight = sorted_elements[0][1]
            comb = {0: sorted_elements.popleft()[0], 1: None}
            sorted_elements.append((comb, weight))
        # в итоге мы получаем дерево (словари словарей)
        return sorted_elements[0][0]

    def haff_code(self, tree, path=''):
        # останавливаем рекурсию, если дошли до последнего элемента(не словаря)
        if not isinstance(tree, dict):
            code_table[tree] = path
        else:
            # через рекурсию доходим до последнего элемента дерева
            self.haff_code(tree[0], path=f'{path}0')
            self.haff_code(tree[1], path=f'{path}1')
        # получаем таблицу кодировок(словарь, в котором ключи - элементы, значения - кодировки)
        return code_table

    def str_code(self, code_str=''):
        for i in self.some_str:
            # преобразовываем строку в кодировку
            code_str += f'{self.code[i]} '
        return code_str

class HaffUncode(HaffCode):
    def __init__(self, code):
        super().__init__(code)

    def uncode_str(code_string):
        uncode = {}
        uncode_str = ''

        for key, value in hc.code.items():
            uncode[value] = key

        for i in code_string.split():
            uncode_str += uncode[i]
        return uncode_str


hc = HaffCode("beep boop beer!")
print(hc.haff_tree())   # дерево
print(hc.code)          # таблица кодировок
print(hc.str_code())    # сама кодировка

hu = HaffUncode
print(hu.uncode_str('00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001'))

"""
Разобрал пример с урока с комментариями для себя
Реализацию понял
Реализовал раскодировку через наследование классов
"""