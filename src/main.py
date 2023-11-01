from user_interface import UserInterface, ExitException


def main():
    """ Обработка запроса пользователя и вывод информации """
    ''' Сценарии использования
        1. Поиск вакансий
            1. Поиск вакансии и вывод на экран, сохранение неотсортированных данных в файл (JSON)
                Запросить платформу HH SJ или оба
                Запросить ключевое слово (слова если расширенный поиск и где искать: везде, только название, название фирмы)        
        2. Работа с найденными вакансиями
            1. Сортировка найденных вакансий
                Указать параметр сортировки (зарплата, название, фирма)
                Указать количество вакансий  
            2. Сохранение данных в файл
                Выбрать формат и имя файла
                Выбрать параметры выбора вакансий
        
    '''
    interface = UserInterface()
    while True:
        try:
            interface.execute()
        except ExitException:
            break


if __name__ == '__main__':
    main()
