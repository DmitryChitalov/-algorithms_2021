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


class StackPlates:
    # список стопок
    list_plate_stacks = []

    def __init__(self):
        self.plates = []

    # кол-во стопок
    @staticmethod
    def len_plate_stacks():
        return len(StackPlates.list_plate_stacks)

    # метод копирования стопки в список
    def add_stack_to_list(self):
        stack = self.plates.copy()
        return StackPlates.list_plate_stacks.append(stack)

        # нахождение высоты/длинны/кол-ва(одна суть) тарелок в стопке
    def size(self):
        return len(self.plates)

    # добавление тарелки в стопку
    def add_plate(self, plate):
        if self.size() <= 7:  # Думаю при семи стопка не свалится
            return self.plates.append(plate)
        else:
            self.add_stack_to_list()
            self.plates.clear()
            return self.add_plate(plate)


# Проверим работу
if __name__ == '__main__':

    plates_stack = StackPlates()
    plates_stack.add_plate('Фарфоровая1')
    plates_stack.add_plate('Фарворовая2')
    plates_stack.add_plate('Глиняная1')
    plates_stack.add_plate('Стеклянная1')
    plates_stack.add_plate('Стеклянная2')
    plates_stack.add_plate('Стеклянная3')
    plates_stack.add_plate('Фарфоровая3')
    plates_stack.add_plate('Фарфоровая4')
    plates_stack.add_plate('Глиняная2')
    # Список заполненных стопок
    print(list(StackPlates.list_plate_stacks))
    # Последняя стопка
    print(plates_stack.plates)
    # Кол-во полных стопок
    print(StackPlates.len_plate_stacks())
