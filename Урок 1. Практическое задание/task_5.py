"""
Задание 5.
Задание на закрепление навыков работы со стеком

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
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

import copy


class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def get_value(self):
        return self.elems

    def clear_value(self):
        return self.elems.clear()

    def stack_size(self):
        return len(self.elems)


def plates_stack(amount, size):
    num_stack = StackClass()
    new_stack = StackClass()

    result = amount // size
    res = amount % size
    for i in range(result):
        for k in range(size):
            new_stack.push_in(7)
        num_stack.push_in(copy.deepcopy(new_stack.get_value()))
        new_stack.clear_value()
    for j in range(res):
        new_stack.push_in(6)
    num_stack.push_in(copy.deepcopy(new_stack.get_value()))

    return num_stack.get_value()


print(plates_stack(31, 6))






