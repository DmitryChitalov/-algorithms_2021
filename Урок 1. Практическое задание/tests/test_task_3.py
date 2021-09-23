from task_3 import most_profit_v1, most_profit_v2
import pytest

# Тестируемый список
companies = [((("Walmart", 524000),
               ("Saudi Aramco", 329800),
               ("State Grid", 387000),
               ("Sinopec Group", 369200),
               ("BP", 278400),
               ("China National Petroleum", 364100),
               ("Royal Dutch Shell", 311600),
               ("Toyota", 280500),
               ("Volkswagen", 275200),
               ("Exxon Mobil", 265700),
               ),
              (("Walmart", 524000),
               ("State Grid", 387000),
               ("Sinopec Group", 369200)))]


@pytest.mark.parametrize("companies_tuple, companies_expected", companies)
def test_most_profit_v1(companies_tuple, companies_expected):
    assert most_profit_v1(companies_tuple) == companies_expected


@pytest.mark.parametrize("companies_tuple, companies_expected", companies)
def test_most_profit_v2(companies_tuple, companies_expected):
    assert most_profit_v2(companies_tuple) == companies_expected
