"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print({k: v for k, v in sorted(x.items(), key=lambda item: item[1])})

comp_n = {"compA": 200000, "compB": 4000000, "IBM": 3000, "compD": 100000, "myCompAny": 10000000}


# comment the complexity !
def func1(data):
    # TODO realize throw exception if data less then 3
    data_sorted = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
    return {data_sorted.popitem(), data_sorted.popitem(), data_sorted.popitem()}


print(func1(x))
print(func1(comp_n))


#############################################################################################


class Top3comp:

    def __init__(self):
        self.keyset = [None] * 3
        self.valset = [None] * 3

    def run(self, key, val):
        if self.valset[0] is None:
            self.valset[0] = val
            self.keyset[0] = key
        elif self.valset[1] is None:
            self.valset[1] = val
            self.keyset[1] = key
        elif self.valset[2] is None:
            self.valset[2] = val
            self.keyset[2] = key
        elif self.valset[0] < val:
            self.valset = [val, self.valset[0], self.valset[1]]
            self.keyset = [key, self.keyset[0], self.valset[1]]
        elif self.valset[1] < val:
            self.valset = [self.valset[0], val, self.valset[1]]
            self.keyset = [self.keyset[0], key, self.valset[1]]
        elif self.valset[2] < val:
            self.valset = [self.valset[0], self.valset[1], val]
            self.keyset = [self.keyset[0], self.valset[1], key]

    def getTo3(self):
        return {
            self.keyset[0]: self.valset[0],
            self.keyset[1]: self.valset[1],
            self.keyset[2]: self.valset[2],
        }



