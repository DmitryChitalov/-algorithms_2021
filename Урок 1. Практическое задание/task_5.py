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
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]


    def stack_size(self):
        return len(self.elems)

class Shot(StackClass):
    def __init__(self, max_size = 3):
        super ().__init__ ()
        self.max_size_stack = max_size

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == []

    def _pucking(self, element):
        self.elems[self.stack_size() - 1].append(element)

    def _stack_size_shot(self):
        return len(self.elems[self.stack_size() - 1])

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if self.is_empty(): # если первый элемент, то добавляем элемент стопка и заносим значение
            self.elems.append ([])
            self._pucking(el)
        elif self._stack_size_shot() < self.max_size_stack:
                self._pucking(el)
        else:
            self.elems.append([]) # Если есть переполнение стопки то формируем новую стопку
            self._pucking(el)

    def pop_out(self):
        value_out = self.elems[self.stack_size() - 1].pop()
        if self._stack_size_shot() == 0:
            self.elems.pop()
        return value_out

    def get_val(self): # Вернуть значение из определенной стопки без удаления
        return self.elems[self.stack_size() - 1][self._stack_size_shot() - 1]



if __name__ == '__main__':
    my_list = [10, 'code', False,
               11, 'code+', False,
               12, 'code++', False,
               13, 'code+++', False,
               14, 'code++++', False,
               15, 'code+++++', False,
               16, 'code++++++', False,
               17, 'code+++++++', False,
               18, 'code++++++++'
               ]

    shot_one = Shot(3)
    for value in my_list:
        shot_one.push_in(value)

    print(shot_one.elems)
    print(shot_one.pop_out())
    print (shot_one.pop_out ())
    print (shot_one.pop_out ())
    print (shot_one.pop_out ())
    print (shot_one.pop_out ())
    print (shot_one.pop_out ())

