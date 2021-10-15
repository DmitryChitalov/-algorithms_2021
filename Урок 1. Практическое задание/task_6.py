"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


from random import randint as ran


class StackClass:
    def __init__(self):
        self.tasks = []
        self.resolved = []
        self.unsolved = []

    def is_empty(self):
        return self.tasks == []

    def push_in(self, el, list_x):
        list_x.append(el)

    def pop_out(self):
        return self.tasks.pop()

    def get_val(self):
        return self.tasks[-1]

    def stack_size(self, list_x):
        return len(list_x)

    def solving_tasks(self):
        y = self.get_val()
        print(y)
        x = input('Enter resolved or unsolved')
        if x == 'resolved':
            self.push_in(y, self.resolved)
            self.pop_out()
        elif x == 'unsolved':
            self.push_in(y, self.unsolved)
        else:
            print('incorrect entered!')
            self.solving_tasks()


if __name__ == '__main__':
    x = StackClass()
    for i in range(100):
        x.push_in(ran(1, 10), x.tasks)
    print(x.stack_size(x.tasks))
    x.solving_tasks()
    print(x.stack_size(x.tasks))
    print(x.stack_size(x.resolved))
    print(x.stack_size(x.unsolved))
