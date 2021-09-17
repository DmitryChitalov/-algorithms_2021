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
# 1 способ

n = int(input())
plates = []
shelf = []
max = 6
count = 0

while count != n:
    plates.append('_')
    count += 1
    if count % max == 0:
        shelf.append(plates.copy())
        plates.clear()
shelf.append(plates)

print(shelf)

# 2 способ через классы
class Stack:
    def __init__(self):
        self.stack = []
        self.max = None
        self.shelf = []

    def get_max(self, m):
        self.max = m

    def push(self, item):
        self.stack.append('_')
        if len(self.stack) == self.max:
            self.shelf.append(self.stack.copy())
            self.stack.clear()

    def get_shelf(self, y):
        return self.shelf + self.stack

plate = Stack()
plate.get_max(5)
plate.push(1)
plate.push(1)
plate.push(1)
plate.push(1)
plate.push(1)
plate.push(1)
plate.push(1)
plate.push(1)
print(plate.stack)
print(plate.shelf)
print(plate.get_shelf(1))
