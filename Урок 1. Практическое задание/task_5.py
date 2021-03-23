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


class StackPlates:
    def __init__(self):
        self.stack_size = 5
        self.stack = [[]]

    def plate_number(self):
        return len(self.stack[:-1]) * self.stack_size + len(self.stack[-1])

    def stack_in(self):
        if len(self.stack[-1]) == self.stack_size:
            self.stack.append([])
        self.stack[-1].append(f"Plate-{self.plate_number()+1}")

    def stack_out(self):
        if self.plate_number() == 0:
            print('There is not plates')
        else:
            if len(self.stack[-1]) == 1:
                self.stack.pop()
            else:
                self.stack[-1].pop()

    def __repr__(self):
        return f"Стопок - {len(self.stack)-1} по {self.stack_size} тарелок в каждой \n " \
               f" и одна стопка с количеством тарелок - {len(self.stack[-1])}"


t = StackPlates()

for i in range(13):
    t.stack_in()
print(t)

for i in range(3):
    t.stack_out()
print(t)