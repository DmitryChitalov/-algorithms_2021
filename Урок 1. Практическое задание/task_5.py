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
class StacksPlates:
    #Стопки тарелок, каждая из которых имеет максимальный размер max_size.
    def __init__(self, max_size):
        self.max_size = max_size
        self.stacks_plates = [[]]

    #Просмотр тарелок в стопке
    def __str__(self):
        return f'Стопки тарелок:{self.stacks_plates}'

    #Проверка, пустая ли стопка.
    def is_empty(self):
        return self.stacks_plates == [[]]

    #Добавление тарелки в стопку
    def push_plates(self, el):
        if self.check_plates_size() == True:
            self.stacks_plates[len(self.stacks_plates)-1].append(el)
        elif self.check_plates_size() == False:
            self.stacks_plates.append([])
            self.stacks_plates[len(self.stacks_plates)-1].append(el)

    #Удаление последней тарелки из стопки
    def pop_out_plates(self):
        result = self.stacks_plates[len(self.stacks_plates) - 1].pop()
        if len(self.stacks_plates[len(self.stacks_plates) - 1]) == 0:
            self.stacks_plates.pop()
        return result

    #Количества тарелок в стопке
    def plates_size(self):
        return len(self.stacks_plates[len(self.stacks_plates)-1])

    #Проверка услови максимального количества тарелок в стопке
    def check_plates_size(self):
        if self.plates_size() < self.max_size:
            return True
        else:
            return False

    #Подсчет общего количества тарелок
    def stack_size(self):
        elem_sum = 0
        for stack in self.stacks_plates:
            elem_sum += len(stack)
        return elem_sum

    #Подсчет количества стопок
    def stack_count(self):
        return len(self.stacks_plates)

if __name__ == '__main__':
    stacks_1 = StacksPlates(5)
    print(stacks_1.is_empty())
    stacks_1.push_plates('1')
    print(stacks_1)
    stacks_1.push_plates('2')
    stacks_1.push_plates('3')
    stacks_1.push_plates('4')
    stacks_1.push_plates('5')
    stacks_1.push_plates('6')
    stacks_1.push_plates('7')
    print(stacks_1.is_empty())
    print(stacks_1)
    stacks_1.pop_out_plates()
    stacks_1.pop_out_plates()
    print(stacks_1)
    print(stacks_1.stack_count())
    print(stacks_1.stack_size())