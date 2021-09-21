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


class Stack:

    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if self.values:
            return self.values.pop(-1)
        else:
            print('Empty Stack')

    def peek(self):
        if self.values:
            return self.values[-1]
        else:
            print('Empty Stack')
            return None


class Stacks:

    def __init__(self, max_size):
        self.stacks = [Stack()]
        self.number_of_stack = 0
        self.max_size = max_size
        self.count = 0

    def push(self, item):
        if self.count < self.max_size:
            self.stacks[self.number_of_stack].push(item)
            self.count += 1
        else:
            self.stacks.append(Stack())
            self.number_of_stack += 1
            self.stacks[self.number_of_stack].push(item)
            self.count = 1

    def pop(self):
        if self.stacks[self.number_of_stack].values:
            self.count -= 1
            return self.stacks[self.number_of_stack].values.pop(-1)
        elif len(self.stacks) != 1:
            self.stacks.pop()
            self.number_of_stack -= 1
            self.count = 4
            return self.stacks[self.number_of_stack].values.pop(-1)

    def peek(self):
        if self.stacks[self.number_of_stack].values:
            return self.stacks[self.number_of_stack].values[-1]
        else:
            print('Empty Stack')


if __name__ == '__main__':

    some_stack = Stacks(5)

    some_stack.pop()

    for num in range(51):
        some_stack.push(num)
        print(some_stack.number_of_stack, some_stack.count)

    for num in range(11):
        print(some_stack.peek())
        print(some_stack.pop())
