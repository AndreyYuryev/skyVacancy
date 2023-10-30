class RequestParameter:
    """ Параметры поиска вакансии """

    def __init__(self, count=100, page=0, archive=False, search=[]):
        self.__count = count
        self.__page = page
        self.__archive = archive
        self.__search = search

    @property
    def count(self):
        """ Количество на одной странице """
        return self.__count

    @property
    def page(self):
        """ Количество страниц """
        return self.__page

    @property
    def archive(self):
        """ Смотреть архив """
        return self.__archive

    @property
    def search(self):
        """ Список ключевый слов """
        return self.__search
