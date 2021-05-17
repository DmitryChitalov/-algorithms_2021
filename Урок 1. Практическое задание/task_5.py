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


def stack_of_plates(stack_1):
    bunch_1 = StackClass()
    bunch_2 = StackClass()
    bunch_3 = StackClass()

    for i in range(len(stack_1)):
        if bunch_1.stack_size() < 5:
            bunch_1.push_in(stack_1[i])
        elif bunch_2.stack_size() < 5:
            bunch_2.push_in(stack_1[i])
        elif bunch_3.stack_size() < 5:
            bunch_3.push_in(stack_1[i])

    bunch_1_string = ""
    while not bunch_1.is_empty():
        bunch_1_string = bunch_1_string + str(bunch_1.pop_out()) + " "

    bunch_2_string = ""
    while not bunch_2.is_empty():
        bunch_2_string = bunch_2_string + str(bunch_2.pop_out()) + " "

    bunch_3_string = ""
    while not bunch_3.is_empty():
        bunch_3_string = bunch_3_string + str(bunch_3.pop_out()) + " "

    print(bunch_1_string)
    print(bunch_2_string)
    print(bunch_3_string)


plates = ["Синяя", "Красная", "Белая", "Желтая", "Зеленая", "Оранжевая", "Фиолетовая", "Голубая", "Синяя",
          "Красная", "Белая", "Желтая", "Зеленая", "Оранжевая", "Фиолетовая", "Голубая"]
stack_of_plates(plates)