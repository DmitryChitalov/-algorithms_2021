
class StackClass:
    def __init__(self):
        self.elems = [[]]

    def push_to(self, el):
        if len(self.elems[len(self.elems) - 1]) == 5:
            self.elems.append([el])
        else:
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        if len(self.elems[len(self.elems) - 1]) == 1:
            return self.elems.pop()
        else:
            return self.elems[len(self.elems) - 1].pop()

    def stack_size(self):
        return len(self.elems)

    def get_val_last(self):
        return self.elems[len(self.elems) - 1]

    def get_stack(self):
        return self.elems


start = StackClass()
start.push_to(1)
start.push_to(2)
start.push_to(3)
start.push_to(4)
start.push_to(5)
start.push_to(6)
print(start.stack_size())
print(start.get_stack())
start.pop_out()
print(start.get_stack())