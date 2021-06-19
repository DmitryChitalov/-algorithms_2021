class StackClass:
    def __init__(self, max_size):
        self.elems = []
        self.max_size = max_size

    def is_empty(self):
        return self.elems == []

    def stack_qty(self):  # Кол-во стопок
        return len(self.elems)

    def insert(self, el):  # Внести в стопку
        self.elems[self.stack_qty() - 1].append(el)

    def stack_size(self):  # Размер последней стопки
        return len(self.elems[self.stack_qty() - 1])

    def push_in(self, el):
        if self.is_empty():  # Если пустой - создать новую стопку и внести значение
            self.elems.append([])
            self.insert(el)
        elif self.stack_size() < self.max_size:  # Стопка не переполнена - вносим значение
            self.insert(el)
        else:  # Если стопка переполнена, то сначала создаем новую и уже туда вносим значение
            self.elems.append([])
            self.insert(el)

    def pop_out(self):
        if self.is_empty():
            result = 'Стэк пустой'
        elif self.stack_size() == 0:
            self.elems.pop()
        result = self.elems[self.stack_qty() - 1].pop()
        return result

    def get_val(self):
        return self.elems[self.stack_qty()-1][self.stack_size()-1]
