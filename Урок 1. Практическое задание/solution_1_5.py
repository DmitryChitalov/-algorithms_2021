
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
        self.stack = []
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в начале списка"""
        self.elems.insert(0, el)
        if len(self.elems) == 10:               # Отслеживаем достижение высоты стека self.elems
            self.stack.append(self.elems)       # добавляем список с элементами в список self.stack
            self.elems.clear()                  # очищаем список self.elems

    def pop_out(self):
        return self.elems.pop(0)

    def get_val(self):
        return self.elems[0]

    def elem_size(self):
        return len(self.elems)

    def stack_size(self):
        return len(self.stack)


SC_OBJ = StackClass()

print(SC_OBJ.is_empty())  # -> стек пустой

# наполняем стек
SC_OBJ.push_in(10)
SC_OBJ.push_in('code')
SC_OBJ.push_in(False)
SC_OBJ.push_in(5.1)
SC_OBJ.push_in(5.2)
SC_OBJ.push_in(5.3)
SC_OBJ.push_in(5.4)
SC_OBJ.push_in(5.5)
SC_OBJ.push_in(5.6)
SC_OBJ.push_in(5.7)
SC_OBJ.push_in(5.8)
SC_OBJ.push_in(5.9)
SC_OBJ.push_in(6.0)
SC_OBJ.push_in(6.1)
SC_OBJ.push_in(6.2)
SC_OBJ.push_in(6.3)
SC_OBJ.push_in(6.4)
SC_OBJ.push_in(6.5)
SC_OBJ.push_in(6.6)
SC_OBJ.push_in(6.7)
SC_OBJ.push_in(6.8)
SC_OBJ.push_in(6.9)
SC_OBJ.push_in(7.0)
SC_OBJ.push_in(7.1)

print(SC_OBJ.elem_size())
print(SC_OBJ.stack_size())
