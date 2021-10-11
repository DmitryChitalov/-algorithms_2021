from task_1_1 import decor

# Курс алгоритмы.


@decor
def my_reverse(enter_num):
    if enter_num == 0:
        return ''
    return f"{str(enter_num % 10)}{my_reverse(enter_num // 10)}"


@decor
def my_reverse_2(enter_num):
    return str(enter_num)[::-1]


if __name__ == '__main__':
    test1, m_diff, t_diff = my_reverse(742234523452345234523453)
    print(f"Использование памяти my_reverse: {m_diff} Mib")
    print(f'Время выполнения my_reverse: {t_diff}')

    test2, m_diff2, t_diff2 = my_reverse_2(742234523452345234523453)
    print(f"Использование памяти my_reverse_2: {m_diff2} Mib")
    print(f'Время выполнения my_reverse_2: {t_diff2}')

    """
    Использование памяти my_reverse: 16.0390625 Mib
    Время выполнения my_reverse: 5.02
    Использование памяти my_reverse_2: 0.0 Mib
    Время выполнения my_reverse_2: 3.04
    
    Используя срез мы минимизировали объем используемой памяти.
    """
