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

freq_dict=collections.Counter(input('Введите строку для кодирования:'))
while len(freq_dict) > 1:
    left,right = freq_dict.most_common()[:-3:-1]
    del freq_dict[left[0]]
    del freq_dict[right[0]]
    freq_dict['('+left[0]+','+right[0]+')']  = left[1] + right[1]
tree = freq_dict.most_common()[0][0]
print(f'Дерево Хаффмана в скобочной форме:{tree}')
code =''
code_tbl = {}
for i in tree:
    if i == '(':
        code += '0'
    elif i == ',':
        code = code[:len(code)-1]
        code += '1'
    elif i == ')':
        code = code[:len(code) - 1]
    else:
        code_tbl[i] = code

print(f'Таблица кодировки:{code_tbl}')
