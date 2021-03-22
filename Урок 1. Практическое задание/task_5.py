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


class Plates:
    def __init__(self, size):
        self.stack = [[]]
        self.size = size

    def is_empty(self):
        return self.stack == [[]]

    def stack_plates_append(self, plate):
        if len(self.stack[len(self.stack) - 1]) < self.size:
            self.stack[len(self.stack) - 1].append(plate)
        else:
            self.stack.append([])
            self.stack[len(self.stack) - 1].append(plate)

    def stack_plates_pop(self):
        return self.stack.pop([len(self.stack) - 1][0])

    def show_stacks(self):
        return self.stack

    def get_el_value(self):
        return self.stack[len(self.stack) - 1][len(self.stack[len(self.stack) - 1]) - 1]

    def stacks_count(self):
        return len(self.stack)


if __name__ == "__main__":
    stack_object = Plates(3)
    stack_object.stack_plates_append('p_1')
    stack_object.stack_plates_append('p_1')
    stack_object.stack_plates_append('p_1')
    stack_object.stack_plates_append('p_1')
    stack_object.stack_plates_append('p_1')
    stack_object.stack_plates_append('p_1')
    stack_object.stack_plates_append('p_1')
    stack_object.stack_plates_append('p_1')
    stack_object.stack_plates_append('p_1')
    stack_object.stack_plates_append('p_1')
    print(stack_object.show_stacks())
    print(stack_object.stacks_count())
    stack_object.stack_plates_pop()
    print(stack_object.show_stacks())
