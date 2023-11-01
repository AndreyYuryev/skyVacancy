class Salary:
    """ Зарплата вакансии"""

    def __init__(self, salary_from: int = 0, salary_to: int = 0, agreement: bool = False):
        self.__from = salary_from
        self.__to = salary_to
        if self.__from == self.__to and self.__from == 0:
            self.__agreement = True
        else:
            self.__agreement = bool(agreement)

    @property
    def max_salary(self):
        """ Если зарплата не по договоренности вернуть максимальную сумму
        По договоренности вернуть 0
        """
        if self.is_agreement():
            return 0
        else:
            salary_list = [self.__from, self.__to]
            return max(salary_list)

    def is_agreement(self):
        """ Зарплата по договоренности """
        return self.__agreement

    def __eq__(self, other):
        """ Зарплаты равны
        Если обе по договоренности
        Если максимальные суммы равны
        """
        if isinstance(other, Salary):
            if self.is_agreement():
                return other.is_agreement()
            if self.max_salary == other.max_salary:
                return True
        return False

    def __lt__(self, other):
        """ Зарплата меньше """
        if isinstance(other, Salary) and not self.is_agreement():
            if self.max_salary < other.max_salary:
                return True
        return False

    def __gt__(self, other):
        """ Зарплата больше """
        if isinstance(other, Salary) and not self.is_agreement():
            if self.max_salary > other.max_salary:
                return True
        return False


class Vacancy:
    """ Описание найденной вакансии"""

    __Vacancies = []

    def __init__(self, title='', salary=Salary(agreement=True), link='', city='', company='', description=''):
        self.__title = title
        self.__salary = salary
        self.__link = link
        self.__city = city
        self.__company = company
        self.__description = description
        Vacancy.__Vacancies.append(self)

    def __eq__(self, other):
        """ Зарплаты равны """
        if isinstance(other, Vacancy):
            return self.__salary == other.__salary
        return False

    def __lt__(self, other):
        """ Зарплата меньше """
        if isinstance(other, Vacancy):
            return self.__salary < other.__salary
        return False

    def __gt__(self, other):
        """ Зарплата больше """
        if isinstance(other, Vacancy):
            return self.__salary > other.__salary
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

    @property
    def link(self):
        """ Ссылка на описание вакансии """
        return self.__link

    @property
    def city(self):
        """ Город """
        return self.__city

    @property
    def company(self):
        """ Наименование компании работодателя """
        return self.__company

    @property
    def description(self):
        """ Полное описание вакансии """
        return self.__description
