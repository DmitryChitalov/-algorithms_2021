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

"""Пример создания стека через ООП"""


class StackClass:
    stacks = []
    __max_elem_count = 3

    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        stack = self.get_last_stack()
        if stack is None:
            stack = StackClass()
            StackClass.stacks.append(stack)
        elif self.is_full(stack):
            stack = StackClass()
            StackClass.stacks.append(stack)
        stack.elems.append(el)

    def pop_out(self):
        stack = self.get_last_stack()
        if stack is None:
            raise TypeError
        last_elem = stack.elems.pop()
        if len(stack.elems) == 0:
            StackClass.stacks.remove(stack)
        return last_elem

    def get_val(self):
        stack = self.get_last_stack()
        return stack.elems[len(self.elems) - 1]

    def stacks_count(self):
        return len(StackClass.stacks)

    def get_last_stack(self):
        if len(StackClass.stacks) == 0:
            return None
        return StackClass.stacks[-1]

    def is_full(self, stack):
        return len(stack.elems) == self.__max_elem_count


if __name__ == '__main__':

    SC_OBJ = StackClass()
    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(52)
    SC_OBJ.push_in(1)
    SC_OBJ.push_in(1)
    print(f'count={SC_OBJ.stacks_count()}')

    # посмотрим что хранится в стеках
    for s in SC_OBJ.stacks:
        print(s.elems)

    # поудаляем элементы и поглядим что остается
    print(SC_OBJ.pop_out())
    print(f'count={SC_OBJ.stacks_count()}')
    print(SC_OBJ.pop_out())
    for s in SC_OBJ.stacks:
        print(s.elems)
