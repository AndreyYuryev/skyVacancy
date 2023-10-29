import abc
from abc import ABC, abstractmethod
from src.env import EnvParameter
from src.req_params import RequestParameter
import requests
import json


class API(ABC):
    """ Класс для описания абстрактных методов API """

    def __init__(self, test_mode=False):
        """ Инициализировать атрибуты """
        self.__test_mode = test_mode

    @property
    def test_mode(self):
        """ Флаг тестового режима """
        return self.__test_mode

    def _get_response_json(self, url=str(), params=dict(), headers=dict()):
        """ Получить ответ на запрос и распарсить JSON """
        rsp = requests.get(url=url, params=params, headers=headers)
        rsp_json = rsp.json()
        return rsp_json

    @abstractmethod
    def _get_api_key(self):
        """ Получить ключ из переменных окружения """
        pass

    @abstractmethod
    def _create_headers(self):
        """ Создать словарь с заголовком запроса """
        pass

    @abstractmethod
    def _create_params(self, request_params: RequestParameter):
        """ Создать словарь с параметрами запроса """
        pass

    @abstractmethod
    def get_vacancies(self, request_params: RequestParameter):
        """ Получить словарь с вакансиями """
        pass


class SuperJobAPI(API):
    """ API для работы с вакансиями от superjob.ru """

    def __init__(self, test_mode=False):
        """ Инициализировать атрибуты """
        super().__init__(test_mode)
        self.__url = 'https://api.superjob.ru/2.0/vacancies/'
        self.__headers = self._create_headers()

    def _get_api_key(self):
        """ Получить api key для объекта с конструктором """
        if super().test_mode:
            return EnvParameter().api_key('TEST_SUPERJOB_API_KEY')
        else:
            return EnvParameter().api_key('SUPERJOB_API_KEY')

    def _create_headers(self):
        return {"X-Api-App-Id": self._get_api_key()}

    def _create_params(self, request_params: RequestParameter):
        params = dict()
        params['count'] = request_params.count
        params['page'] = request_params.page
        params['archive'] = request_params.archive
        # формирование запроса
        # поиск везде по ключевым словам
        params['keyword'] = ' '.join(request_params.search)

        return params

    def get_vacancies(self, request_params: RequestParameter):
        vacancies = self._get_response_json(url=self.__url, headers=self.__headers,
                                            params=self._create_params(request_params=request_params))
        print(f'\n----- SuperJob-----')
        for vacancy in vacancies['objects']:
            print(vacancy['profession'])


class HeadHunterAPI(API):
    """ API для работы с вакансиями от headhunter.ru """

    def __init__(self, test_mode=False):
        """ Инициализировать атрибуты """
        super().__init__(test_mode)
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = self._create_headers()

    def _get_api_key(self):
        """ Получить api key для объекта без конструктора """
        if super().test_mode:
            return EnvParameter().api_key('TEST_HEADHUNTER_API_KEY')
        else:
            return EnvParameter().api_key('HEADHUNTER_API_KEY')

    def _create_headers(self):
        return {}

    def _create_params(self, request_params: RequestParameter):
        params = dict()
        params['count'] = request_params.count
        params['page'] = request_params.page
        params['archive'] = request_params.archive
        # формирование запроса
        # поиск везде по ключевым словам
        params['text'] = ' '.join(request_params.search)
        return params

    def get_vacancies(self, request_params: RequestParameter):
        vacancies = self._get_response_json(url=self.__url, headers=self.__headers,
                                            params=self._create_params(request_params=request_params))
        print(f'\n-----HeadHunter-----')
        for vacancy in vacancies['items']:
            print(vacancy['name'])
