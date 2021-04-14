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

code_table = dict()

sentence = 'beep boop beer!'
#sentence = 'I love lasagna'
incidence = Counter(sentence)
incidence_sort = deque(sorted(incidence.items(), key=lambda i: i[1]))

# Пока по шагам
# Возьмём первые 2 элемента и суммируем их значение
summa = incidence_sort[0][1] + incidence_sort[1][1]
print(incidence_sort[0][1], incidence_sort[1][1], summa)
# и удалим их из массива
sub_tree = {0: incidence_sort.popleft()[0], 1: incidence_sort.popleft()[0]}
print('sub_tree', sub_tree)

print(incidence_sort)
if(summa > incidence_sort[1]):
    print('нужно поставить правее') # ???? 

# print(incidence_sort[0].values(), incidence_sort[1])
# Не смог(())
