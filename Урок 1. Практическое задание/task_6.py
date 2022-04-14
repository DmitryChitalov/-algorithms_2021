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

class MyQueueClass:
    def __init__(self):
        self.task = []             # задачи
        self.decided_task = []     # решеные задачи
        self.revision_task = []    # доработка задач

    def is_empty(self):
        return self.task == []

    def to_queue(self, item, where, status=True):
        if where == 'task':
            self.task.insert(0, item)
        elif where == 'decided_task' and item in self.task:
            self.chek_decided(item, status)
        elif where == 'revision_task':
            self.revision_task.insert(0, item)
        else:
            print('не правильный ввод  to_queue')


    def chek_decided(self, item, status):                           #проверка решенных задач
        if status == True:                                    # если да то
            ind = self.task.index(item)                         # узнаем индекс
            self.decided_task.insert(0, item)                   # если да то
            return self.task.pop(ind)
        elif status == False:                                 # если нет то отправляем на доработку
            return self.to_queue(item, 'revision_task')
        else:
            print('не правильный ввод  chek_decided')


    # def del_decided(self):         # удаление решенной задачи из очереди задач


    def from_queue(self,where):   # удаление с очереди
        if where == 'task':
            return self.task.pop()
        elif where == 'decided_task':
            return self.decided_task.pop()
        elif where == 'revision_task':
            return self.revision_task.pop()
        else:
            print('не правильный ввод  to_queue')


    def size_task(self):
        return len(self.task)

if __name__ == '__main__':
    my_queue = MyQueueClass()

    my_queue.is_empty()                                     # проверка очереди -> True

    my_queue.to_queue('выкинуть мусор', 'task')
    my_queue.to_queue('проснутся', 'task')
    my_queue.to_queue('сделать чай', 'task')
    my_queue.to_queue('пойти в магазин', 'task')
    my_queue.to_queue('сделать кофе', 'task')
    my_queue.to_queue('сделать зарядку', 'task')            # наполнение очереди

    my_queue.is_empty()                                     # проверка очереди -> False

    print(my_queue.task)
    print()

    my_queue.to_queue('выкинуть мусор', 'decided_task')     # перемещение задачи в 'revision_task' и удаление задачи из очереди "task"

    print(my_queue.task)                                    # проверка очереди
    print(my_queue.decided_task)                            # проверка очереди

    my_queue.to_queue('проснутся', 'decided_task', False)   # попытка перемещение задачи в 'revision_task' и удаление задачи из очереди "task", с атрибутом False

    print(my_queue.decided_task)                            # проверка очереди
    print(my_queue.task)                                    # проверка очереди
    print(my_queue.revision_task)                           # проверка очереди

    my_queue.from_queue('revision_task')                    # удаление задачи из 'revision_task'

    print(my_queue.revision_task)                           # проверка очереди


















