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


class HelpDesk:
    def __init__(self):
        self.__clean_board = []
        self.__in_process = []
        self.__accepted = []
        self.__finished = []

    def is_empty(self):
        return self.__clean_board == []

    def new_task(self, item):
        self.__clean_board.append(item)

    def in_process(self):
        if self.__clean_board:
            self.__in_process.append(self.__clean_board.pop(0))
            return f'Задача {self.__in_process[-1]} в работе'
        return 'Все задачи в работе или выполнены'

    def task_to_fix(self):
        if self.__in_process:
            self.__accepted.append(self.__in_process.pop(0))
            return f'Задача {self.__accepted[-1]} принята к рассмотрению'
        return 'Нет задач в очереди'

    def task_to_done(self, queue):
        msg = 'Выполнено'
        if queue == 'Выполняется' and self.__in_process:
            self.__finished.append(self.__in_process.pop(0))
        elif queue == 'Исправлено' and self.__accepted:
            self.__finished.append(self.__accepted.pop(0))
        else:
            msg = 'Ошибка выполнения'
        return msg

    def size(self):
        return len(self.__clean_board)


if __name__ == '__main__':
    helpdesk = HelpDesk()
    print(helpdesk.is_empty())
    for i in range(1, 11):
        helpdesk.new_task(i)
    for i in range(10):
        print(helpdesk.in_process())
    for i in range(10):
        if i % 5 == 0:
            print(helpdesk.task_to_fix())
        else:
            print(helpdesk.task_to_done('Выполняется'))
    print(helpdesk.size())
