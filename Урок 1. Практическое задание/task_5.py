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


# Класс будет обслуживать стопку тарелок. По дефолту в стопке может быть 10 тареклок и стопка на старте - пуста.
class PlateTower:
    def __init__(self):
        self.max_h = 10
        self.count = 0

    def add_plate(self):
        if self.space_left():
            self.count = self.count + 1
            return True
        else:
            return False

    def remove_plate(self):
        if self.count > 0:
            self.count = self.count - 1

    @property
    def plate_count(self):
        return self.count

    def space_left(self):
        if self.max_h - self.count > 0:
            return True
        else:
            return False


# А это наш стол. На нем стоят стопки, куда мы кладем тарелки.
class Table:
    def __init__(self):
        self.place = []
        self.place.append(PlateTower())

    @property
    def get_last_pos(self):
        if len(self.place) == 0:
            return None
        else:
            return self.place[len(self.place) - 1]

    def add_tower(self):
        self.place.append(PlateTower())

    def rem_plates(self, count):
        for x in range(count):
            if self.get_last_pos != None:
                self.get_last_pos.remove_plate()
                if self.get_last_pos.plate_count == 0:
                    self.place.pop()

    def add_plates(self, count):
        if self.get_last_pos is None:
            self.add_tower()
        for x in range(count):
            if self.get_last_pos.space_left():
                self.get_last_pos.add_plate()
            else:
                self.add_tower()
                self.get_last_pos.add_plate()

    def __str__(self):
        f = ''
        if self.get_last_pos is None:
            f = 'Стол пустой.\n'
        else:
            for x in range(len(self.place)):
                f = f + (f'Стопка: {x + 1} содержит тарелок {self.place[x].plate_count} шт.\n')
        return f


tt = Table()
tt.add_plates(12)
tt.add_plates(14)
print(tt)
tt.rem_plates(122)
print(tt)
tt.add_plates(11)
print(tt)
