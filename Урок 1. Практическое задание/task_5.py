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
    def __init__(self, stack_size=0):
        """ Если нужно разделение стека по длине ([[], [], [], [],....]),
        то передаём размер.
        """
        self.elems = []
        self.max_stack_size = stack_size

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в начале списка"""
        if len(self.elems) > 0:
            if self.max_stack_size > 0:
                if len(self.elems[0]) < self.max_stack_size:
                    self.elems[0].insert(0, el)
                else:
                    self.elems.insert(0, [el])
            else:
                self.elems.insert(0, el)
        else:
            if self.max_stack_size > 0:
                self.elems.insert(0, [el])
            else:
                self.elems.insert(0, el)

    def pop_out(self):
        if self.max_stack_size > 0:
            if len(self.elems[0]) > 0:
                element_pop = self.elems[0].pop(0)

                if len(self.elems[0]) == 0:
                    self.elems.pop(0)

                return element_pop
        else:
            return self.elems.pop(0)

    def get_val(self):
        if self.max_stack_size > 0:
            if len(self.elems[0]) > 0:
                return self.elems[0][0]
        else:
            return self.elems[0]

    def stack_size(self):
        if self.max_stack_size > 0:
            st_size = int()
            for x in self.elems:
                st_size += len(x)
            return st_size
        else:
            return len(self.elems)


# Если я правильно понял задание.
# Будем разделять стек по 10 элементов.
SC_OBJ = StackClass(10)

# Наполняем стек.
for x in range(101)[1::]:
    SC_OBJ.push_in(str(x) + "_plate")

print(SC_OBJ.elems)
print(SC_OBJ.stack_size())
print(SC_OBJ.get_val())
print()

# Удалим 15 элементов.
for _ in range(16)[1::]:
    print(SC_OBJ.pop_out())

print(SC_OBJ.elems)
print(SC_OBJ.stack_size())
