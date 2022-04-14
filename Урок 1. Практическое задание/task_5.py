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
        self.main_stack = []
        self.elems = []

    def is_empty(self):
        return self.main_stack == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в начале списка"""
        if len(self.elems) >= 5:
            self.main_stack.insert(0, self.elems)
            self.elems = []
            self.elems.insert(0, el)
        else:
            self.elems.insert(0, el)

    def pop_out(self):
        if len(self.elems) == 0:
            self.elems = self.main_stack[0]
            self.main_stack.pop(0)
            return self.elems.pop(0)
        else:
            return self.elems.pop(0)

    def get_val(self):
        return self.elems[0]

    def stack_size(self):
        return len(self.elems)

    def main_stack_size(self):
        return len(self.main_stack)

    def show_stack(self):
        return self.elems

    def show_main_stack(self):
        return self.main_stack


SC_OBJ = StackClass()

print(SC_OBJ.is_empty())

SC_OBJ.push_in(10)
SC_OBJ.push_in('code')
SC_OBJ.push_in(False)
SC_OBJ.push_in(5.5)
SC_OBJ.push_in(78)
SC_OBJ.push_in(95)
SC_OBJ.push_in(95)

print(SC_OBJ.get_val())
print(SC_OBJ.stack_size())
print(SC_OBJ.main_stack_size())

SC_OBJ.pop_out()
SC_OBJ.pop_out()
SC_OBJ.pop_out()
SC_OBJ.pop_out()

print(SC_OBJ.stack_size())
print(SC_OBJ.main_stack_size())
print(SC_OBJ.get_val())

print(SC_OBJ.show_stack())

SC_OBJ.push_in(5.5)
SC_OBJ.push_in(78)
SC_OBJ.push_in(95)
SC_OBJ.push_in(95)


print(SC_OBJ.show_main_stack())