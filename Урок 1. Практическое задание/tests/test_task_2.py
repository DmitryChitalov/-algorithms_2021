from task_2 import min_n2, min_n
import pytest

# Тестовый набор данных с ожидаемыми значениями
tests = [([9, -1, 0, 2, 4], -1),
         ([3, 4, 5, 10], 3),
         ([23, 112, 2, -8, 1024], -8)]


@pytest.mark.parametrize("lst, l_expected", tests)
def test_min_n2(lst, l_expected):
    # Проверка функции min_n2
    assert min_n2(lst) == l_expected


@pytest.mark.parametrize("lst, l_expected", tests)
def test_min_n(lst, l_expected):
    # Проверка функции min_n
    assert min_n(lst) == l_expected
