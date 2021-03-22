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

class QueueClass:
    def __init__(self):
        self.elems = []

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == []

    def to_queue(self, el):
        if el != None:
            self.elems.insert(0, el)

    def from_queue(self):
        if not self.is_empty():
            return self.elems.pop()
        else:
            return None

    def size(self):
        return len(self.elems)

class TaskClass:
    def __init__(self):
        self.base_queue = QueueClass()      # Базовая очередь задач
        self.rework_queue = QueueClass()    # Очередь для доработок
        self.finish_list = []               # Список с решенными задачами

    def __str__(self):
        cur_tasks = 'Перечень текущих задач:\n' + str(self.base_queue) +\
                    '\nПеречень задач "на доработке":\n' + str(self.rework_queue) +\
                    '\nПеречень выполненных задач:\n' + str(self.finish_list)
        return cur_tasks

    def to_finish(self):                    # Решенную задачу отправляем в список
        self.finish_list.append(self.base_queue.from_queue())

    def to_rework(self):                    # Нерешенную задачу отправляем в очередь доработок
        self.rework_queue.to_queue(self.base_queue.from_queue())

    def to_base(self, task):                # Добавим задачу в основную очередь
        self.base_queue.to_queue(task)

    def from_rework(self):                  # Извлечем задачу из очереди доработок (и добавим в основную)
        self.base_queue.to_queue(self.rework_queue.from_queue())

if __name__ == '__main__':
    my_task = TaskClass()
    my_task.to_base('Посадить дерево')
    my_task.to_base('Заработать миллион')
    my_task.to_base('Построить дом')
    my_task.to_base('Вырастить дочь')
    my_task.to_base('Вырастить вторую дочь')
    print(my_task)
    for i in range(3):
        my_task.to_finish()
        my_task.to_rework()
        print(my_task)
    my_task.from_rework()
    print(my_task)

