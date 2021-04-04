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


class Stack:
    def __init__(self, n):
        self.items = []
        self.n = n

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.item = item
        if len(self.items) > self.n:
            self.items[len(self.items) - 1].append(self.item)
        elif len(self.items) == self.n:
            self.items.insert(len(self.items), [self.item])
        else:
            self.items.append(self.item)

    def pop(self):
        if len(self.items) > self.n:
            self.items[len(self.items) - 1].pop()
        else: self.items.pop()

    def size(self):
        return len(self.items)

    def fullStack(self):
        return self.items


stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(9)
stack.pop()
stack.push(10)
stack.push(100)
print(stack.fullStack())
stack.pop()
print(stack.size())
print(stack.fullStack())