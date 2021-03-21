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
        self.max_size_of_bank = 2
        self.active_bank = 0
        self.current_position_in_bank = 0
    
    def add_new_bank(self):
        self.elems.append([])
        self.active_bank+=1
        self.current_position_in_bank = 0
    
    def remove_empty_bank(self):
        self.elems.pop()
        self.active_bank -= 1
    
    def push_in(self, el):
        if self.current_position_in_bank == self.max_size_of_bank:
            self.add_new_bank()
        self.elems[self.active_bank].append(el)
        self.current_position_in_bank+=1
        
        
    def pop_out(self):
        self.element_to_return = self.elems[self.active_bank].pop()
        self.current_position_in_bank-=1
        if self.current_position_in_bank == 0:
            self.remove_empty_bank()
            self.current_position_in_bank = self.max_size_of_bank
        return self.element_to_return
        
    def dump(self):
        return self.elems
    
new_stack = StackClass()
new_stack.push_in(5)
new_stack.push_in(4)
new_stack.push_in(11)
new_stack.push_in(58)
new_stack.push_in(545)
print(new_stack.dump())
print(new_stack.pop_out())
print(new_stack.dump())
print(new_stack.pop_out())
print(new_stack.dump())
print(new_stack.pop_out())
print(new_stack.dump())
new_stack.push_in(231)
print(new_stack.dump())
print(new_stack.pop_out())
print(new_stack.dump())