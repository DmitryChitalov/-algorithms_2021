"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""
import random

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
        if self.is_empty():
            return None
        else:
            result = self.elems[0].pop(0)
            if len(self.elems[0]) == 0 and len(self.elems) > 1:
                self.elems.pop(0)
            return result

    def get_top(self):
        if self.is_empty():
            return None
        else:
            return self.elems[0][0]

stack_size = random.randint(2,6)
SC_OBJ = StackClass(stack_size)
print ('Макс кол-во элементов в стеках:', stack_size)

plate_qty = random.randint(10,20)
print('Общее количество тарелок: ', plate_qty)
for i in range(plate_qty):
    SC_OBJ.push_in(i)
print(SC_OBJ)

for i in range(plate_qty):
    print('Удаляем :', SC_OBJ.get_top())
    SC_OBJ.pop_out()
    print(SC_OBJ)