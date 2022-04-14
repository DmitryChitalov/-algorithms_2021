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

class  PlateStack:
    def __init__(self, size):
        self.elem = []
        self.size = size

    def __str__(self):
        return str(self.elem)

    def empt(self):
        return self.elem == [[]]

    def push(self,elm):
        if len(self.elem[len(self.elem)-1]) < self.size:
            self.elem[len(self.elem)-1].append(elm)
        else:
            self.elem.append([])
            self.elem[len(self.elem)-1].append(elm)

    def out(self):
         result = self.elem[len(self.elem)- 1]
         [len(self.elem[len(self.elem) - 1])-1]

    def stack_size(self):
        el_sum = 0
        for i in self.elem:
            el_sum += len(i)
        return el_sum

    def st_count(self):
        return len(self.elem)


if __name__ == '__main__':
    plate = PlateStack(2)
    plate.push('pl1')
    plate.push('pl2')
    plate.push('pl3')
    print(plate)
    
    
    
 # у меня почему-то выдает ошибку:  IndexError: list index out of range
