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


class PlatesStack:
    def __init__(self):
        self.elems = []
        self.stack_size = 10

    def is_empty(self):
        return self.elems == []

    def push(self, el):
        self.elems.append(el)

    def pop(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def get_stack_size(self):
        return len(self.elems)

    def is_full(self):
        if len(self.elems) >= self.stack_size:
            return True

    def get_all_elems(self):
        return self.elems

    def get_max_size(self):
        return self.stack_size


if __name__ == '__main__':
    plates_count = 45


    def add_plates():
        plates = []
        plates_stack = PlatesStack()
        for i in range(1, plates_count + 1):
            plates_stack.push(i)
            if plates_stack.is_full():
                plates.append(plates_stack.get_all_elems())
                plates_stack = PlatesStack()

        plates.append(plates_stack.get_all_elems())

        return plates


    print(add_plates())
