''' Тесты для классов API с помощью pytest'''
import pytest
from src.api import HeadHunterAPI, SuperJobAPI


def test_api_key():
    """ Проверить чтение тестовых переменных окружения """
    sj = SuperJobAPI(test_mode=True)
    hh = HeadHunterAPI(test_mode=True)
    assert sj.get_api_key() == 'TEST111'
    assert hh.get_api_key() == 'TEST222'


def test_value():
    pass