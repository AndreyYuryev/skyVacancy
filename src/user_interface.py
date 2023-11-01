from req_params import SearchParameter, RequestParameter
from api import SuperJobAPI, HeadHunterAPI


class ExitException(Exception):
    pass


class UserInterface:
    """ Пользовательский интерфейс по работе с вакансиями """

    def __init__(self):
        self.__platform = []
        self.__vacancies = []
        print(f'Для завершения программы при любом вводе данных введите: exit')

    def execute(self):
        """ Процесс обработки команд пользователя"""
        self.__platform = self.__search_platform()
        self._search_vacancies()
        self.__sort_vacancies()
        self.__list_vacancies()

    def __ask_user(self, input_string):
        """ Проверка ввода пользователя на завершение программы """
        answer = input(input_string)
        if answer == 'exit':
            raise ExitException
        return answer

    def _search_vacancies(self):
        """ Процесс поиска вакансий """
        answer = self.__ask_user(f'Введите ключевое слова для поиска вакансий: ')

        search_prm = SearchParameter(keywords=[answer])
        req_prm = RequestParameter(count=100, page=0, archive=False, search=search_prm)

        for item in self.__platform:
            if item == 'HH':
                # искать вакансии на HH
                hh = HeadHunterAPI()
                hh_vacancies = hh.get_vacancies(request_params=req_prm)

            if item == 'SJ':
                # искать вакансии на SJ
                sj = SuperJobAPI()
                sj_vacancies = sj.get_vacancies(request_params=req_prm)

        self.__vacancies.extend(sj_vacancies)
        self.__vacancies.extend(hh_vacancies)

    def __search_platform(self):
        """ Выбрать платформу """
        platforms = list()
        answer = self.__ask_user(f'Выберите платформу 1-SuperJob 2-HeadHunter 3-обе платформы: ')
        if answer == '1':
            platforms.append('SJ')
        elif answer == '2':
            platforms.append('HH')
        else:
            platforms.append('SJ')
            platforms.append('HH')
        return platforms

    def __sort_vacancies(self):
        """ Сортировать вакансии """
        print(f'По запросу найдено вакансий: {len(self.__vacancies)}')
        answer = self.__ask_user(
            f'Выберите признак сортировки:\n1-Наименование вакансии\n2-Город\n3-Фирма\n4-Зарплата ')
        match answer:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass

    def __list_vacancies(self):
        """ Вывести список вкансий """
        answer = self.__ask_user(
            f'Выберите количество вакансий для вывода: ')
        counter = int(answer)
        if counter > len(self.__vacancies):
            counter = len(self.__vacancies)
        for index in range(counter):
            print(self.__vacancies[index])