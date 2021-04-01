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
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def isFull(self):
        if len(self.items) == 5:
            return True

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        listToStr = ' '.join([str(elem) for elem in self.items])
        return f'{listToStr}'


class SetOfStacks:

    def __init__(self):
        self.stacks = []

    def get_last_steck(self):
        if len(self.stacks) == 0:
            return 0
        return self.stacks[len(self.stacks)-1]

    def __len__(self):
        return len(self.stacks)

    def push(self, item):
        last = self.get_last_steck()
        if last != 0 and last.isFull() != True:
            last.push(item)
        else:
            stack = Stack()
            stack.push(item)
            self.stacks.append(stack)

    def __str__(self):
        listToStr = ' '.join([str(elem) for elem in self.stacks])
        return f'{listToStr}'
s = SetOfStacks()
while True:

    item = input("Enter item: ")
    s.push(item)
    print(f'Count stacks {len(s)}')
    print (str(s).strip('[]'))