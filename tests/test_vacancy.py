''' Тесты для классов API с помощью pytest'''
import pytest
from src.vacancy import Vacancy


def test_vacancy():
    vacancy1 = Vacancy(title='vacancy 1', link='https:/testvacancy.ru')
    vacancy2 = Vacancy(title='vacancy 2', salary={'from': 10000, 'to': 0}, city='Moscow')
    assert len(Vacancy.vacancies) == 2
    assert vacancy1.title == 'vacancy 1'
    assert vacancy2.title == 'vacancy 2'
    assert vacancy1.salary == (0, 0)
    assert vacancy2.salary == (10000, 0)
    assert vacancy1.link == 'https:/testvacancy.ru'
    assert vacancy2.link == ''
    assert vacancy1.city == ''
    assert vacancy2.city == 'Moscow'


def test_salary():
    vacancy1 = Vacancy(title='vacancy 1', salary={'from': 20000, 'to': 0})
    vacancy2 = Vacancy(title='vacancy 2', salary={'from': 10000, 'to': 0})
    vacancy3 = Vacancy(title='vacancy 3', salary={'from': 10000, 'to': 0})
    vacancy4 = Vacancy(title='vacancy 4', salary={'from': 10000, 'to': 20000})
    assert vacancy2 < vacancy1
    assert vacancy1 > vacancy2
    assert vacancy2 == vacancy3
    assert vacancy4 > vacancy3
    assert vacancy4 == vacancy1
