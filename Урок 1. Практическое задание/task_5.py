"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

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
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""


class StackClass:
    def __init__(self):
        self.elems = [[]]
        self.max_size = 6

    def is_empty(self):
        return self.get_stack() == []

    def push_in(self, el):
        if self.stack_size() == self.max_size:
            self.elems.append([])
        self.get_stack().append(el)

    def pop_out(self):
        if self.stack_size() == 0:
            self.elems.pop()
        return self.get_stack().pop()

    def get_val(self):
        return self.get_stack()[self.stack_size() - 1]

    def stack_size(self):
        return len(self.get_stack())

    def stacks_count(self):
        return len(self.elems)

    def get_stack(self):
        return self.elems[len(self.elems) - 1]


SC_OBJ = StackClass()

print(SC_OBJ.is_empty())  # -> стек пустой

# наполняем стек
SC_OBJ.push_in('plate_01')
SC_OBJ.push_in('plate_02')
SC_OBJ.push_in('plate_03')
SC_OBJ.push_in('plate_04')
SC_OBJ.push_in('plate_05')
SC_OBJ.push_in('plate_06')
SC_OBJ.push_in('plate_07')
SC_OBJ.push_in('plate_08')
SC_OBJ.push_in('plate_09')
SC_OBJ.push_in('plate_10')


print('Верхняя тарелка: ', SC_OBJ.get_val())

print(f'Размер последней стопки: {SC_OBJ.stack_size()}')

# кладем еще одну тарелку в стопку
SC_OBJ.push_in('plate_11')

# убираем последнюю тарелку со стопки
print(SC_OBJ.pop_out())  # -> 'plate_11'

# убираем еще одну тарелку
print(SC_OBJ.pop_out())  # -> 'plate_10'

print(f'Размер последней стопки {SC_OBJ.stack_size()}')

print(f'Последняя стопка {SC_OBJ.get_stack()}')

print(f'количество стопок с тарелками {SC_OBJ.stacks_count()}')
