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


class Todo:
    def __init__(self):
        self.tasks = [
            {
              'id': 1,
              'task': 'Создать класс'
            },
            {
              'id': 2,
              'task': 'Описать класс'
            },
            {
              'id': 3,
              'task': 'Создать методы'
            },
            {
              'id': 4,
              'task': 'Сделать оптимальную хрень'
            },
        ]
        self.check_tasks = []
        self.rewrite = []
        self.completed = []
    
    def get_position(self, lst, idn):
      for task in lst:
        if task['id'] == idn:
          return lst.index(task)

    def get_lists(self, description, lst):
      print(f"\n{description} задания:")
      if len(lst) == 0:
        print('\tЗаданий нет')
      for task in lst:
        print(f"\t{task['id']}. {task['task']}")
        # print(task)

    def add_task(self, content):
      self.tasks.append({
        'id': self.tasks[-1]['id']+1,
        'task': content
      })
    
    def to_next_step(self, from_state, to_state, idn):
      for task in from_state:
        if task['id'] == idn:
          to_state.append(from_state.pop(self.get_position(from_state ,idn)))


sess = Todo()
sess.get_lists("Новые", sess.tasks)
sess.add_task('Проверка')
sess.to_next_step(sess.tasks, sess.check_tasks, 3)
sess.to_next_step(sess.tasks, sess.check_tasks, 1)
sess.to_next_step(sess.check_tasks, sess.rewrite, 1)
sess.to_next_step(sess.check_tasks, sess.completed, 3)
sess.to_next_step(sess.tasks, sess.check_tasks, 2)
print('\n*******************************************************')
sess.get_lists("Новые", sess.tasks)
sess.get_lists("На проверку", sess.check_tasks)
sess.get_lists("На доработку", sess.rewrite)
sess.get_lists("Выполенные", sess.completed)