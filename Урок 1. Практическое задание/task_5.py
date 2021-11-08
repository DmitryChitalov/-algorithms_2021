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


class PlatesClass:
    def __init__(self, max_size):
        self.elems = []
        self.max_size = max_size

    def is_empty(self):
        return self.elems[len(self.elems) - 1] == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if not self.elems:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)
        elif len(self.elems[len(self.elems) - 1]) == self.max_size:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        last_elem = self.elems[len(self.elems) - 1].pop()
        if self.is_empty():
            self.elems.pop()
        return last_elem

    def get_val(self):
        return self.elems[len(self.elems) - 1][-1]

    def stack_size(self):
        counter = 0
        for stack in self.elems:
            counter += len(stack)
        return counter

    def stack_counter(self):  # счетчик стеков
        return len(self.elems)

    def get_all(self):  # посмотреть все стеки
        return self.elems


plates = PlatesClass(5)
plates.push_in('1plate')
plates.push_in('2plate')
plates.push_in('3plate')
plates.push_in('4plate')
plates.push_in('5plate')
plates.push_in('6plate')
plates.push_in('7plate')
plates.push_in('8plate')
print(plates.get_val())
print(plates.stack_size())
print(plates.stack_counter())
print(plates.get_all())
print(plates.pop_out())
print(plates.pop_out())
print(plates.get_all())
print(plates.pop_out())
print(plates.stack_counter())
print(plates.is_empty())
print(plates.get_val())
print(plates.get_all())
print(plates.stack_size())
print(plates.pop_out())
