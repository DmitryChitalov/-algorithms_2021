class PlateStack:
    def __init__(self, max_level):
        self.elems = []
        self.max_level = max_level

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems) < self.max_level:
            self.elems.append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        elem_sum = 0
        for stack in self.elems:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        return len(self.elems)


if __name__ == '__main__':
    plates = PlateStack(3)
    plates.push_in('Plate_1')
    plates.push_in('Plate_2')
    plates.push_in('Plate_3')
    plates.push_in('Plate_4')
    plates.push_in('Plate_5')
    print(plates.get_val())
    print(plates.pop_out())
    print(plates.is_empty())
    print(plates.stack_count())
