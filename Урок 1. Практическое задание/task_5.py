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
class PlateStackClass:
    plates_height = 6 #Высота стопки тарелок по умолчанию

    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def get_stack_num(self):
        return len(self.elems)

    def free_cells (self):
        if self.is_empty():
            return 0
        else:
            return 6 - len(self.elems[len(self.elems)-1])


    def push(self, num_plates=1):
        """Добавляет в стопку num_plates тарелок"""
        while num_plates > 0:
            if self.free_cells() > 0:
                self.elems[len(self.elems)-1].append(1)
            else:
                self.elems.append([])
                self.elems[len(self.elems) - 1].append(1)
            num_plates -= 1

    def pop(self):
        if self.is_empty():
            return None
        if len(self.elems[len(self.elems)-1]) == 0:
            self.elems.pop()
            self.pop()
        else:
            return self.elems[len(self.elems)-1].pop()

plates = PlateStackClass()
print(plates.free_cells())
plates.push(num_plates=13)
plates.push()
plates.pop()
plates.pop()
plates.pop()
print(plates.get_stack_num())
