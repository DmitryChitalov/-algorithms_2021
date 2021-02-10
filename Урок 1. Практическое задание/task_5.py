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


class PlatePile:
    def __init__(self, size):
        self.pile = []
        self.size = size

    def put_plate(self):
        if len(self.pile) < self.size:
            self.pile.append('plate')

    def if_full(self):
        return len(self.pile) >= self.size

    def take_plate(self):
        return self.pile.pop()

    def pile_size(self):
        return len(self.pile)


# Создадим несколько экземпляров стека с тарелками:
small_pile = PlatePile(6)
medium_pile = PlatePile(11)
big_pile = PlatePile(15)
# Для удобства взаимодействия поместим их в словарь:
plate_list = [small_pile, medium_pile, big_pile]


# Создадим функцию для взаимодействия с тремя стопками тарелок
def plate_by_plate(amount, piles):
    # Сделаем проверку количества тарелок, которое можно поместить в стопки:
    max_amount = 0
    for pile in piles:
        max_amount += pile.size
    if max_amount < amount:
        print('Вы разложили слишком много тарелок в стопки, и все они разбились')
    else:
        # Помещаем тарелки
        for i in range(amount):
            for pile in piles:
                if pile.if_full() is False:
                    pile.put_plate()
                    break
        # Выводим результат
        print('Количество тарелок в стопках:')
        for ind, pile in enumerate(piles):
            print(f'{ind + 1}) {pile.pile_size()}')


plate_by_plate(21, plate_list)
