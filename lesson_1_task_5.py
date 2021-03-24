import random # для определения кол-ва тарелок и макс размера стеков

class StackClass:
    def __init__(self, max_size):
        self.elems = [[]]
        self.max_size = max_size

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[0]) >= self.max_size:
            self.elems.insert(0, [])
        self.elems[0].insert(0, el)

    def pop_out(self):
        if self.is_empty():     # Проверка на извлечение из пустого стека
            return None
        else:
            result = self.elems[0].pop(0)
            if len(self.elems[0]) == 0 and len(self.elems) > 1:
                self.elems.pop(0)
            return result

    def get_top(self):
        if self.is_empty():     # Проверка на извлечение из пустого стека
            return None
        else:
            return self.elems[0][0]

## Исходные данные, создание экземпляра класса и вызов функций
stack_size = random.randint(2,6)
SC_OBJ = StackClass(stack_size)
print ('Макс кол-во элементов в стеках:', stack_size)

# заполнение стеков
plate_qty = random.randint(10,20)
print('Общее количество тарелок: ', plate_qty)
for i in range(plate_qty):
    SC_OBJ.push_in(i)
print(SC_OBJ)
# удаление элементов сверху (начало списка)
for i in range(plate_qty):
    print('Удаляем :', SC_OBJ.get_top())
    SC_OBJ.pop_out()
    print(SC_OBJ)
