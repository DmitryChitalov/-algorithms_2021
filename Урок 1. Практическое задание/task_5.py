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
        self.stack_list = []

    def is_empty(self):
        return self.stack_list == []

    def push(self, element):
        self.stack_list.append(element)

    def pop(self):
        return self.stack_list.pop()

    def peek(self):
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)


class Plates:
    def __init__(self, capacity):
        self.stacks = []
        self.stacks.append(Stack())
        self.capacity = capacity

    def is_empty(self):
        return len(self.stacks) == 1 and self.stacks[0].is_empty()

    def push(self, element):
        if self.stacks[-1].size() >= self.capacity:
            self.stacks.append(Stack())
        self.stacks[-1].push(element)

    def pop(self):
        result = self.stacks[-1].pop()
        if self.stacks[-1].is_empty() and len(self.stacks) > 1:
            self.stacks.pop()
        return result

    def peek(self):
        return self.stacks[-1].peek()

    def last_stack_size(self):
        return self.stacks[-1].size()

    def number_of_stacks(self):
        return len(self.stacks)


test = Plates(5)
print('Стек пустой?', test.is_empty())
test.push(1)
test.push(2)
test.push(3)
test.push(4)
test.push(5)
test.push(6)
print('Стек пустой?', test.is_empty())
print('Количество стопок тарелок', test.number_of_stacks())
print('Высота последней стопки тарелок', test.last_stack_size())
print('Должно быть шесть', test.pop())
print('Стек пустой?', test.is_empty())
print('Количество стопок тарелок', test.number_of_stacks())
print('Высота последней стопки тарелок', test.last_stack_size())
print('Должно быть пять', test.pop())
print('Стек пустой?', test.is_empty())
print('Количество стопок тарелок', test.number_of_stacks())
print('Высота последней стопки тарелок', test.last_stack_size())
