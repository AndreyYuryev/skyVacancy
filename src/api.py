import abc
from abc import ABC
from src.env import EnvParameter


class API(ABC):
    """ Класс для описания абстрактных методов API """

    def __init__(self, test_mode=False):
        """ Инициализировать атрибуты """
        self.__test_mode = test_mode

    @abc.abstractmethod
    def get_api_key(self):
        pass

    @property
    def test_mode(self):
        """ Флаг тестового режима """
        return self.__test_mode


class SuperJobAPI(API):
    """ API для работы с вакансиями от superjob.ru """

    def __init__(self, test_mode=False):
        """ Инициализировать атрибуты """
        super().__init__(test_mode)

    def get_api_key(self):
        """ Получить api key для объекта с конструктором """
        if super().test_mode:
            return EnvParameter().api_key('TEST_SUPERJOB_API_KEY')
        else:
            return EnvParameter().api_key('SUPERJOB_API_KEY')


class HeadHunterAPI(API):
    """ API для работы с вакансиями от headhunter.ru """

    def get_api_key(self):
        """ Получить api key для объекта без конструктора """
        if self.test_mode:
            return EnvParameter().api_key('TEST_HEADHUNTER_API_KEY')
        else:
            return EnvParameter().api_key('HEADHUNTER_API_KEY')
