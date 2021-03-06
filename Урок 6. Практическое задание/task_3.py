from memory_profiler import profile
"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""


@profile
def func1(number, result=''):
    def make_palindrome(num=number, res=result):
        if num == 0:
            return res
        new_number = num % 10
        res = res + str(new_number)
        make_palindrome(num // 10, res)
    return make_palindrome(number)


print(func1(102))
"""
При профилировании рекурсивной функции она при каждом рекурсивном вызове показывает профилировку.
Чтобы это исправить нужно обернуть рекурсию еще в одну функцию
"""