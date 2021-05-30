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
    def __init__(self, limit):
        self.limit = limit
        self.stack = [[]]

    def add_plate(self, plate):
        if len(self.stack[len(self.stack)-1]) < int(limit):
            self.stack[len(self.stack)-1].append(plate)
        else:
            self.stack.append([])
            self.stack[len(self.stack)-1].append(plate)

    def __str__(self):
        return str(self.stack)

if __name__ == '__main__':
    limit = input('Введите макисмальное количество тарелок в стопке: ')

    plates = PlatesStack(limit)
    plates.add_plate('First plate')
    plates.add_plate('Second plate')
    plates.add_plate('Third plate')
    plates.add_plate('Fourth plate')
    plates.add_plate('Fifth plate')
    print(plates)

