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
import itertools


class LimitedStackClass:
    def __init__(self, limit):
        self.limit = limit
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def is_full(self):
        return self.len() == self.limit

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elems.append(el)
        return self.is_full()

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def len(self):
        return len(self.elems)

    def print(self):
        print(self.elems)


class PlatesStackClass:
    def __init__(self, limit):
        self.limit = limit
        self.stacks = [LimitedStackClass(limit)]

    def len(self):
        return len(self.stacks)

    def get_last_stack(self):
        return self.stacks[self.len() - 1]

    def is_empty(self):
        return self.len() == 1 & self.stacks[0].len() == 0

    def push_in(self, el=1):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if self.get_last_stack().is_full():
            self.stacks.append(LimitedStackClass(self.limit))
        self.stacks[self.len() - 1].push_in(el)

    def pop_out(self):
        if self.get_last_stack().is_empty():
            if self.len() != 1:
                self.stacks.pop()
        return self.get_last_stack().pop_out()

    def get_val(self):
        return self.get_last_stack().get_val()

    def print(self):
        for stack in self.stacks:
            stack.print()


PLATES_STACK = PlatesStackClass(4)

for _ in itertools.repeat(None, 9):
    PLATES_STACK.push_in()
    PLATES_STACK.print()
    print()

print()

for _ in itertools.repeat(None, 17):
    PLATES_STACK.push_in()

PLATES_STACK.print()
print()

for _ in itertools.repeat(None, 10):
    PLATES_STACK.pop_out()

PLATES_STACK.print()
print()

for _ in itertools.repeat(None, 7):
    PLATES_STACK.pop_out()

PLATES_STACK.print()
print()

for _ in itertools.repeat(None, 9):
    PLATES_STACK.pop_out()

PLATES_STACK.print()
print()
