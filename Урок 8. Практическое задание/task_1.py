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


class Haffman:

    def __init__(self, *args):
        self.code_table = dict()
        self.decode_table = dict()
        self.encoded_string = ''
        self.my_str = ''
        try:
            if len(args) < 2:
                self.my_str = args[0]
            else:
                self.code_table = args[0]
                for key, val in self.code_table.items():
                    self.decode_table[val] = key
                self.encoded_string = args[1].split()
        except Exception:
            print('Исходные данные введены с ошибкой.')

    def make_tree(self):
        freq_of_char = Counter(self.my_str)
        sorted_elements = deque(sorted(freq_of_char.items(), key=lambda item: item[1]))
        if len(sorted_elements) != 1:
            # Цикл для построения дерева
            while len(sorted_elements) > 1:
                weight = sorted_elements[0][1] + sorted_elements[1][1]
                comb = {0: sorted_elements.popleft()[0],
                        1: sorted_elements.popleft()[0]}
                # Ищем место для ставки объединенного элемента
                for i, _count in enumerate(sorted_elements):
                    if weight > _count[1]:
                        continue
                    else:
                        sorted_elements.insert(i, (comb, weight))
                        break
                else:
                    sorted_elements.append((comb, weight))
        else:
            # приравниваемыем значение 0 к одному повторяющемуся символу
            weight = sorted_elements[0][1]
            comb = {0: sorted_elements.popleft()[0], 1: None}
            sorted_elements.append((comb, weight))

        return sorted_elements[0][0]

    def haffman_code(self, tree, path=''):
        # Если элемент не словарь, значит мы достигли самого символа
        # и заносим его, а так же его код в словарь (кодовую таблицу).
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        # Если элемент словарь, рекурсивно спускаемся вниз
        # по первому и второму значению (левая и правая ветви).
        else:
            self.haffman_code(tree[0], path=f'{path}0')
            self.haffman_code(tree[1], path=f'{path}1')

    def table_code(self):
        self.code_table.clear()
        self.haffman_code(self.make_tree())
        return self.code_table

    def str_encode(self):
        if len(self.code_table) == 0:  # если таблица кодировки не была создана, то создадим
            self.table_code()
        return ' '.join([(lambda x: self.code_table.get(x))(i) for i in self.my_str])

    def str_decode(self):
        if len(self.decode_table) == 0:  # если таблица кодировки не была создана, то создадим
            return 'В класс не была передана таблица кодировки.'
        else:
            self.my_str = ''.join([(lambda x: self.decode_table.get(x))(i) for i in self.encoded_string])
            return self.my_str


# -- Проверка решения:

# Кодируем данные
print(f'{"-" * 20} Кодируем данные {"-" * 20}')
h = Haffman("Мой дядя самых честных правил")
print(f'Кодируемый текст: {h.my_str}')
print(f'Структура дерева: {h.make_tree()}')  # если нужно создать и посмотреть дерево
print(f'Кодировочная таблица:  {h.table_code()}')  # если нужно посмотреть полученную кодировочную таблицу
print(f'Результат кодирования: {h.str_encode()}')  # результат кодирования (можно запустить без make_tree и table_code)

print(f'\n{"-" * 20} Декодируем данные {"-" * 20}')
# Декодируем данные
# В переменную класса передадим два параметра - словарь с кодировочной таблицей, закодированный текст
table_code = {'х': '000', 'л': '0010', 'в': '00110', 'и': '00111', 'п': '01000', 'р': '01001',
              'т': '01010', 'н': '01011', ' ': '011', 'М': '10000', 'о': '10001', 'д': '1001',
              'ч': '10100', 'е': '10101', 'й': '10110', 'м': '10111', 'а': '1100', 'ы': '1101',
              'я': '1110', 'с': '1111'}
str_encode = '10000 10001 10110 011 1001 1110 1001 1110 011 1111 1100 10111 1101 000 011 10100 10101 1111 ' \
             '01010 01011 1101 000 011 01000 01001 1100 00110 00111 0010'
nh = Haffman(table_code, str_encode)
print(f'Результат декодирования: {nh.str_decode()}')
print(f'Структура дерева: {h.make_tree()}')
