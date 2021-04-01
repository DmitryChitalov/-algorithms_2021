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


class StackClass:
    def __init__(self, max_size):
        self.elems = []
        self.max_size = max_size

    def is_empty(self):
        return self.elems == []

    def push_in(self, item):
        self.item = item

        if len(self.elems) > self.max_size:
            self.elems[len(self.elems) - 1].append(self.item)
        elif len(self.elems) == self.max_size:
            self.elems.insert(len(self.elems), [self.item])
        else:
            self.elems.append(self.item)

    def pop_out(self):
        if len(self.elems) > self.max_size:
            self.elems[len(self.elems) - 1].pop()
        else:
            self.elems.pop()

    def stack_size(self):
        return len(self.elems)

    def full_stack(self):
        return self.elems


stack = StackClass(3)
print(stack.is_empty())
stack.push_in(1)
stack.push_in(2)
stack.push_in(3)
stack.push_in(4)
stack.pop_out()
stack.push_in(10)
stack.push_in(20)
stack.push_in(30)
stack.push_in(40)
print(stack.full_stack())
print(stack.stack_size())
stack.pop_out()
print(stack.full_stack())
print(stack.stack_size())
print(stack.is_empty())
