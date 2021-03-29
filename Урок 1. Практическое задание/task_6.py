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


import random as r


class TaskBoard:
    def __init__(self):
        self.in_progress = []
        self.succes_done = 0  # счетчик успешно готовых задач

    def add_task(self, item):
        self.in_progress.insert(0, item)

    def task_filter(self, ready):
        """ Фильтр задач по готовности"""
        if ready:
            self.succes_done += 1
            return self.in_progress.pop()
        else:
            return self.add_task(self.in_progress.pop())

    def stack_size(self):
        return len(self.in_progress)


if __name__ == '__main__':
    go_work = TaskBoard()
    task_list = ['task_' + str(task) for task in range(r.randint(3, 5))]  # формирую список задач
    for i in task_list:  # добавляю все задачи
        go_work.add_task(i)
    print(f'Всего задач поступило > {go_work.stack_size()}')
    for el in task_list:  # рандомно определяю готовность задачи
        go_work.task_filter(r.randint(0, 1))

    print(f'Успешно сделано {go_work.succes_done} задачи(а)')
    print(f'Осталось на доработку: {", ".join(go_work.in_progress)}' if go_work.stack_size() > 0 else 'Все успешно '
                                                                                                      'сделано!')
