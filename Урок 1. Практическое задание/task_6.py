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
        self.new_tasks = [] # Список новых задач
        self.completed_tasks = []  # Список завершенных задач
        self.repeat_tasks = []  # Список задач для дорешивания
    
    def add_new_task(self,task):    # Добавляет товую задачу
        self.new_tasks.insert(0,task)
    
    def get_new_task(self): # Прочитать очередную задачу
        if len(self.new_tasks)>0:
            return self.new_tasks[-1]
        else:
            return "No tasks available"
    
    def get_repeat_task(self): # Прочитать очередную задачу из списка на дорешивание
        if len(self.repeat_tasks)>0:
            return self.repeat_tasks[-1]
        else:
            return "No tasks available"

    def send_new_task_to_completed(self):   # Пометить очередную задачу как выполненную
        self.tasks_to_move = self.new_tasks.pop()
        self.completed_tasks.insert(0,self.tasks_to_move)
     
    def send_repeat_task_to_completed(self):   # Пометить задачу из очереди на дорешивание как выполненную
        self.tasks_to_move = self.repeat_tasks.pop()
        self.completed_tasks.insert(0,self.tasks_to_move)
        
    def send_new_task_to_repeat(self):  # Отправить очередную задачу на дорешивание
        self.tasks_to_move = self.new_tasks.pop()
        self.repeat_tasks.insert(0,self.tasks_to_move)
    
    def dump(self): # returns new_tasks, repeat_tasks, completed_tasks
        return (self.new_tasks,self.repeat_tasks,self.completed_tasks)
        
new_tasks_dispatcher = QueueClass()
print(new_tasks_dispatcher.get_new_task())
new_tasks_dispatcher.add_new_task("Resolve problem #1")
new_tasks_dispatcher.add_new_task("Resolve problem #2")
new_tasks_dispatcher.add_new_task("Resolve problem #3")
print(new_tasks_dispatcher.get_new_task())
print(new_tasks_dispatcher.dump())
new_tasks_dispatcher.send_new_task_to_completed()
print(new_tasks_dispatcher.dump())
new_tasks_dispatcher.send_new_task_to_repeat()
print(new_tasks_dispatcher.dump())
print(new_tasks_dispatcher.get_repeat_task())
new_tasks_dispatcher.send_repeat_task_to_completed()
print(new_tasks_dispatcher.dump())
new_tasks_dispatcher.send_new_task_to_completed()
print(new_tasks_dispatcher.dump())
        