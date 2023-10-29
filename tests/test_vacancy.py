''' Тесты для классов API с помощью pytest'''
import pytest
from src.vacancy import Vacancy


def test_vacancy():
    vacancy1 = Vacancy(title='vacancy 1')
    vacancy2 = Vacancy(title='vacancy 2', salary=10000)
    assert len(Vacancy.vacancies) == 2
    assert vacancy1.title == 'vacancy 1'
    assert vacancy2.title == 'vacancy 2'
    assert vacancy1.salary == 0
    assert vacancy2.salary == 10000
