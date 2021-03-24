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

# Максимальное значение для стопки равняется 3, при его заполнении создается новый "бланк" (list), который заполняется
# до тех пор, пока не перерастет значение в 3 элемента. Долго не могла понять как реализовать это, но полистав GitHub и
# прочие статьи все-таки дошло.


class StackClass:

    def __init__(self):

        self.elements = [[]]
        self.max_size = 3
        self.active_bank = 0
        self.position_in_bank = 0

    def add_new_bank(self):

        self.elements.append([])
        self.active_bank += 1
        self.position_in_bank = 0

    def remove_null_bank(self):

        self.elements.pop()
        self.active_bank -= 1

    def push_in(self, el):

        if self.position_in_bank == self.max_size:
            self.add_new_bank()
        self.elements[self.active_bank].append(el)
        self.position_in_bank += 1

    def pop_out(self):

        self.return_element = self.elements[self.active_bank].pop()
        self.position_in_bank -= 1

        if self.position_in_bank == 0:
            self.remove_null_bank()
            self.position_in_bank = self.max_size
        return self.return_element

    def dump(self):
        return self.elements


new_stack = StackClass()

new_stack.push_in(10)

new_stack.push_in(34)

new_stack.push_in(11)

new_stack.push_in(47)

new_stack.push_in(1)

new_stack.push_in(98)

new_stack.push_in(479)

print(new_stack.dump())

print(new_stack.pop_out())

print(new_stack.dump())

print(new_stack.pop_out())

new_stack.push_in(15)

print(new_stack.dump())

print(new_stack.pop_out())

print(new_stack.dump())

new_stack.push_in(29)

print(new_stack.dump())

print(new_stack.pop_out())

print(new_stack.dump())

new_stack.push_in(98)

print(new_stack.dump())
