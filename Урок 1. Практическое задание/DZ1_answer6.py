"""
Задание 6.
Задание на закрепление навыков работы с очередью
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
"""

class QueueTaskClass:                                       #Класс очереди
    def __init__(self):
        self.tasks = []                                     #список текущих задач

    def is_empty(self):                                     #проверка списка на пустоту
        return self.tasks == []

    def add_task(self, task):                               #добавления задачи в список
        self.tasks.insert(0, task)

    def from_queue_to_other_queue(self, to_queue):          #перемещение задачи в другую очередь (доску задач)
        to_queue.add_task(self.tasks.pop())

    def size(self):                                         #размер списка текущих задач
        return len(self.tasks)

current_tasks = QueueTaskClass()                    #список текущих задач (базовая)
rework_tasks = QueueTaskClass()                     #список задач на переработку
completed_tasks = QueueTaskClass()                  #список решенных задач

print('Ситуация - просто добавление в базовую доску')
current_tasks.add_task('task1')
current_tasks.add_task('task2')
current_tasks.add_task('task3')
current_tasks.add_task('task4')
current_tasks.add_task('task5')
current_tasks.add_task('task6')
current_tasks.add_task('task7')
current_tasks.add_task('task8')
print(f'Текущие задачи (базовая): {current_tasks.tasks}')
print(f'Текущие задачи (на переработку): {rework_tasks.tasks}')
print(f'Выполненные задачи: {completed_tasks.tasks}')
print('########################################################################')

print('Ситуация - перемещение задач на доработку из базовой')
current_tasks.from_queue_to_other_queue(rework_tasks)
current_tasks.from_queue_to_other_queue(rework_tasks)
current_tasks.from_queue_to_other_queue(rework_tasks)
print(f'Текущие задачи (базовая): {current_tasks.tasks}')
print(f'Текущие задачи (на переработку): {rework_tasks.tasks}')
print(f'Выполненные задачи: {completed_tasks.tasks}')
print('########################################################################')

print('Ситуация - перемещение задач в решеные из базовой')
current_tasks.from_queue_to_other_queue(completed_tasks)
current_tasks.from_queue_to_other_queue(completed_tasks)
current_tasks.from_queue_to_other_queue(completed_tasks)
print(f'Текущие задачи (базовая): {current_tasks.tasks}')
print(f'Текущие задачи (на переработку): {rework_tasks.tasks}')
print(f'Выполненные задачи: {completed_tasks.tasks}')
print('########################################################################')

print('Ситуация - перемещение задач из доработки в базовые')
rework_tasks.from_queue_to_other_queue(current_tasks)
rework_tasks.from_queue_to_other_queue(current_tasks)
print(f'Текущие задачи (базовая): {current_tasks.tasks}')
print(f'Текущие задачи (на переработку): {rework_tasks.tasks}')
print(f'Выполненные задачи: {completed_tasks.tasks}')