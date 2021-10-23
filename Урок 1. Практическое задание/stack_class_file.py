class StackClass:
    def __init__(self, max):
        self.elems = [[]]
        self.max = max
    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, elem):
        if len(self.elems[len(self.elems) - 1]) < self.max:
            self.elems[len(self.elems) - 1].append(elem)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(elem)

    def pop_out(self):
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)
