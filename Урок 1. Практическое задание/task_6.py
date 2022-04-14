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


class TaskBoard:
    def __init__(self):
        self.to_do = []
        self.in_work = []
        self.revision = []
        self.done = []

    def __is_empty__(self, list):
        if list == 'to_do':
            return self.to_do == []
        elif list == 'in_work':
            return self.in_work == []
        elif list == 'revision':
            return self.revision == []
        else:
            return self.done == []

    def new_task(self, task):
        """
        добаление задачи
        """
        self.to_do.insert(0, task)

    def see_list(self, list_to_view):
        """
        покажет задачи в указанном листе
        варианты запросов:
        начальный список задач - to_do
        в работе - in_work
        на доработке - revision
        сделано - done
        """
        if list_to_view == 'to_do' and not self.__is_empty__(list_to_view):
            return ', '.join(self.to_do)
        elif list_to_view == 'in_work' and not self.__is_empty__(list_to_view):
            return ', '.join(self.in_work)
        elif list_to_view == 'revision' and not self.__is_empty__(list_to_view):
            return ', '.join(self.revision)
        elif list_to_view == 'done' and not self.__is_empty__(list_to_view):
            return ', '.join(self.done)
        else:
            return f'список задач {list_to_view} пуст'

    def to_in_work_list(self):
        """
        перемещение задачи из листа "сделать" в лист "в работе"
        """
        if not self.__is_empty__('to_do'):
            self.in_work.insert(0, self.to_do.pop())
        else:
            print('список to_do пуст')

    def to_done_list(self):
        """
        перемещение задачи из листа "в работе" в лист "сделано"
        """
        if not self.__is_empty__('in_work'):
            self.done.insert(0, self.in_work.pop())
        else:
            print('список in_work пуст')

    def to_revision(self):
        """
        перемещение задани из "сделано" на "доработку"
        """
        if not self.__is_empty__('done'):
            self.revision.insert(0, self.done.pop())
        else:
            print('список done пуст')

    def from_revision(self):
        """
        из доработки в готово
        """
        if not self.__is_empty__('revision'):
            self.done.insert(0, self.revision.pop())
        else:
            print('список revision пуст')

    def size(self, list):
        if list == 'to_do':
            return len(self.to_do)
        elif list == 'in_work':
            return len(self.in_work)
        elif list == 'revision':
            return len(self.revision)
        else:
            return len(self.done)


if __name__ == '__main__':
    task_board = TaskBoard()
    print(task_board.see_list('to_do'))
    print(task_board.see_list('in_work'))
    print(task_board.see_list('revision'))
    print(task_board.see_list('done'))
    task_board.new_task('первая задача')
    task_board.new_task('вторая задача')
    task_board.new_task('третья задача')
    task_board.new_task('четвертая задача')
    print(task_board.see_list('to_do'))
    print(task_board.see_list('in_work'))
    print(task_board.see_list('revision'))
    print(task_board.see_list('done'))

    task_board.to_in_work_list()
    task_board.to_in_work_list()
    print(task_board.see_list('to_do'))
    print(task_board.see_list('in_work'))
    print(task_board.see_list('revision'))
    print(task_board.see_list('done'))
    task_board.to_in_work_list()
    task_board.to_done_list()
    task_board.to_done_list()
    print(task_board.see_list('to_do'))
    print(task_board.see_list('in_work'))
    print(task_board.see_list('revision'))
    print(task_board.see_list('done'))

    task_board.to_revision()
    print(task_board.see_list('to_do'))
    print(task_board.see_list('in_work'))
    print(task_board.see_list('revision'))
    print(task_board.see_list('done'))

    task_board.from_revision()
    task_board.from_revision()
    print(task_board.see_list('to_do'))
    print(task_board.see_list('in_work'))
    print(task_board.see_list('revision'))
    print(task_board.see_list('done'))


