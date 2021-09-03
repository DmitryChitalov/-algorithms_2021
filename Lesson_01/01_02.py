"""
Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только
арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых
делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.
"""
numbers = []
for i in range(500):
  numbers.append((i*2+1)**3)

summa = 0
for num in numbers :
  a = num
  digit_sum = 0
  while a > 0 :
    b = a % 10
    digit_sum += b
    a = a // 10
  if ((digit_sum % 7) == 0 ) :
    summa += num

print('Final summa = {}'.format(summa))

for i in range(500):
  numbers[i] = numbers[i] + 17

summa = 0
for num in numbers :
  a = num
  digit_sum = 0
  while a > 0 :
    b = a % 10
    digit_sum += b
    a = a // 10
  if ((digit_sum % 7) == 0 ) :
    summa += num

print('Final summa = {}'.format(summa))

