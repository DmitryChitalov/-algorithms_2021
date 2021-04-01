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


class BaseQueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

    def show_elems(self):
        print(f'{self.__class__.__name__} {self.elems}')


class InWorkBoard(BaseQueueClass):
    def on_revision(self, on_revision_board):
        elem = self.elems.pop()
        on_revision_board.to_queue(elem)
        return elem

    def complete(self, complete_board):
        elem = self.elems.pop()
        complete_board.to_queue(elem)
        return elem


class OnRevisionBoard(BaseQueueClass):
    def to_work(self, in_work_board):
        elem = self.elems.pop()
        in_work_board.to_queue(elem)
        return elem


if __name__ == '__main__':
    print('создаем пустые объекты')
    in_work_board = InWorkBoard()
    on_revision_board = OnRevisionBoard()
    completed_board = BaseQueueClass()

    in_work_board.show_elems()
    on_revision_board.show_elems()
    completed_board.show_elems()

    print('помещаем объекты в очередь')

    in_work_board.to_queue('task1')
    in_work_board.to_queue('task2')
    in_work_board.to_queue('task3')

    in_work_board.show_elems()
    on_revision_board.show_elems()
    completed_board.show_elems()

    print('перемещаем объекты на доработку и в выполненные')

    in_work_board.on_revision(on_revision_board)
    in_work_board.complete(completed_board)

    in_work_board.show_elems()
    on_revision_board.show_elems()
    completed_board.show_elems()

    print('перемещаем объекты обратно в работу')
    on_revision_board.to_work(in_work_board)
    in_work_board.show_elems()
    on_revision_board.show_elems()
    completed_board.show_elems()
