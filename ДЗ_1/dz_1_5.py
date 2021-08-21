class StackClass:
    def __init__(self):
        self.elems = []
        self.total_plate_stacks = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems) + 1 > 4:
            self.total_plate_stacks.append(self.elems)
            self.elems = []
            self.elems.append(el)
        else:
            self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def get_total_plate_stacks(self):
        return self.total_plate_stacks

    def get_plate_stack(self):
        return self.elems

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':
    stk1 = StackClass()

    # наполняем стек
    stk1.push_in(10)
    stk1.push_in('code')
    stk1.push_in(False)
    stk1.push_in(5.5)

    stk1.push_in(6)
    stk1.push_in('code5')
    stk1.push_in('kl')
    stk1.push_in(7)

    stk1.push_in(3)
    stk1.push_in(7)

    print(stk1.get_total_plate_stacks())
    print(stk1.get_plate_stack())
