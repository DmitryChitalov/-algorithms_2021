"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
__mul__
__адд__
Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
1. вариант
defaultdict(список)
int(, 16)
уменьшить
2. вариант
шестнадцатеричный номер класса:
 __адд__
 __mul__
hx = шестнадцатеричный номер
хх + хх
шестигранник()
"""
from collections import defaultdict

nums = defaultdict(list)

for i in range(2):
    number = input(f'Введите {i+1} число: ').upper()
    nums[f'{i+1} число - {number}'] = list(number)
print(nums)

#
sum_nusm = sum(int(''.join(i), 16) for i in nums.values())
print("Сумма равна: ", list('%X' % sum_nusm))


nums_for_multiplication = [int(''.join(i), 16) for i in nums.values()]
multi_nums = nums_for_multiplication[0] * nums_for_multiplication[1]
print("Произведение равно: ", list('%X' % multi_nums))
