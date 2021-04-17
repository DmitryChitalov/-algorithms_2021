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


class StackClass:
    def __init__(self, count):
        self.plat_list = []
        self.new_plat_list = []
        self.max_of_plates = count

    def push_in(self, count):
        self.plat_list.append(count)
        while self.stack_size() > self.max_of_plates:
            self.new_plat_list.append(self.plat_list[:self.max_of_plates])
            self.plat_list = self.plat_list[self.max_of_plates:]

    def all_stack_size(self):
        return self.new_plat_list + self.plat_list

    def stack_size(self):
        return len(self.plat_list)


game = StackClass(5)

for i in range(1, 14):
    game.push_in(i)
    print(game.all_stack_size())
