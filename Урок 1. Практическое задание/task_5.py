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

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        if len(self.stack[len(self.stack) - 1]) >= 10:
            self.stack.append([])
        self.stack[len(self.stack) - 1].append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack[len(self.stack) - 1].pop()
        if len(self.stack[len(self.stack) - 1]) == 0:
            self.stack.pop()
        return removed

    def get(self):
        return self.stack[len(self.stack) - 1].[len(self.stack[len(self.stack) - 1]) - 1]

    def size(self):
        lenght = [len(self.stack[i]) for i in range(len(self.stack[len(self.stack) - 1]))]
        return lenght

my_stack = Stack()
for i in range(100, 300, 7):
    my_stack.push(i)

print(my_stack.size())
print(my_stack.get())
