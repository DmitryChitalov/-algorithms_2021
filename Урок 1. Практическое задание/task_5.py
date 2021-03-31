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
        self.max_size = 4

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


# получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
print('first plate: ', SC_OBJ.get_val())  # -> plate 11

# получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
print(SC_OBJ.get_val())  # -> plate 101

# узнаем размер стека
print(f'stack size: {SC_OBJ.stack_size()}')  # -> 3

print(SC_OBJ.is_empty())  # -> стек уже непустой

# кладем еще один элемент в стек
SC_OBJ.push_in('plate_11')

# убираем элемент с вершины стека и возвращаем его значение
print(SC_OBJ.pop_out())  # -> 'plate_11'

# снова убираем элемент с вершины стека и возвращаем его значение
print(SC_OBJ.pop_out())  # -> 'plate_10'

# вновь узнаем размер стека
print(SC_OBJ.stack_size())  # -> 3

print(SC_OBJ.get_stack())