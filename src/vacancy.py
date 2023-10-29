class Vacancy:
    """ Описание найденной вакансии"""

    __Vacancies = []

    def __init__(self, title='', salary=0):
        self.__title = title
        self.__salary = int(salary)
        Vacancy.__Vacancies.append(self)

    def __eq__(self, other):
        """ Зарплаты вакансий равны """
        if isinstance(other, Vacancy):
            if self.salary == other.salary:
                return True
        return False

    def __lt__(self, other):
        """ Зарплата вакании меньше """
        if isinstance(other, Vacancy):
            if self.salary < other.salary:
                return True
        return False

    def __gt__(self, other):
        """ Зарплата вакании больше """
        if isinstance(other, Vacancy):
            if self.salary > other.salary:
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
        return self.__salary
