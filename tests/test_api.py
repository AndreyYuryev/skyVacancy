''' Тесты для классов API с помощью pytest'''
import pytest
from src.api import HeadHunterAPI, SuperJobAPI
from src.req_params import RequestParameter


def test_api_key():
    """ Проверить чтение тестовых переменных окружения """
    sj = SuperJobAPI(test_mode=True)
    hh = HeadHunterAPI(test_mode=True)
    assert sj._get_api_key() == 'TEST111'
    assert hh._get_api_key() == 'TEST222'


def test_params():
    sj = SuperJobAPI()
    hh = HeadHunterAPI()
    req_parm = RequestParameter(search=['python', 'django'])
    assert sj._create_params(req_parm) == {
        "archive": False,
        "count": 100,
        "keyword": 'python django',
        "page": 0,
    }
    assert hh._create_params(req_parm) == {
        "archive": False,
        "count": 100,
        "page": 0,
        "text": 'python django',
    }


def test_vacancies():
    sj = SuperJobAPI()
    hh = HeadHunterAPI()
    req_parm = RequestParameter(search=['python', 'django'])
    sj_vacancies = sj.get_vacancies(request_params=req_parm)
    hh_vacancies = hh.get_vacancies(request_params=req_parm)
    all_vacancies = len(sj_vacancies) + len(hh_vacancies)
    count_vacancies = len(sj_vacancies[0].vacancies)
    assert sj_vacancies is not None
    assert hh_vacancies is not None
    assert all == count_vacancies

