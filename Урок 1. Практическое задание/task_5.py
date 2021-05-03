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
    def __init__(self, stack_size):
        self.elems = []
        self.stack_size = stack_size

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, pl):
        """Помещаем тарелки в стопки. Если размер стопки становится равным заданному,
        то создаем новую стопку. В теории должно быть так, но получаю на 48 строку
        ошибку 'list index out of range'. Не могу сообразить  """
        if self.elems[(len(self.elems) - 1) < self.stack_size]:
            self.elems[len(self.elems) - 1].append(pl)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(pl)

    def pop_out(self):
        """
        удаление элементов с конца списка, если стек пустой, то он удаляется
        """
        self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return self.elems[len(self.elems) - 1].pop()

    def total_stacks(self):
        """
        количество стоек с тарелками
        """
        return self.elems[len(self.elems) - 1]

    def all_size(self):
        """
        всего тарелок
        """
        count_el = 0
        for stack in self.elems:
            count_el += len(stack)
        return count_el


if __name__ == '__main__':
    sp = StackClass(2)
    sp.push_in('plate_1')
    sp.push_in('plate_2')
    sp.push_in('plate_3')
    sp.push_in('plate_4')
    sp.push_in('plate_5')
    sp.push_in('plate_6')
    sp.push_in('plate_7')
    print(sp)
    print(sp.pop_out())
    print(sp.total_stacks())
    print(sp.all_size())
