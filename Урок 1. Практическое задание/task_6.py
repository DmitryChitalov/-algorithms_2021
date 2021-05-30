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


#Класс очередь
class QueueClass:
    def __init__(self):
        self.elems = []

    #Проверка пустой ли список очереди
    def is_empty(self):
        return self.elems == []

    #Вставка элемента в очередь
    def to_queue(self, item):
        self.elems.insert(0, item)

    #Удаление элемента из очереди
    def from_queue(self):
        return self.elems.pop()

    #Длина очереди
    def size(self):
        return len(self.elems)

#Класс "Доска задач"
class Board:
    def __init__(self):
        self.cur_queue = QueueClass()    #Базоваяя очередь
        self.revision_queue = QueueClass()   #Очередь на доработку задачи
        self.log = []  #Список решенных задач

    #Закрытие задачи и запись лога
    def closed_task(self):
        task = self.cur_queue.from_queue()
        self.log.append(task)

    #Отправка задачи на доработку
    def to_revision_task(self):
        task = self.cur_queue.from_queue()
        self.revision_queue.to_queue(task)

    #Добавление задачи в текущие задачи
    def to_current_queue(self, item):
        self.cur_queue.to_queue(item)

    #Возвращение задачи из доработки в текущую очередь
    def from_revision(self):
        task = self.revision_queue.from_queue()
        self.cur_queue.to_queue(task)

    #Текущая задача
    def current_task(self):
        return self.cur_queue.elems[len(self.cur_queue.elems) - 1]

    #Текущая задача в доработке
    def current_revision(self):
        return self.revision_queue.elems[len(self.revision_queue.elems) - 1]


if __name__ == '__main__':
    task_board = Board()
    task_board.to_current_queue('1')
    task_board.to_current_queue('2')
    task_board.to_current_queue('3')
    print(task_board.current_task())
    task_board.to_revision_task()
    print(task_board.current_revision())
    task_board.to_revision_task()
    print(task_board.current_revision())
    task_board.from_revision()
    print(task_board.current_revision())
    task_board.closed_task()
