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
    def __init__(self, max_stack_size = 10):
        self.elems = [[]]                               # список стопок
        self.one_stack_size = max_stack_size            # макс. размер стопки
        self.stack_count = 0                            # количество стопок - 1
        self.cur_stack = self.elems[self.stack_count]   # последняя стопка

    def is_empty(self):
        return (self.cur_stack == []) and (self.stack_count == 0)

    def push_in(self, el):
        if len(self.cur_stack) >= self.one_stack_size:
            self.elems.append([])
            self.stack_count += 1
            self.cur_stack = self.elems[self.stack_count]
        self.cur_stack.append(el)

    def pop_out(self):
        result = self.cur_stack.pop()
        if (len(self.cur_stack) == 0) and (self.stack_count > 0):
            self.stack_count -= 1
            self.elems.pop()
            self.cur_stack = self.elems[self.stack_count]
        return result

    def get_val(self):
        return self.cur_stack[len(self.cur_stack) - 1]

    def stack_size(self):
        return self.stack_count * self.one_stack_size + len(self.cur_stack)
