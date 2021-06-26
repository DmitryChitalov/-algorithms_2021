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
Отдельные стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class PlatesStack:
    def __init__(self):
        self.platesList = [[]]
        self.__maxPlates__ = 10

    def __str__(self):
        return str(self.platesList)

    def is_limit(self):
        return len(self.platesList[-1]) == self.__maxPlates__

    def push(self, value):
        # Проверяем, что в текущую стопку еще можно добавить значения, иначе добавляем новую
        if self.is_limit():
            self.platesList.append([])

        self.platesList[-1].append(value)

    def get(self):
        if len(self.platesList[-1]) == 0:
            returned_value = None
        else:
            returned_value = self.platesList[-1][-1]

        return returned_value

    def pop(self):
        if len(self.platesList[-1]) == 0 and len(self.platesList) > 1:
            self.platesList.pop()

        if len(self.platesList[-1]) != 0:
            self.platesList[-1].pop()

            if len(self.platesList[-1]) == 0 and len(self.platesList) > 1:
                self.platesList.pop()


current_plates_stack = PlatesStack()

current_plates_stack.push(1)
current_plates_stack.push(2)
current_plates_stack.push(3)
current_plates_stack.push(4)
current_plates_stack.push(5)
current_plates_stack.push(6)
current_plates_stack.push(7)
current_plates_stack.push(8)
current_plates_stack.push(9)
current_plates_stack.push(10)
current_plates_stack.push(11)
current_plates_stack.push(12)
current_plates_stack.push(13)
print(current_plates_stack)

current_plates_stack.pop()
current_plates_stack.pop()
current_plates_stack.pop()
current_plates_stack.pop()
print(current_plates_stack)

print(current_plates_stack.get())
