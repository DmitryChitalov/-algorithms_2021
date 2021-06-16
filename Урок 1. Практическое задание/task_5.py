
"""
Задание 5.
Задание на закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.
После реализации структуры, проверьте ее работу на различных сценариях
Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

class StackClass:
    def __init__(self):
        self.my_list = [[]]

    # Очистка всего листа
    def is_empty(self):
        self.my_list = [[]]
        return f'func is_empty = {self.my_list}.'

    # Обозначили максимальное кол-во элементов в стопке 4
    def push_in(self, el):
        self.index_last_stack = len(self.my_list) - 1
        if len((self.my_list[self.index_last_stack])) >= 4:
            self.my_list.append([el])
        elif len((self.my_list[self.index_last_stack])) < 4:
            self.my_list[self.index_last_stack].append(el)

    # удаление последнего элемента
    def pop_out(self):
        self.index_last_stack = len(self.my_list) - 1
        self.index_last_el_stack = len((self.my_list[self.index_last_stack])) - 1
        if self.index_last_el_stack == 0:
            self.my_list.pop()
        else:
            self.my_list[self.index_last_stack].pop(self.index_last_el_stack)

    # Запрос общего вида
    def get_view(self):
        return f'func get_view = {self.my_list}.'

    # Общее кол-во элементов
    def get_val(self):
        return f'func get_val = {self.my_list[len(self.my_list) - 1][0]}.'

    # Кол-во стопок
    def stack_size(self):
        return f'func stack_size = {len(self.my_list)}.'


if __name__ == '__main__':
    stack_class = StackClass()
    stack_class.push_in(1)
    stack_class.push_in(2)
    stack_class.push_in(3)
    stack_class.push_in(4)
    stack_class.push_in(5)
    print(stack_class.get_val())
    print(stack_class.stack_size())
    stack_class.push_in(6)
    stack_class.push_in(7)
    stack_class.push_in(8)
    print(stack_class.get_view())
    stack_class.pop_out()
    print(stack_class.get_view())
    print(stack_class.is_empty())
    print(stack_class.get_view())

# Думаю этого должно быть вполне достаточно для выполнения задания. Хотя можно добавить так же добавление стопок, а не
# элементов (по одному) отдельно.
