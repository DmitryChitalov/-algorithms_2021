"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

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
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""


class PlatesStack:
    """
    Класс реализует стэк "стопка тарелок"
    """

    def __init__(self):
        """инициализация - создание пустой стопки тарелок """
        self.plates = []

    def is_empty(self):
        """проверка на пустую стопку"""
        return self.plates == []

    def add_plate(self, plate):
        """добавление тарелки в стопку"""
        self.plates.append(plate)

    def pop_plate(self):
        """удаление тарелки"""
        return self.plates.pop()

    def get_plate(self):
        """получение тарелки"""
        return self.plates[len(self.plates) - 1]

    def get_size(self):
        """получение размера стопки"""
        return len(self.plates)


class PlatesStacks:
    """Реализация класса списка стопок тарелок"""

    def __init__(self):
        self.stacks = []

    def add_stack(self, stack):
        """добавление стопки тарелок в конец(конец = голова стека)"""
        self.stacks.append(stack)

    def pop_stack(self):
        """удаление стопки тарелок"""
        return self.stacks.pop()

    def get_size(self):
        """проверка длинны стопки"""
        return len(self.stacks)

    def get_stack(self):
        """получение стопки тарелок в голове"""
        return self.stacks[len(self.stacks) - 1]

    def is_empty(self):
        """проверка: есть ли стопки тарелок"""
        return self.stacks == []


plates_list = ['blue plate', 'red plate', 'green plate',
               'orange plate', 'pink plate', 'black plate',
               'brown plate']

stacks = PlatesStacks()
stacks.add_stack(PlatesStack())
for pl in plates_list:
    if stacks.get_stack().get_size() < 3:
        stacks.get_stack().add_plate(pl)
    else:
        stacks.add_stack(PlatesStack())
        stacks.get_stack().add_plate(pl)

while not stacks.is_empty():
    print(f"stack number: {stacks.get_size()}")
    print("-" * 20)
    print()
    while not stacks.get_stack().is_empty():
        print(f"{stacks.get_stack().pop_plate()}")
        print("\____________/")
    print()
    print("-" * 20)
    stacks.pop_stack()
