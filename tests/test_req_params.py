''' Тесты для класса параметры запроса с помощью pytest'''
import pytest
from src.req_params import RequestParameter


def test_params():
    request = RequestParameter(count=100, page=0, archive=False, search=['python', 'developer'])
    assert request.count == 100
    assert request.page == 0
    assert not request.archive
    assert request.search == ['python', 'developer']
