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

# Данный класс вмещает в себя 10 тарелок. Если тарелок больше 10, то создается новая стопка.
# Вымытые тарелки удаляются, начиная с последней стопки. Когда стопка опустевает (кроме первой стопки), она удаляется.

class PlateStack:
    total_stacks = []

    def __init__(self):
        PlateStack.total_stacks.append(self)
        self.plates = []

    def is_full(self):
        return len(self.plates) == 10

    def stacks_number(self):
        return len(PlateStack.total_stacks)

    def push_in(self, el):
        currents_stack = PlateStack.total_stacks[-1]
        if not currents_stack.is_full():
            currents_stack.plates.append(el)
        else:
            print('добавляем стопку')
            new_stack = PlateStack()
            new_stack.push_in(el)

    def wash(self):
        current_stack = PlateStack.total_stacks[-1]
        if not current_stack.plates:
            print('Вся посуда вымыта')
        else:
            washed_plate = current_stack.plates.pop()
            if not current_stack.plates and len(PlateStack.total_stacks) > 1:
                print('одна стопка вымыта')
                PlateStack.total_stacks.pop()
            return washed_plate


# Добавим 23 тарелки, создастся 3 стопки, потом попытаемся вымыть 30:
plate_stack = PlateStack()
for plate in [f'тарелка_{m}' for m in range (1, 24)]:
    plate_stack.push_in(plate)
print(len(PlateStack.total_stacks))

for i in range(30):
    print(plate_stack.wash())
print(len(PlateStack.total_stacks))
