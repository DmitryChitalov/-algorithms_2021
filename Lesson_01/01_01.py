"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

#interval = int(input('Введите интервал в секундах: '))
interval = 500000000
result = str(interval % 60) + ' сек.'
interval = interval // 60
if interval > 0 :
    result = str(interval % 60) + ' мин. ' + result
    interval = interval // 60
if interval > 0 :
    result = str(interval % 60) + ' ч. ' + result
    interval = interval // 60
if interval > 0 :
    result = str(interval % 24) + ' д. ' + result
    interval = interval // 24
if interval > 0 :
    result = str(interval % 30) + ' мес. ' + result
    interval = interval // 30
if interval > 0 :
    result = str(interval % 12) + ' г. ' + result
print('Результат: {}'.format(result))


