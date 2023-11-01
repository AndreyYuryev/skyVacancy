from req_params import SearchParameter, RequestParameter
from api import SuperJobAPI, HeadHunterAPI
from uploader import JSONUploader


class ExitException(Exception):
    pass


class UserInterface:
    """ Пользовательский интерфейс по работе с вакансиями """

    def __init__(self):
        self.__platform = []
        self.__vacancies = []
        self.__proceed_vacancies = []
        self.__state = 0
        print(f'Для завершения программы при любом вводе данных введите: exit')

    def execute(self):
        """ Процесс обработки команд пользователя"""
        match self.__state:
            case 0:
                # выбор платформы
                self.__platform = self.__search_platform()
            case 1:
                # поиск вакансий
                self.__vacancies = self._search_vacancies()
            case 2:
                # сортировка вакансий
                self.__proceed_vacancies = self.__sort_vacancies()
            case 3:
                # вывод подготовленных вакансий на экран
                self.__list_vacancies()
            case 4:
                # сохранение подготовленных вакансий в файл
                self.__save_vacancies()
            case 5:
                # решение о дальнейшей обработке
                self.__decision()
            case 9:
                raise ExitException

    def __ask_user(self, input_string):
        """ Проверка ввода пользователя на завершение программы """
        answer = input(input_string)
        if answer == 'exit':
            raise ExitException
        return answer

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
        self.__state = 1
        return platforms

    def _search_vacancies(self):
        """ Процесс поиска вакансий """
        answer = self.__ask_user(f'Введите ключевое слова для поиска вакансий: ')

        vacancies = []
        search_prm = SearchParameter(keywords=[answer])
        req_prm = RequestParameter(count=100, page=0, archive=False, search=search_prm)

        for item in self.__platform:
            if item == 'HH':
                # искать вакансии на HH
                hh = HeadHunterAPI()
                hh_vacancies = hh.get_vacancies(request_params=req_prm)
                vacancies.extend(hh_vacancies)

            if item == 'SJ':
                # искать вакансии на SJ
                sj = SuperJobAPI()
                sj_vacancies = sj.get_vacancies(request_params=req_prm)
                vacancies.extend(sj_vacancies)

        print(f'Найдено вакансий: {len(vacancies)}')
        answer = self.__ask_user(f'Дальше\n'
                                 f'1-сортировка вакансий\n'
                                 f'2-вывод на экран\n'
                                 f'3-сохранение в файл: ')
        if answer == '1':
            self.__state = 2
        elif answer == '2':
            self.__state = 3
        elif answer == '3':
            self.__state = 4
        else:
            self.__state = 2
        return vacancies

    def __sort_vacancies(self):
        """ Сортировать вакансии """
        print(f'По запросу найдено вакансий: {len(self.__vacancies)}')
        proceed_vacancies = []
        answer = self.__ask_user(
            f'Выберите признак сортировки:\n'
            f'1-Наименование вакансии\n'
            f'2-Город\n'
            f'3-Фирма\n'
            f'4-Зарплата ')
        match answer:
            case '1':
                proceed_vacancies = sorted(self.__vacancies, key=lambda x: x.title)
            case '2':
                proceed_vacancies = sorted(self.__vacancies, key=lambda x: x.city)
            case '3':
                proceed_vacancies = sorted(self.__vacancies, key=lambda x: x.company)
            case '4':
                proceed_vacancies = sorted(self.__vacancies, key=lambda x: x.salary.max_salary, reverse=True)
        answer = self.__ask_user(
            f'Сколько ТОП записей? ')
        top = int(answer)
        self.__state = 3
        return proceed_vacancies[:top]

    def __list_vacancies(self):
        """ Вывести список вкансий """
        vacancies = self.__get_proceed_vacancies()
        proceed_counter = len(vacancies)

        answer = self.__ask_user(
            f'Выберите количество вакансий для вывода, доступно {proceed_counter}: ')
        counter = int(answer)

        if counter > proceed_counter:
            counter = proceed_counter
        for index in range(counter):
            print(vacancies[index])
        self.__state = 5

    def __save_vacancies(self):
        """ Сохранить подготовленные вакансии в файл """
        answer = self.__ask_user(f'Введите имя файла:')

        # сохранение в файл
        saver = JSONUploader(data=self.__create_json(self.__proceed_vacancies))
        saver.save_file(answer)
        self.__state = 5

    def __decision(self):
        """ Дальнейшая обработка """
        answer = self.__ask_user(
            f'Что дальше?\n'
            f'1-изменить платформы для поиска\n'
            f'2-выполнить поиск по другим критериям\n'
            f'3-выполнить сортировку по другим ключам\n'
            f'4-сохранить в файл\n'
            f'5-вывести на экран: ')
        if answer == '1':
            self.__state = 0
        elif answer == '2':
            self.__state = 1
        elif answer == '3':
            self.__state = 2
        elif answer == '4':
            self.__state = 4
        elif answer == '5':
            self.__state = 3
        else:
            self.__state = 2

    def __get_proceed_vacancies(self):
        """ Получить список подготовленных вакансий """
        if len(self.__proceed_vacancies) == 0:
            self.__proceed_vacancies.extend(self.__vacancies)
        return self.__proceed_vacancies

    def __create_json(self, vacancies):
        """ Создать json для сохранения в файл"""
        json_data = {}
        index = 0
        for vacancy in self.__get_proceed_vacancies():
            index += 1
            json_data[index] = vacancy.get_json_data()
        return json_data
