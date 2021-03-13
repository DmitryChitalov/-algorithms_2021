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
from random import randint


class TaskBoard:
    def __init__(self):
        self.task_list = []
        self.result_list = []
        self.not_result_list = []

    def new_task(self, task):
        self.task_list.append(task)

    def get_task(self, status='new'):
        if status == 'new':
            return self.task_list.pop(0)
        if status == 'done':
            return self.result_list.pop(0)
        if status == 'bad':
            return self.not_result_list.pop(0)

    def push_task(self, task, new_status='done'):
        if new_status == 'done':
            self.result_list.append(task)
        if new_status == 'bad':
            self.not_result_list.append(task)

    def get_tasks(self, status='all'):
        if status == 'all':
            return f'Все задания: {self.task_list}\nВыполненные задания: {self.result_list}\n' \
                   f'Не выполненные задания: {self.not_result_list}'
        if status == 'done':
            return f'Выполненные задания: {self.result_list}'
        if status == 'bad':
            return f'Не выполненные задания: {self.not_result_list}'
        else:
            return 'что-то пошло не так'


task_to_work = TaskBoard()

for i in range(5):
    task_to_work.new_task(f'Задача_{randint(1, 100)} - {i}')

#  смотрим все добавленные задачи
print(task_to_work.get_tasks())
print()
# берем новую задачу в работу
work_1 = task_to_work.get_task()
print(work_1)
print()
# выполняем ее и смотрим общий статус по всем задачам
task_to_work.push_task(work_1, 'done')
print(task_to_work.get_tasks())
print()
# берем еще одну задачу и не выполняем ее и смотрим общий статус по всем задачам
work_2 = task_to_work.get_task()
task_to_work.push_task(work_2, 'bad')
print(task_to_work.get_tasks())
print()
# берем не выполненную задачу и изменяем ее
work_3 = task_to_work.get_task('bad')
task_to_work.push_task(work_3, 'done')
print(task_to_work.get_tasks())
print()
# смотрим только выполненные задачи
print(task_to_work.get_tasks('done'))
