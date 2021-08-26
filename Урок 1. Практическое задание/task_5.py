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


class PlateStack:
    def __init__(self, maximum):
        self.el = []
        self.maximum = maximum

    def __str__(self):
        return str(self.el)

    def push_in(self, plate):
        """Добавляем тарелки в стопки. Если стопка наполняется - добавляем новую стопку"""
        if len(self.el) == 0:
            self.el.append([plate])
        elif len(self.el[len(self.el) - 1]) < self.maximum:
            self.el[len(self.el) - 1].append(plate)
        else:
            self.el.append([])
            self.el[len(self.el) - 1].append(plate)

    def pop_out(self):
        """Удаляем верхний элемент стопки"""
        self.el[len(self.el) - 1].pop()
        if len(self.el[len(self.el) - 1]) == 0:
            self.el.pop()

    def last_plate(self):
        """Получаем значение верхнего элемента стопки"""
        return f"Последняя тарелка № {self.el[len(self.el) - 1][-1]}"

    def stack_height(self):
        """Получаем высоту крайней стопки"""
        return f"Высота стопки - {len(self.el[len(self.el) - 1])}"

    def stacks_count(self):
        """Получаем количество стопок"""
        return f"Количество стопок - {len(self.el)}"


plates = PlateStack(5)
print(type(plates))

for i in range(1, 7):
    plates.push_in(i)

print(plates)
print(plates.last_plate())
print(plates.stack_height())
print(plates.stacks_count())
plates.pop_out()
print(plates)
print(plates.last_plate())
print(plates.stack_height())
print(plates.stacks_count())
