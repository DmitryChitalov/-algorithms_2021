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
# структура доски по умолчанию: {'inbox': [], 'planning': [], 'working': [], 'finished': []}


class Desk:
    def __init__(self):
        self.desk_list = {'inbox': [], 'planning': [], 'working': [], 'finished': []}

    def show_desk(self):
        print('\nДоска:')
        for el in self.desk_list:
            print(el)
            if not self.desk_list.get(el):
                print('-\n')
            else:
                for i in range(len(self.desk_list.get(el))):
                    print(self.desk_list.get(el)[i], end='; ')
                print('\n')

    def new_task(self, task_name):
        print('')
        self.desk_list.get('inbox').append(task_name)
        print(f"Задача {task_name} добавлена, список inbox задач: {self.desk_list.get('inbox')}")

    def inbox_to_planning_all(self):
        print('')
        while self.desk_list.get('inbox'):
            self.desk_list.get('planning').append(self.desk_list.get('inbox').pop())
        print(f"Все входящие задачи перенесены в список planning: {self.desk_list.get('planning')}")

    def move_one_task(self, from_status, to_status, task_name):
        print('')
        self.desk_list.get(from_status).remove(task_name)
        self.desk_list.get(to_status).append(task_name)
        print(f"Задача {task_name} перенесена из {from_status} в {to_status}, список обновлен: "
              f"\n{to_status}:"
              f"\n{self.desk_list.get(to_status)}")

    def revision(self, old_task_name, new_task_name):
        print('')
        self.desk_list.get('planning').remove(old_task_name)
        self.desk_list.get('planning').append(new_task_name)
        print(f"Задача {old_task_name} в planning списке изменена: {self.desk_list.get('planning')}")

    def inbox_to_planning_one(self, task_name):
        self.move_one_task('inbox', 'planning', task_name)

    def get_working(self, task_name):
        self.move_one_task('planning', 'working', task_name)

    def for_revision(self, task_name):
        self.move_one_task('working', 'planning', task_name)

    def finishing(self, task_name):
        self.move_one_task('working', 'finished', task_name)


Desk_obj = Desk()
Desk_obj.show_desk()
Desk_obj.new_task('пропылесосить')
Desk_obj.new_task('постирать')
Desk_obj.inbox_to_planning_all()
Desk_obj.new_task('помыть посуду')
Desk_obj.inbox_to_planning_one('помыть посуду')
Desk_obj.revision('помыть посуду', 'помыть посуду(не забыть сковородку)')
Desk_obj.get_working('помыть посуду(не забыть сковородку)')
Desk_obj.for_revision('помыть посуду(не забыть сковородку)')
Desk_obj.get_working('помыть посуду(не забыть сковородку)')
Desk_obj.finishing('помыть посуду(не забыть сковородку)')
Desk_obj.show_desk()
