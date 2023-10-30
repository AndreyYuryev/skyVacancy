class Vacancy:
    """ Описание найденной вакансии"""

    __Vacancies = []

    def __init__(self, title='', salary={}, link='', city=''):
        self.__title = title
        if salary is not None:
            self.__salary_from = int(salary.get('from', 0))
            self.__salary_to = int(salary.get('to', 0))
        else:
            self.__salary_from = 0
            self.__salary_to = 0
        self.__link = link
        self.__city = city
        Vacancy.__Vacancies.append(self)

    def __eq__(self, other):
        """ Зарплаты равны """
        if isinstance(other, Vacancy):
            if max(self.salary) == max(other.salary):
                return True
        return False

    def __lt__(self, other):
        """ Зарплата меньше """
        if isinstance(other, Vacancy):
            if max(self.salary) < max(other.salary):
                return True
        return False

    def __gt__(self, other):
        """ Зарплата больше """
        if isinstance(other, Vacancy):
            if max(self.salary) > max(other.salary):
                return True
        return False

    @classmethod
    @property
    def vacancies(cls):
        """ Список вакансий """
        return cls.__Vacancies

    @property
    def title(self):
        """ Название вакансии """
        return self.__title

    @property
    def salary(self):
        """ Зарплата """
        return self.__salary_from, self.__salary_to

    @property
    def link(self):
        """ Ссылка на описание вакансии """
        return self.__link

    @property
    def city(self):
        """ Город """
        return self.__city
