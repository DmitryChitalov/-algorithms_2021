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


class StackOfPlatesClass:

    def __init__(self, max_quantity):
        self.unit = [[]]
        self.max_quantity = max_quantity  # Max количество тарелок в стопке

    def __str__(self):
        if self.unit == [[]]:
            return 'Нет ни одной тарелки.'
        return str(self.unit)

    def is_empty(self):
        self.unit = [[]]
        return 'Тарелок больше нет'

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.unit[len(self.unit) - 1]) < self.max_quantity:
            self.unit[len(self.unit) - 1].append(el)
        else:
            self.unit.append([])
            self.unit[len(self.unit) - 1].append(el)

    def pop_out(self):
        result = self.unit[len(self.unit) - 1].pop()
        if len(self.unit[len(self.unit) - 1]) == 0:
            self.unit.pop()
        return f'Из стопки {self.stack_count()} забрали {result}.'

    def get_val(self):
        return self.unit[len(self.unit) - 1]  # Содержимое 'активной' стопки

    def stack_size(self):
        elem_sum = 0
        for stack in self.unit:
            elem_sum += len(stack)
        return f'Всего тарелок: {elem_sum}'

    def stack_count(self):
        return len(self.unit)


plates = StackOfPlatesClass(5)
print(plates)
plates.push_in('plate_01')
plates.push_in('plate_02')
plates.push_in('plate_03')
plates.push_in('plate_04')
plates.push_in('plate_05')
plates.push_in('plate_06')
plates.push_in('plate_07')
plates.push_in('plate_08')
plates.push_in('plate_09')
plates.push_in('plate_10')
plates.push_in('plate_11')
plates.push_in('plate_12')
plates.push_in('plate_13')
print(plates)
print(plates.pop_out())
print(plates.pop_out())
print(plates.pop_out())
print(plates.pop_out())
print(plates.get_val())
print(plates.stack_size())
print(f'Всего стопок: {plates.stack_count()}')
print(plates)
print(plates.is_empty())
print(plates)
