from abc import ABC


class API(ABC):
    ''' класс для описания абстрактных методов API '''
    pass


class SuperJobAPI(API):
    ''' API для работы с вакансиями от superjob.ru '''
    def __init__(self):
        pass


class HeadHunterAPI(API):
    ''' API для работы с вакансиями от headhunter.ru '''
    def __init__(self):
        pass
