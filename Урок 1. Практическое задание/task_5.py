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


def new_stack():
    name_list = ['second_stack', 'third_stack', 'fourth_stack']
    for name in name_list:
        globals()[name] = StackOfPlates()


class StackOfPlates:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def is_full(self):
        if len(self.elems) == 5:
            new_stack()
            return True
        else:
            return False


first_stack = StackOfPlates()

print(first_stack.is_empty())

first_stack.push_in('plate_one')
first_stack.push_in('plate_two')
first_stack.push_in('plate_three')
first_stack.push_in('plate_four')

print(first_stack.get_val())

print(first_stack.stack_size())

print(first_stack.is_empty())

first_stack.push_in('plate_five')

print(first_stack.pop_out())


print(first_stack.pop_out())

print(first_stack.stack_size())

print(first_stack.is_full())

first_stack.push_in('plate_four')
first_stack.push_in('plate_five')

print(first_stack.is_full())

print(first_stack.elems)

first_stack.push_in('plate_six')

print(first_stack.elems)

print(second_stack.elems)
