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


class PlateStacks:
    def __init__(self):
        self.elems = [[]]
        self.max_plate = 3
        self.cur_stack = 0

    def is_empty(self):
        return self.elems == [[]]

    def put_plate_in(self, el):
        if len(self.elems[self.cur_stack]) == self.max_plate:
            self.elems.append([])
            self.cur_stack += 1
            self.elems[self.cur_stack].append(el)
        else:
            self.elems[self.cur_stack].append(el)

    def remove_plate(self):
        rem_plates = self.elems[self.cur_stack].pop()
        if len(self.elems[self.cur_stack]) == 0:
            self.elems.pop()
            self.cur_stack -= 1
        return rem_plates

    def all_plates(self):
        plates = self.max_plate * (len(self.elems) - 1) + len(self.elems[self.cur_stack])
        return plates

    def stack_size(self):
        return len(self.elems[self.cur_stack])


if __name__ == '__main__':
    stacks = PlateStacks()

    print(stacks.is_empty())
    stacks.put_plate_in(2)
    stacks.put_plate_in(9)
    stacks.put_plate_in(7)
    stacks.put_plate_in(1)
    stacks.put_plate_in(2)
    stacks.put_plate_in(2)
    stacks.put_plate_in(2)
    print(stacks.is_empty())
    print(stacks.stack_size())
    stacks.put_plate_in(4)
    print(stacks.stack_size())
    stacks.remove_plate()
    print(stacks.stack_size())
