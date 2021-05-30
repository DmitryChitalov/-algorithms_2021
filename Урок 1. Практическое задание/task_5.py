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


class Stack_Of_Plates:
    def __init__(self, max_stack):
        self.elems = []
        self.max_stack = max_stack

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[len(self.elems)-1]) < self.max_stack:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        plate = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) -1]) == 0:
            self.elems.pop()
        return plate

    def get_val(self):
        return self.elems[len(self.elems) - 1] [len(self.elems[len(self.elems) - 1]) - 1]

    def stack_size(self):
        number_plates = 0
        for stack in self.elems:
            number_plates += len(stack)
        return number_plates

    def number_of_stacks(self):
        return len(self.elems)

if __name__ == '__main__':
    plates = Stack_Of_Plates(3)
    plates.push_in('Plate1')
    plates.push_in('Plate2')
    plates.push_in('Plate3')
    plates.push_in('Plate4')
    plates.push_in('Plate5')
    plates.push_in('Plate6')
    plates.push_in('Plate7')
    print(plates)
    print(plates.pop_out())
    print(plates.get_val())
    print(plates.stack_size())
    print(plates.number_of_stacks())
    print(plates)
