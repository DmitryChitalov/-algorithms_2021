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


class Ocered():
    def __init__(self, otvet):
        self.otvet = otvet
        self.ver = []
        self.never = []

    def verno(self, ed):
        self.ver.append(ed)

    def neverno(self, ed):
        self.never.append(ed)

    def decision(self, dec, num):
        otv = self.otvet.pop(0)
        if dec == otv:
            self.verno(f"{num} задания верное ответ: {otv}")
        else:
            self.neverno(f"{num} задание неверно ответ: {otv}")

    def result(self):
        return self.ver,self.never


def doska():
    otvet = [1, 2, 5, 2, 6]
    dec1, dec2, dec3, dec4, dec5 = int(input("10/10 ")), int(input("корень 4 ")), int(input("20-15 ")), int(input("2*1 ")), int(input("1+1+1+1+1+1 "))
    dec = [dec1, dec2, dec3, dec4, dec5]
    oceredi = Ocered(otvet)
    num = 0
    for i in dec:
        num+= 1
        oceredi.decision(i,num)
    print(oceredi.result())

doska()