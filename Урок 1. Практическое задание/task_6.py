"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""


class ClassQueue:

    auto_count = 0

    def __init__(self):
        self.base_list = []
        self.work_list = []
        self.done_list = []

    def push_work(self):
        self.work_list.insert(0, self.base_list[-1])
        return self.base_list.pop()

    def push_done(self):
        self.done_list.insert(0, self.work_list[-1])
        return self.work_list.pop()

    def push_in(self, el):
        ClassQueue.auto_count += 1
        if ClassQueue.auto_count >= 4:
            ClassQueue.push_work(self)
            if ClassQueue.auto_count >= 7:
                ClassQueue.push_done(self)
        return self.base_list.insert(0, el)


qe = ClassQueue()

qe.push_in(1)
qe.push_in(2)
qe.push_in(3)
qe.push_in(4)
qe.push_in(5)
qe.push_in(6)
qe.push_in(7)
qe.push_in(8)
qe.push_in(9)
qe.push_in(10)
print(f'Не решенные задачи\n{qe.base_list}')
print(f'Задачи на доработке\n{qe.work_list}')
print(f'Решенные задачи\n{qe.done_list}')
