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

class HFNode:
    '''
    Узел в дереве алгоритма Хаффмана
    '''
    def __init__(self,value,weight):
        self.value = value # значение - символ
        self.weight = weight # вес - суммарный счетчик
        self.parent = None # родительский узел
        self.childs = None # дочерние узлы
        self.code = list() # кодирование символа      
        self.title = f"{self.value}:{self.weight}" # для отладки

    def __add__(self,node):
        parent_node = HFNode(f"p.0:{self.value};1:{node.value}", self.weight+node.weight) #создать родительский узел для слагаемых узлов    
        parent_node.childs = {0:self,1:node} # установить дочерние узлы для родителя      
        self.parent = parent_node # устанавливает значение родителя
        node.parent = parent_node # устанавливает значение родителя
        self.code.append(0)
        node.code.append(1)
        return parent_node
    def __str__(self):
        return self.title
        
    def __repr__(self):
        return self.__str__()

class HFTree:
    '''
    Класс Дерево алгоритма Хаффмана
    '''
    def __init__(self,inp_str=""):
        self.input_str = inp_str # входящая строка
        self.count_tbl = dict() # таблица символ : частотность
        self.code_tbl = dict() # таблица символ : код
        self.leaf = list() # список узлов - листьев 
        self.root = None # корень дерева

    def _sub_tree(self,deq):
        '''
        рекурсивное создание дерева из узлов
        '''
        node = deq.popleft() + deq.popleft()
        if len(deq) == 0:
            deq.append(node)
            return deq[0] 
        if len(deq) >= 1 and node.weight > deq[len(deq)-1].weight:
            deq.append(node)            
        else:
            for i,_ in enumerate(deq):
                if node.weight <= deq[i].weight:
                    deq.insert(i,node)
                    break
        return self._sub_tree(deq)
            
    def str_to_hfm(self):
        '''
        создание табицы символ:частотность
        формирование дерева
        кодирование символов
        '''
        dct = dict(Counter(self.input_str))
        tmp_tupl= sorted(dct.items(), key=lambda item: item[1])
        self.count_tbl = {k: v for k, v in tmp_tupl}
        deq = deque([HFNode(k,v)for k,v in self.count_tbl.items()])
        self.leaf = list(deq)
        self.root = self._sub_tree(deq)
        self.get_code()
        for n in hft.leaf:
            n.code.reverse()
            self.code_tbl[n.value] = ''.join(str(i) for i in n.code)

    def _find_code(self,node,node_parent):
        '''
        рекурсивно формирует код для символов строки
        '''
        if node_parent:
            if len(node_parent.code):
                node.code.append(node_parent.code[0])
            return self._find_code(node,node_parent.parent)
        else:
            return 0
    
    def get_code(self):
        for n in hft.leaf:
            self._find_code(n,n.parent)

    def coding_str(self):
        '''
        кодирует строку
        '''
        coded = list()
        for i,ch in enumerate(self.input_str):
            if ch in self.code_tbl.keys():
                coded.append(self.code_tbl[ch])
        return " ".join(str(i) for i in coded)
    
    def str_decoder(self,code_str):
        '''
        декодирует строку
        '''
        decod=list()
        lst = code_str.split(' ')
        for i in lst:
            for k,v in self.code_tbl.items():
                if i == v:
                    decod.append(k)

        return "".join(str(i) for i in decod)


#---------------------------------------------------------------------------------
test_str1 = "beep boop beer!"
test_str = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
              sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
              Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
              nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
              reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
              Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
              deserunt mollit anim id est laborum.'''
hft = HFTree(test_str)
hft.str_to_hfm()
print("test_str:\n\t ",test_str)
print(f"count table:\n\t{hft.count_tbl}\n")
print(f"symbol_code:\n\t{hft.code_tbl}\n")

coded = hft.coding_str()
print(f"coding_str:\n\t{coded}\n")

print(f"decoder:\n\t{hft.str_decoder(coded)}")

'''
test_str:
          beep boop beer!
count table:
count table:
        {'r': 1, '!': 1, 'p': 2, ' ': 2, 'o': 2, 'b': 3, 'e': 4}

symbol_code:
        {'r': '1000', '!': '1001', 'p': '101', ' ': '010', 'o': '011', 'b': '00', 'e': '11'}

coding_str:
        00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001

decoder:
        beep boop beer!

#------------------------------------------------------------------------------------------------------
test_str:
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
              sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
              Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
              nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
              reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
              Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
              deserunt mollit anim id est laborum.

count table:
        {'L': 1, 'U': 1, 'D': 1, 'h': 1, 'E': 1, 'g': 3, 'b': 3, 'v': 3, 'x': 3,
 'f': 3, ',': 4, '.': 4, 'q': 5, '\n': 6, 'p': 11, 'c': 16, 'm': 17, 's': 18, 'd
': 18, 'l': 21, 'r': 22, 'n': 24, 'u': 28, 'o': 29, 'a': 29, 't': 32, 'e': 37, '
i': 42, ' ': 151}

symbol_code:
        {'L': '001011100', 'U': '001011101', 'D': '0010111110', 'h': '0010111111
', 'E': '001011110', 'g': '0010000', 'b': '0010001', 'v': '11111010', 'x': '1111
1011', 'f': '0010100', ',': '0010101', '.': '0010110', 'q': '1111100', '\n': '00
1001', 'p': '111111', 'c': '01110', 'm': '01111', 's': '11000', 'd': '11001', 'l
': '11110', 'r': '0000', 'n': '0001', 'u': '0011', 'o': '0100', 'a': '0101', 't'
: '0110', 'e': '1101', 'i': '1110', ' ': '10'}

coding_str:
        001011100 0100 0000 1101 01111 10 1110 111111 11000 0011 01111 10 11001 
0100 11110 0100 0000 10 11000 1110 0110 10 0101 01111 1101 0110 0010101 10 01110
 0100 0001 11000 1101 01110 0110 1101 0110 0011 0000 10 0101 11001 1110 111111 1
110 11000 01110 1110 0001 0010000 10 1101 11110 1110 0110 0010101 10 001001 10 1
0 10 10 10 10 10 10 10 10 10 10 10 10 11000 1101 11001 10 11001 0100 10 1101 111
0 0011 11000 01111 0100 11001 10 0110 1101 01111 111111 0100 0000 10 1110 0001 0
1110 1110 11001 1110 11001 0011 0001 0110 10 0011 0110 10 11110 0101 0010001 010
0 0000 1101 10 1101 0110 10 11001 0100 11110 0100 0000 1101 10 01111 0101 001000
0 0001 0101 10 0101 11110 1110 1111100 0011 0101 0010110 10 001001 10 10 10 10 1
0 10 10 10 10 10 10 10 10 10 001011101 0110 10 1101 0001 1110 01111 10 0101 1100
1 10 01111 1110 0001 1110 01111 10 11111010 1101 0001 1110 0101 01111 0010101 10
 1111100 0011 1110 11000 10 0001 0100 11000 0110 0000 0011 11001 10 1101 1111101
1 1101 0000 01110 1110 0110 0101 0110 1110 0100 0001 10 0011 11110 11110 0101 01
111 01110 0100 10 11110 0101 0010001 0100 0000 1110 11000 10 001001 10 10 10 10 
10 10 10 10 10 10 10 10 10 10 0001 1110 11000 1110 10 0011 0110 10 0101 11110 11
10 1111100 0011 1110 111111 10 1101 11111011 10 1101 0101 10 01110 0100 01111 01
111 0100 11001 0100 10 01110 0100 0001 11000 1101 1111100 0011 0101 0110 0010110
 10 0010111110 0011 1110 11000 10 0101 0011 0110 1101 10 1110 0000 0011 0000 110
1 10 11001 0100 11110 0100 0000 10 1110 0001 10 001001 10 10 10 10 10 10 10 10 1
0 10 10 10 10 10 0000 1101 111111 0000 1101 0010111111 1101 0001 11001 1101 0000
 1110 0110 10 1110 0001 10 11111010 0100 11110 0011 111111 0110 0101 0110 1101 1
0 11111010 1101 11110 1110 0110 10 1101 11000 11000 1101 10 01110 1110 11110 111
10 0011 01111 10 11001 0100 11110 0100 0000 1101 10 1101 0011 10 0010100 0011 00
10000 1110 0101 0110 10 0001 0011 11110 11110 0101 10 111111 0101 0000 1110 0101
 0110 0011 0000 0010110 001001 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0010111
10 11111011 01110 1101 111111 0110 1101 0011 0000 10 11000 1110 0001 0110 10 010
0 01110 01110 0101 1101 01110 0101 0110 10 01110 0011 111111 1110 11001 0101 011
0 0101 0110 10 0001 0100 0001 10 111111 0000 0100 1110 11001 1101 0001 0110 0010
101 10 11000 0011 0001 0110 10 1110 0001 10 01110 0011 11110 111111 0101 10 1111
100 0011 1110 10 0100 0010100 0010100 1110 01110 1110 0101 10 001001 10 10 10 10
 10 10 10 10 10 10 10 10 10 10 11001 1101 11000 1101 0000 0011 0001 0110 10 0111
1 0100 11110 11110 1110 0110 10 0101 0001 1110 01111 10 1110 11001 10 1101 11000
 0110 10 11110 0101 0010001 0100 0000 0011 01111 0010110

decoder:
        Lorem ipsum dolor sit amet, consectetur adipiscing elit,
 0110 10 1110 0001 10 01110 0011 11110 111111 0101 10 1111100 0011 1110 10 0100 0010100 0010100 1110 01110 1110 0101 10 001001 10 10 10 10 10 10 10 10 10 10 10 10 10 10 11001 1101 11000 1101 0000 0011 0001 0110 10 01111 0100 11110 11110 1110 0110 10 0101 0001 1110 01111 10 1110 11001 10 1101 11000 0110 10 11110 0101 0010001 0100 0000 0011 01111 0010110

decoder:
        Lorem ipsum dolor sit amet, consectetur adipiscing elit,
              sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
              Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
              nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
              reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
              Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
              deserunt mollit anim id est laborum.
'''
 