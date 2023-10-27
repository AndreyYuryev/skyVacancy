import os
from dotenv import load_dotenv


class EnvParameter:
    ''' получение переменных окружения '''

    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.split(current_dir)[0]
        filepath = os.path.join(root_dir, '.env')
        if os.path.exists(filepath):
            load_dotenv(filepath)

    @property
    def superjobapikey(self):
        return os.getenv('SUPERJOB_API_KEY')

    @property
    def headhunterapikey(self):
        return os.getenv('HEADHUNTER_API_KEY')
