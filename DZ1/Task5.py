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
        self.stack = []

    def __str__(self):
        s = ' '
        for el in self.stack:
            s += el.__str__() + ' '
        return s + '\n'

    def empty(self):
        return (len(self.stack) == 0)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.empty():
            return None
        else:
            return self.stack.pop()


class Stacks:
    def __str__(self):
        return self.stacks.__str__()

    def __init__(self, max_size):
        self.stacks = Stack()
        self.max_size = max_size
        self.count = 0
        self.stacks.push(Stack())

    def push(self, item):
        if self.count < self.max_size:
            temp = self.stacks.pop()
            temp.push(item)
            self.stacks.push(temp)
            self.count += 1
        else:
            temp = Stack()
            temp.push(item)
            self.stacks.push(temp)
            self.count = 1

    def pop(self):
        if self.stacks.empty():
            return None
        else:
            temp = self.stacks.pop()
            if temp.empty():
                return None
            else:
                item = temp.pop()
                if not temp.empty():
                    self.stacks.push(temp)
                return item


test = Stacks(3)
for i in range(10):
    test.push(i)
print(test)
for i in range(3):
    test.pop()
print(test)
