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


class StackOfPlates:
    def __init__(self, max_plates_in_stack=10):
        self.elems = [[]]
        self.stackcount = 0
        self.maxinstack = max_plates_in_stack
        self.curr_stack = self.elems[self.stackcount]

    def clear(self):
        self.curr_stack = []
        self.elems = [[]]
        self.stackcount = 0
        return

    def push_in(self, el):
        for i in range(el):
            if sum(self.curr_stack) == self.maxinstack:
                self.elems.append([])
                self.stackcount += 1
                self.curr_stack = self.elems[self.stackcount]
                self.curr_stack.append(1)
            else:
                self.curr_stack.append(1)

    def pop_out(self):
        result = self.curr_stack.pop()
        if (len(self.curr_stack) == 0) and (self.stackcount > 0):
            self.stackcount -= 1
            self.elems.pop()
            self.curr_stack = self.elems[self.stackcount]
        return result

    def countstacks(self):
        return self.stackcount + 1

    def totalplates(self):
        return self.stackcount * self.maxinstack + len(self.curr_stack)


tmp = StackOfPlates(5)

tmp.push_in(16)
tmp.push_in(5)
print(f'Текущая кол-во: {tmp.totalplates()}\n'
      f'Текущее стопка: {tmp.countstacks()}\n\n')

tmp.pop_out()
print(f'Текущая кол-во: {tmp.totalplates()}\n'
      f'Текущее стопка: {tmp.countstacks()}\n\n')

tmp.clear()
print(f'\nТекущее кол-во: {tmp.totalplates()}\n'
      f'Текущая стопка: {tmp.countstacks()}\n')