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
class QueueClassMY:
    def __init__(self):
        self.tasks = []
        self.solved_tasks = []
        self.rework_tasks = []
    def to_queue(self, item):
        self.tasks.insert(0, item)
    def from_queue(self):
        return self.tasks.pop()
    def size(self):
        return f'Текущих задач: {len(self.tasks)}'
    def solved_task(self):
        task = self.from_queue()
        self.solved_tasks.append(task)
        return f'Задача {task} выполнена'
    def not_solved_task(self):
        task = self.from_queue()
        self.rework_tasks.append(task)
        return f'Все херня, переделывай {task}'
    def is_rework_tasks(self):
        return f'Задач на доработку: {len(self.rework_tasks)}'

if __name__ == '__main__':
    qc_obj = QueueClassMY()
    """Добавляем задачи"""
    qc_obj.to_queue('task1')
    qc_obj.to_queue('task2')
    qc_obj.to_queue('task3')
    qc_obj.to_queue('task4')
    qc_obj.to_queue('task5')
    print(qc_obj.size())
    """Согласованные задачи"""
    print(qc_obj.solved_task())
    print(qc_obj.solved_task())
    print(qc_obj.solved_task())
    print(qc_obj.size())
    """Задачи на доработку"""
    print(qc_obj.not_solved_task())
    print(qc_obj.not_solved_task())
    print(qc_obj.size())
    print(qc_obj.is_rework_tasks())
    #print(qc_obj.solved_task())