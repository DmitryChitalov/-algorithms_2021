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
import random


class StackClass:
    def __init__(self):
        self.elem = [[]]
        self.size = 10

    def is_empty(self):
        return self.elem == [[]]

    def push_in(self, el):
        if len(self.elem[len(self.elem)-1]) < self.size:
            self.elem[len(self.elem)-1].append(el)
        else:
            self.elem.append([])
            StackClass.push_in(self, el)

    def pop_out(self):
        if len(StackClass.stack_val(self)) != 0:
            last_elem = self.elem[len(self.elem)-1].pop()
            if len(self.elem[len(self.elem)-1]) == 0:
                self.elem.pop()
            return last_elem
        else:
            return None

    def stack_val(self):
        stacks = []
        for el in self.elem:
            stacks.append(el)
        return stacks

    def stack_size(self):
        return len(StackClass.stack_val(self))


SC_OBJ = StackClass()

print(SC_OBJ.is_empty())  # -> стек пустой

# наполняем стек
for i in random.sample(range(1, 100), 20):
    SC_OBJ.push_in(i)
# получаем все элементы из стэка
print(SC_OBJ.stack_val())

# узнаем размер стека
print(SC_OBJ.stack_size())

print(SC_OBJ.is_empty())  # -> стек уже непустой

# кладем еще один элемент в стек
SC_OBJ.push_in(4)
print(SC_OBJ.stack_val())
print(SC_OBJ.stack_size())
# убираем элемент с вершины стека и возвращаем его значение
print(SC_OBJ.pop_out())

# снова убираем элемент с вершины стека и возвращаем его значение
print(SC_OBJ.pop_out())

# вновь узнаем размер стека
print(SC_OBJ.stack_size())
