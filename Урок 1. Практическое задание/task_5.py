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



class PlatesStackClass:
    def __init__(self, size):
        self.elems = []
        self.size = size

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка, если элемент равен размеру (size),
        создаём новую стопку"""
        if self.elems[len(self.elems)-1] < self.size:
            self.elems[len(self.elems)-1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)


    def pop_out(self):
        """Удаляем стопку, если она пустая"""
        var = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return var

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        """Общее число тарелок"""
        elem_sum = 0
        for stack in self.elems:
            elem_sum += len(stack)
        return elem_sum


pl = PlatesStackClass(2)
pl.push_in('Pl1')
pl.push_in('Pl2')
pl.push_in('Pl3')
pl.push_in('Pl4')

print(pl)
print(pl.pop_out())
print(pl.get_val())
print(pl.stack_size())
print(pl)