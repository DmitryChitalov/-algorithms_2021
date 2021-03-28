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


class StackOfPlate:
    def __init__(self):
        self.stacks = []

    def push(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка. В стопке по 2 тарелки"""
        if self.stacks == [] or len(self.stacks[len(self.stacks) - 1]) >= 2:
            self.stacks.append([])
            self.stacks[len(self.stacks) - 1].append(el)
        else:
            self.stacks[len(self.stacks) - 1].append(el)

    def pop_one_plate(self):
        if not self.stacks:
            return 'the stack is empty'
        elif len(self.stacks[len(self.stacks) - 1]) > 1:
            return self.stacks[len(self.stacks) - 1].pop()
        else:
            last_plate = self.stacks[len(self.stacks) - 1].pop()
            del self.stacks[len(self.stacks) - 1]
            return last_plate

    def pop_stack_plate(self):
        if not self.stacks:
            return 'the stack is empty'
        else:
            last_plate = self.stacks.pop()
            del self.stacks[len(self.stacks) - 1]
            return last_plate

    def get_one_plate(self):
        if not self.stacks:
            return 'the stack is empty'
        else:
            return self.stacks[len(self.stacks) - 1][-1]

    def get_stack_plate(self):
        if not self.stacks:
            return 'the stack is empty'
        else:
            return self.stacks[-1]


plates = StackOfPlate()
plates.push('red')
plates.push('green')
plates.push('white')
plates.push('blue')
print(plates.get_one_plate())
print(plates.pop_one_plate())
plates.push('red')
plates.push('green')
plates.push('white')
print(plates.get_stack_plate())
print(plates.pop_stack_plate())
