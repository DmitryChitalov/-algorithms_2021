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
from collections import Counter,deque
my_str = "beep boop beer!"


def haffman(my_str):
    count = Counter(my_str)
    sorted_count = deque(sorted(Counter(my_str).items(), key=lambda item: item[1]))
    if len(sorted_count) != 1:
        while len(sorted_count) > 1:
            final_deq = {0:sorted_count[0][0],1:sorted_count[1][0]}
            weigth = sorted_count[0][1]+sorted_count[1][1]
            sorted_count.popleft()
            sorted_count.popleft()
            for i,_count in enumerate(sorted_count):
                if weigth > _count[1]:
                    continue
                else:
                    sorted_count.insert(i,(final_deq,weigth))
                    break
            else:
                sorted_count.append((final_deq, weigth))
        else:
            weigth = sorted_count[0][1]
            final_deq = {0:sorted_count.popleft()[0],1:None}
            sorted_count.append((final_deq,weigth))
    return sorted_count[0][0]

def haffman_code(tree, path=''):
    if not isinstance(tree,dict):
        table[tree] = path
    else:
        haffman_code(tree[0],path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')

table = dict()
haffman_code(haffman(my_str))
print(haffman(my_str))
for i in my_str:
    print(table[i],end = ' ')
print()


"""
Свою реализацию придумать не смог. Тема действительно идет тяжело и пытался разобраться в предложенном на вебинаре
варианте.

С формированием deque разобрался. Отметил для себя три вещи:
1) оказывается for и while могут быть c else
2) интересный способ определения, куда в deque вставлять объединенные элементы (раскладка deque через enumerate и 
сравнение "веса" со вторым элементом в tuple)
3) как-то раньше не сталкивался с тем, что for можно не проходить целиком и выходить из него по нахождению элемента,
отвечающего нужному условию, через continue и break

А вот получение закодированной строки как-то совсем не очевидно и непонятно.
"""