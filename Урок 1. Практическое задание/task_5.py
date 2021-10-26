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

Solution: Доработал функции push_plate и pop_plate (добавление в стек и удаление из него).

"""


class StackPlates:
    def __init__(self):
        self.st = []
        self.current_st = []

    def is_empty(self):
        return self.current_st == []

    def push_plate(self):
        if len(self.current_st) < 10:
            self.current_st.append('plate')
        else:
            self.st.append(self.current_st[:])
            self.current_st.clear()

    def pop_plate(self):
        if self.current_st:
            self.current_st.pop(-1)
        else:
            self.st[-1].pop()

    def get_val(self):
        return self.current_st[len(self.current_st) - 1]

    def cur_stack_size(self):
        return self.current_st

    def stack_size(self):
        return self.st

    def stack_count(self):
        return len(self.st)


sp_obj = StackPlates()

# наполняем стек тарелок
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()
sp_obj.push_plate()

print(sp_obj.stack_size())
# удаляем из стека тарелок

sp_obj.pop_plate()
sp_obj.pop_plate()
sp_obj.pop_plate()

print(sp_obj.stack_size())