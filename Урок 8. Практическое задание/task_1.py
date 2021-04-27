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

from collections import deque
from collections import Counter


class Haffman():
    def __init__(self, s):
        self.s = s
        self.check_s = ''
        self.codes = dict()
        self.codestring = ''
        self.deq = deque()

    # Построение дерева Хаффмана. Cоздаем дерево на основании частотного анализа элементов
    def create_tree(self, s):
        # строим словарь с частотами символов в строке
        freq = Counter(s)
        # строим отсортированный по частоте дек (список кортежей)
        self.deq = deque(sorted(freq.items(), key=lambda item: item[1]))
        print(f'Отсортированный по частоте дек: {self.deq}')
        # бежим по деку и перетаскиваем элементы согласно их сумме частот
        length_dec = len(self.deq)
        if length_dec == 0:  # входная строка пустая
            self.deq = {}
        elif length_dec == 1:  # входная строка - единственный символ
            weight = self.deq[0][1]
            new_node = {0: self.deq.popleft()[0], 1: None}  # кодируем нулем
            self.deq.append((new_node, weight))
        else:
            while len(self.deq) > 1:
                weight = self.deq[0][1] + self.deq[1][1]  # Сумма частот двух соседних элементов
                # строим новый комбинированный элемент из двух соседних элементов. Для левой ссылки присваиваем вес 0, для правой - 1
                new_node = {0: self.deq.popleft()[0], 1: self.deq.popleft()[0]}

                # ишем место куда переместить новый комбинированный элемент
                for i, node in enumerate(self.deq):
                    if weight > node[1]:
                        continue
                    else:
                        self.deq.insert(i, (new_node, weight))  # добавляем перед элементом с большей частотой
                        break
                else:
                    self.deq.append((new_node, weight))  # добавляем в конец

    #  Возвращаем словарь кодов символов
    def encode(self, tree, path=''):
        if not isinstance(tree, dict):
            self.codes[tree] = path
        else:
            self.encode(tree[0], path=f'{path}0')
            self.encode(tree[1], path=f'{path}1')

    #  Декодируем кодовую строку
    def decode(self):
        l = []
        temp = ''
        for i in self.codestring.replace(' ', ''):
            #  print('i', i)
            temp = temp + i
            # Проверяем наличие кода в нашей таблие
            for j in self.codes:
                #  print('j=', j)
                if self.codes.get(j) == temp:
                    l.append(j)
                    temp = ''
                    break
        return "".join(l)

    def __str__(self):
        return f'Итоговое дерево:{self.deq}\n' \
               f'Таблица кодировок символов: {self.codes}\n' \
               f'Закодированная строка: {self.codestring}\n' \
               f'Декодируем обратно: {self.check_s}'

    def run(self):
        # создаем дерево на основании частотного анализа элементов
        self.create_tree(self.s)
        # кодируем
        if self.deq != dict():
            self.encode(self.deq[0][0])
        # форируем кодовую последовательность
        self.codestring = "".join(self.codes[i] for i in self.s)
        # Декодируем обратно
        self.check_s = self.decode()


s = input('Введите строку, котрую Вы хотите закодировать: ')
h = Haffman(s)
h.run()
print(h)
