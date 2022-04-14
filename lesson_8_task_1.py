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


def haffman_tree(user_str):
    # Считаем уникальные символы.
    count = Counter(user_str)
    # Сортируем по возрастанию количества повторений.
    sorted_freq = deque(sorted(count.items(), key=lambda item: item[1]))
    # Проверка, если строка состоит из одного повторяющего символа.
    if len(sorted_freq) != 1:
        # Цикл для построения дерева
        while len(sorted_freq) > 1:
            # далее цикл объединяет два крайних левых элемента
            # Вес объединенного элемента (накопленная частота)
            weight = sorted_freq[0][1] + sorted_freq[1][1]
            # Словарь из 2 крайних левых элементов, попутно вырезаем их
            # из "sorted_elements" (из очереди).
            # comb - объединенный элемент
            comb = {0: sorted_freq.popleft()[0],
                    1: sorted_freq.popleft()[0]}

            # Ищем место для ставки объединенного элемента
            for i, freq in enumerate(sorted_freq):
                if weight > freq[1]:
                    continue
                else:
                    # Вставляем объединенный элемент
                    sorted_freq.insert(i, (comb, weight))d
                    break
            else:
                # Добавляем объединенный корневой элемент после
                # завершения работы цикла

                sorted_freq.append((comb, weight))

    else:
        # приравниваемыем значение 0 к одному повторяющемуся символу
        weight = sorted_freq[0][1]
        comb = {0: sorted_freq.popleft()[0], 1: None}
        sorted_freq.append((comb, weight))
    # словарь - дерево
    return sorted_freq[0][0]


code_table = dict()


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
user_str = input('Введите строку для кодирования: ')

# функция заполняет кодовую таблицу (символ-его код)
haffman_code(haffman_tree(user_str))

# code_table - {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}

# выводим коды для каждого символа
for i in user_str:
    print(code_table[i], end=' ')
print()
