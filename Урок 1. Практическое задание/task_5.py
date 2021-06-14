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


# 2)
# stek = []
# stek_stek = []
# while True:
#     tarelka = input("добавь в стэк\n")
#     if tarelka == '':
#         stek_stek.append(stek)
#         break
#     if len(stek) < 3:               # стопка
#         stek.append(tarelka)
#     else:
#         stek_stek.append(stek)
#         stek = []                   # если тут stek.clear() то очищало и stek_stek ?
#         stek.append(tarelka)
#
# print(stek_stek)
# print("стопок в стэке =", len(stek_stek))
# # извлечение из стэка
# print("извлекаем из стэка")
# for i in range(len(stek_stek)):
#     print(f'стопка {i + 1}')
#     tmp = stek_stek.pop(-1)
#     for j in range(len(tmp)):
#         print(tmp.pop(-1))
# print('стэк пуст')

# 1)
class Stek:
    _stek = []
    _stek_tmp = []

    @staticmethod
    def stek_add(tmp):
        if len(Stek._stek_tmp) < 3:
            Stek._stek_tmp.append(tmp)
        else:
            Stek._stek.append(Stek._stek_tmp)
            Stek._stek_tmp = []
            Stek._stek_tmp.append(tmp)

        print(Stek._stek + Stek._stek_tmp)

    @staticmethod
    def stek_pop():
        print(Stek._stek)


a = Stek()
a.stek_add(1)
a.stek_add(2)
a.stek_add(3)
a.stek_add(4)
a.stek_add(5)
a.stek_add(6)
a.stek_add(7)
a.stek_add(8)

a.stek_pop()
a.stek_pop()