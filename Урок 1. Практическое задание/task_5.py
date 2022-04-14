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
    def __init__(self, max_size):
        self.elements = [[]]
        self.max_size = max_size

    def is_empty(self):
        return self.elements == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elements[len(self.elements) - 1]) < self.max_size:
            self.elements[len(self.elements) - 1].append(el)
        else:
            self.elements.append([])
            self.elements[len(self.elements) - 1].append(el)

    def pop_out(self):
        plate = self.elements[len(self.elements) - 1].pop()
        if len(self.elements[len(self.elements) - 1]) == 0:
            self.elements.pop()
        return f'Удалена тарелка {plate}'

    def get_val(self):
        return self.elements[len(self.elements) - 1][len(self.elements[len(self.elements) - 1]) - 1]

    def stack_size(self):
        sum_plates = (len(self.elements) - 1) * self.max_size + len(self.elements[len(self.elements) - 1])
        sum_stacks = len(self.elements)
        return f'Сумма стопок в стеке = {sum_stacks},\nСумма всех тарелок = {sum_plates}'


plates = StackClass(3)
print(plates.is_empty())
plates.push_in(1)
plates.push_in(2)
plates.push_in(3)
plates.push_in(4)
plates.push_in(5)
plates.push_in(6)
plates.push_in(7)
plates.push_in(8)
plates.push_in(9)
plates.push_in(10)
plates.push_in(11)
plates.push_in(12)
print(plates)
print(plates.get_val())
print(plates.stack_size())
print(plates.pop_out())
print(plates.stack_size())
print(plates.pop_out())
print(plates.pop_out())
print(plates.pop_out())
print(plates.stack_size())
print(plates.get_val())
print(plates.is_empty())