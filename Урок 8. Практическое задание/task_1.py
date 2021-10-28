from collections import Counter, deque, OrderedDict


class HaffmanTree:
    __slots__ = ('result', 'counter_string', 'list_deque', 'code')
    def __init__(self, s):
        self.result = {}
        self.counter_string = Counter(s)
        self.list_deque = deque(sorted(self.counter_string.items(), key=lambda val: val[1]))
        self.code = ''

    def binary_tree(self):
        if len(self.list_deque) != 1:
            while len(self.list_deque) > 1:
                weight = self.list_deque[0][1] + self.list_deque[1][1]
                trans_dict = {0: self.list_deque.popleft()[0],
                              1: self.list_deque.popleft()[0]}
                for i, value in enumerate(self.list_deque):
                    if weight > value[1]:
                        continue
                    else:
                        self.list_deque.insert(i, (trans_dict, weight))
                        break
                else:
                    self.list_deque.append((trans_dict, weight))
        else:
            trans_dict = {0: self.list_deque[0][0]}
            return trans_dict
        return self.list_deque[0][0]

    def haffman_result(self, tree, path=""):
        if not isinstance(tree, dict):
            self.result[tree] = path
        else:
            self.haffman_result(tree[0], '%s0' % (path))
            self.haffman_result(tree[1], '%s1' % (path))

    def table_code(self):
        for i in self.result.items():
            self.code += f'{i[1]} '
        print(self.code)


s = "beep boop beer!"
start = HaffmanTree(s)
tree = start.binary_tree()
# print(start)
start.haffman_result(tree)
# print(start.res_code)
# print(list(start.table_code()))
start.table_code()
# for value in start.table_code():
#     print(*value)
