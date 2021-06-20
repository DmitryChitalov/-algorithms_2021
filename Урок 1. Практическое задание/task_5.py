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
    def __init__(self, n):
        self.n = n
        self.plates = [[]]

    # просмотр текущих стопок тарелок
    def __str__(self):
        return self.plates

    # добавление тарелки в стопки
    def add_plate(self, pl):
        st = len(self.plates)-1
        if len(self.plates[st]) < self.n:
            self.plates[st].append(pl)
        else:
            self.plates.append([])
            self.plates[st+1].append(pl)
        return self.plates

    # убираем тарелку из стопки
    def del_plate(self):
        st = len(self.plates) - 1
        if len(self.plates[st]) != 0:
            self.plates[st].pop()
            if len(self.plates[st]) == 0:
                self.plates.pop()
        return self.plates


SP_OBJ = StackPlates(3)

SP_OBJ.del_plate()
print(SP_OBJ.__str__())

SP_OBJ.add_plate('plate_1')
SP_OBJ.add_plate('plate_2')
SP_OBJ.add_plate('plate_3')
SP_OBJ.add_plate('plate_4')
SP_OBJ.add_plate('plate_5')
SP_OBJ.add_plate('plate_6')
SP_OBJ.add_plate('plate_7')
print(SP_OBJ.__str__())

SP_OBJ.del_plate()
print(SP_OBJ.__str__())

SP_OBJ.del_plate()
print(SP_OBJ.__str__())

SP_OBJ.del_plate()
print(SP_OBJ.__str__())