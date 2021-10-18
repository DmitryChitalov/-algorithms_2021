"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным.
Пункты 2 и 3 можно выполнить через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

from operator import itemgetter


class StorageLst:
    """Класс реализует хранилище с информацией о компаниях: название и годовая
    прибыль на базе списка кортежей"""

    def __init__(self):
        """Конструктор - создаем пустой список для хранения"""
        self.storage_lst = list()

    def __str__(self):
        """Отображение объекта в строку"""
        MAX_FOR_STRICT = 20  # макс. кол-во эл-тов для полного показа хранилища
        CNT_FIRST_LAST = 5  # кол-во эл-тов с начала и конца для частичн. отобр.

        count = self.count()
        if count > MAX_FOR_STRICT:
            return f'Storage_lst (count: {count}): ' \
                   f'{self.storage_lst[:CNT_FIRST_LAST]}' \
                   f' ... ' \
                   f'{self.storage_lst[-CNT_FIRST_LAST:]}'
        return f'Storage_lst (count: {count}): {self.storage_lst}'

    def count(self):
        """Кол-во записей в хранилище"""
        return len(self.storage_lst)

    def append(self, company_name, year_income):
        """Добавление записи в хранилище"""
        self.storage_lst.append((company_name, year_income))

    def pop(self, idx=None):
        """Извлечение записи с удалением из хранилища"""
        max_idx = self.storage_lst.count() - 1
        if idx is None:
            return self.storage_lst.pop()
        if -max_idx <= idx <= max_idx:
            return self.storage_lst.pop(idx)  # else => None

    def get_idx(self, idx=None):
        """Получение записи из хранилища по индексу"""
        max_idx = len(self.storage_lst) - 1
        if idx is None:
            return self.storage_lst[max_idx]
        if -max_idx <= idx <= max_idx:
            return self.storage_lst[idx]  # else => None

    def get_company(self, company):
        """Получение записи из хранилища по названию компании"""
        for idx, curr_el in enumerate(self.storage_lst):
            curr_comp, curr_income = curr_el[0], curr_el[1]
            if curr_comp == company:
                return idx, curr_comp, curr_income

    def del_idx(self, idx=None):
        """Удаление элемента из хранилища по индексу (если не указан,
        то удаляется последний элемент)"""
        if idx is None:
            self.storage_lst.pop()
            exit(0)
        self.storage_lst.pop(idx)

    def get_max_income(self, max_cnt=1):
        """Выдача max_cnt кортежей эл-тов из хранилища (по-умолчанию - 1).
        Если запрошено больше эл-тов, чем есть в хранилище, то возвращает
        целиком отсортированное хранилище"""

        # сортируем inplace хранилище по убыванию годовой прибыли компаний
        self.storage_lst.sort(key=itemgetter(1), reverse=1)
        return self.storage_lst[:max_cnt]


class StorageDict:
    """Класс реализует хранилище с информацией о компаниях: название и годовая
    прибыль на базе словаря"""

    def __init__(self):
        """Конструктор - создаем пустой список для хранения"""
        self.storage_dict = dict()

    def __str__(self):
        """Отображение объекта в строку"""

        count = self.count()
        return f'Storage_dict (count: {count}): {self.storage_dict}'

    def count(self):
        """Кол-во записей в хранилище"""
        return len(self.storage_dict)

    def append(self, company_name, year_income):
        """Добавление записи в хранилище"""
        self.storage_dict[company_name] = year_income

    def pop(self, company_name):
        """Возвращает (при наличии) - запись из хранилища с company_name с
        удалением из хранилища, если нет - возвращает None"""
        self.storage_dict.pop(company_name, default=None)

    def get_company(self, company_name):
        """Получение записи из хранилища по названию компании, если компании
        нет в хранилище - возвращает (company_name, None)"""
        return company_name, self.storage_dict.get(company_name, default=None)

    def del_idx(self, idx=None):
        """Удаление элемента из хранилища по индексу (если не указан,
        то удаляется последний элемент)"""
        if idx is None:
            self.storage_lst.pop()
            exit(0)
        self.storage_lst.pop(idx)

    def get_max_income(self, max_cnt=1):
        """Выдача max_cnt кортежей эл-тов из хранилища (по-умолчанию - 1).
        Если запрошено больше эл-тов, чем есть в хранилище, то возвращает
        целиком отсортированное хранилище"""

        # получаем список отсортированных ключей словаря по убыванию значений
        sorted_keys = sorted(self.storage_dict, key=self.storage_dict.get(),
                             reverse=1)
        print(f"отсортированные по значению ключи {sorted_keys}")
        # return self.storage_lst[:max_cnt]


if __name__ == "__main__":

    print("\nРеализация хранилища на базе списка кортежей:")
    storage_lst = StorageLst()
    # добавление данных в хранилище
    storage_lst.append('XXX', 123456)
    storage_lst.append('YYY', 654321)
    storage_lst.append('AAA', 111111)
    storage_lst.append('ZZZ', 101010)
    print(f'Метод __str__: {storage_lst}')
    print(f'Метод get_company: {storage_lst.get_company("XXX")}')
    print(f'Метод get_idx: {storage_lst.get_idx()}')
    print(f'Метод get_max: {storage_lst.get_max_income(max_cnt=3)}')

    print("\nРеализация хранилища на базе словаря:")
    storage_dict = StorageDict()
    # добавляем данные в хранилище
    storage_dict.append('XXX', 123456)
    storage_dict.append('YYY', 654321)
    storage_dict.append('AAA', 111111)
    storage_dict.append('ZZZ', 101010)
    print(f'Метод __str__: {storage_dict}')
