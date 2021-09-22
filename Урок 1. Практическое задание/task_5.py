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
from threading import stack_size


class StackManager:
    def __init__(self):
        self.stack_lst = []
        self.stack_lst.append(StackData())

    def add_element(self, elm):
        last_stack_data = self.stack_lst[len(self.stack_lst) - 1]
        if last_stack_data.stack_size() == 5:
            new_stack_data = StackData()
            self.stack_lst.append(new_stack_data)
            new_stack_data.add_element(elm)
        else:
            last_stack_data.add_element(elm)

    def pop_element(self):
        last_stack_data = self.stack_lst[len(self.stack_lst) - 1]
        if last_stack_data.stack_size() == 0:
            return f'Stack is empty'
        result = last_stack_data.pop_element()
        if last_stack_data.stack_size() == 0:
            if len(self.stack_lst) > 1:
                self.stack_lst.pop()
        return result


class StackData:
    def __init__(self):
        self.elements = []

    def add_element(self, elm):
        self.elements.append(elm)

    def pop_element(self):
        return self.elements.pop()

    def ended_elements(self):
        return self.elements[len(self.elements) - 1]

    def stack_size(self):
        return len(self.elements)


stack_1 = StackManager()
stack_1.add_element(1)
stack_1.add_element(2)
stack_1.add_element(3)
stack_1.add_element(4)
stack_1.add_element(5)
stack_1.add_element(6)


print(stack_1.pop_element())
print(stack_1.pop_element())
print(stack_1.pop_element())
print(stack_1.pop_element())
print(stack_1.pop_element())
print(stack_1.pop_element())
print(stack_1.pop_element())

