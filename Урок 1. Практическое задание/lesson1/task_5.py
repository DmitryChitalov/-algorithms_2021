class StackClass:
    """
        Класс создания стека
    """
    def __init__(self):
        self.elems = []

    def is_empty(self):
        """Проверка пустой ли стек"""
        return self.elems == []

    def push_in(self, element):
        """
            Предполагаем, что верхний элемент стека находится в конце
        """
        self.elems.append(element)

    def pop_out(self):
        """Достаем элемент из стека"""
        return self.elems.pop()

    def get_val(self):
        """Получаем значение элемента стека"""
        return self.elems[-1]

    def stack_size(self):
        """Количество элементов в стеке"""
        return len(self.elems)


class StacksOfPlates:
    """Класс стопка тарелок"""
    def __init__(self, size):
        self.size = size    # высота стопки
        self.stacks_of_plates = []

    def stack_is_full(self):
        """Проверка можно ли добавять в стопку"""
        return self.stacks_of_plates[-1].stack_size() == self.size

    def stack_is_empty(self):
        """Проверка опустошена ли стопка"""
        return not self.stacks_of_plates[-1].stack_size()

    def push_in(self):
        """Если стопка заполнена, добавляем новую, затем в нее добавляем тарелку"""
        if self.stacks_of_plates:
            if self.stack_is_full():
                self.stacks_of_plates.append(StackClass())
        else:
            self.stacks_of_plates.append(StackClass())
        self.stacks_of_plates[-1].push_in('|')

    def pop_out(self):
        """Забираем тарелку, если в стопке не осталось тарелок то удаляем ее из списка"""
        if self.stacks_of_plates[-1].stack_size():
            self.stacks_of_plates[-1].pop_out()
        if self.stack_is_empty():
            self.stacks_of_plates.pop()

    def show_last_stack(self):
        """Показать последнюю стопку (тарелки в виде символа '|')"""
        if self.stacks_of_plates:
            return len(self.stacks_of_plates[-1].elems) * '|'
        return 'Стопок нет'

    def show_all_stacks(self):
        """Показать все стопки (стопки в виде символа '=')"""
        return len(self.stacks_of_plates) * ' ='

    def total_stacks(self):
        """Посчитать все стопки"""
        return len(self.stacks_of_plates)

    def total_plates(self):
        """Посчитать все тарелки"""
        if self.stacks_of_plates:
            return self.total_stacks() * self.size - \
                (self.size - self.stacks_of_plates[-1].stack_size())
        return 0


plates = StacksOfPlates(10)

for _ in range(100):
    plates.push_in()
print(f'Всего стопок: {plates.total_stacks()}')
print(plates.show_all_stacks())
print(f'Всего тарелок: {plates.total_plates()}')
print(plates.show_last_stack())

print('-' * 1000)

for _ in range(35):
    plates.pop_out()
print(f'Всего стопок: {plates.total_stacks()}')
print(plates.show_all_stacks())
print(f'Всего тарелок: {plates.total_plates()}')
print(plates.show_last_stack())

print('-' * 1000)

for _ in range(65):
    plates.pop_out()
print(f'Всего стопок: {plates.total_stacks()}')
print(plates.show_all_stacks())
print(f'Всего тарелок: {plates.total_plates()}')
print(plates.show_last_stack())
