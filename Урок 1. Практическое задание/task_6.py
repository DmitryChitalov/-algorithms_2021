"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class Que():
    def __init__(self, answ):
        self.answ = answ
        self.rig = []
        self.no_rig = []

    def rigs(self, ed):
        self.rig.append(ed)

    def no_rigs(self, ed):
        self.no_rig.append(ed)

    def decision(self, dec, num):
        otv = self.answ.pop(0)
        if dec == otv:
            self.rigs(f"{num} задания верное ответ: {otv}")
        else:
            self.no_rigs(f"{num} задание неверно ответ: {otv}")

    def result(self):
        return self.rig,self.no_rig


def board():
    answ = [1, 2, 5, 2, 6]
    dec1, dec2, dec3, dec4, dec5 = int(input("10/10 ")), int(input("корень 4 ")), int(input("20-15 ")), int(input("2*1 ")), int(input("1+1+1+1+1+1 "))
    dec = [dec1, dec2, dec3, dec4, dec5]
    queue = Que(answ)
    num = 0
    for i in dec:
        num+= 1
        queue.decision(i,num)
    print(queue.result())

board()
