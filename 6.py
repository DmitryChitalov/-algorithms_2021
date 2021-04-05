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

class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def push_to_queue(self,element):
        self.elements.insert(0,element)


    def pop_from_queue(self):
        self.elements.pop()


    def size(self):
        return len(self.elements)


class TaskBoard:
    def __init__(self):
        self.to_do = Queue()
        self.to_finalize = Queue()
        self.done = []

    def add_to_queue(self, element):
        """Добавляем задачу в текущие"""
        self.to_do.push_to_queue(element)
    def add_to(self,action):
        if action == 'to_finalize':
            task = self.to_do.pop_from_queue()
            self.to_finalize.push_to_queue(task)
        elif action == 'done':
            task = self.to_do.pop_from_queue()
            self.done.append(task)
        else:
            print('Неправильно выбрано действие')


'''first = Queue()
first.push_to_queue('Do homework')
first.push_to_queue('Do sports')
first.push_to_queue('Do programming')
first.pop_from_queue()
first.pop_from_queue() '''
my_task_board=TaskBoard()
my_task_board.add_to_queue('Do homework')
my_task_board.add_to('to_finalize')
my_task_board.add_to_queue('Do sports')
my_task_board.add_to('done')
print(my_task_board.to_do.elements)