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


class PlateStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.elements = []

    def is_empty(self):
        return self.elements == [[]]

    def push(self, elem):
        if len(self.elements[len(self.elements)-1]) < self.max_size:
            self.elements[len(self.elements)-1].append(elem)
        else:
            self.elements.append([])
            self.elements[len(self.elements)-1].append(elem)

    def pop(self):
        pop_plate = self.elements[len(self.elements)-1].pop()
        if len(self.elements[len(self.elements)-1]) == 0:
            self.elements.pop()
        return pop_plate

    def val(self):
        return self.elements[len(self.elements)-1][len(self.elements[len(self.elements)-1])-1]

    def plate_size(self):
        sum_of_plates = 0
        for stack in self.elements:
            sum_of_plates += len(stack)
        return sum_of_plates

    def stack_sum(self):
        return len(self.elements)




