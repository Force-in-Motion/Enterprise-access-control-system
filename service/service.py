import json
import os.path


class DataService:

    @staticmethod
    def create_folder() -> None:
        """
        Проверяет наличие папки по указанному адресу, если папка отсутствует то создает ее
        """
        if not os.path.isdir(path_dir):
            os.mkdir(path_dir)


    @staticmethod
    def check_file_data_log() -> bool:
        """
        Проверяет наличие файла по указанному пути, в данном случае в папке
        :return: True или False
        """
        file = path_dir + r'\data_log.json'

        if os.path.isfile(file):
            return True
        else:
            return False


    @staticmethod
    def check_file_data_user() -> bool:
        """
        Проверяет наличие файла по указанному пути, в данном случае в папке
        :return: True или False
        """
        file = path_dir + r'\data_user.json'

        if os.path.isfile(file):
            return True
        else:
            return False


    @staticmethod
    def get_common_areas_path() -> str:
        """
        Создает относительный путь к файлу common_areas
        :return: Путь в виде строки
        """
        current_dir = os.path.dirname(__file__)
        common_areas_path = os.path.join(current_dir, '..', 'storage', 'common_areas.json')

        return os.path.abspath(common_areas_path)


    @staticmethod
    def read_data_user():
        """
        Считывает из файла данные пользователя
        :return: Возвращает данные
        """
        with open(path_dir + r'\data_user.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data


    @staticmethod
    def write_data_user(*args):
        """
        Записывает в файл данные пользователя
        :param args: Принимает любое количество позиционных параметров ( данных для записи )
        :return: bool
        """
        with open(path_dir + r'\data_user.json', 'w', encoding='utf-8') as f:
            json.dump(*args, f, ensure_ascii=False, indent=4)
            return True


    @staticmethod
    def read_data_log():
        """
        Считывает из файла данные о попытках авторизации пользователей
        :return: Возвращает данные
        """
        with open(path_dir + r'\data_log.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data


    @staticmethod
    def write_data_log(*args):
        """
        Записывает в файл данные о попытках авторизации пользователей
        :param args: Принимает любое количество позиционных параметров ( данных для записи )
        :return: bool
        """
        with open(path_dir + r'\data_log.json', 'w', encoding='utf-8') as f:
            json.dump(*args, f, ensure_ascii=False, indent=4)
            return True


    @staticmethod
    def read_data_common_areas():
        """
        Считывает из файла данные об общих зонах доступа, открытых для всех пользователей
        :return: Возвращает данные
        """
        with open(path_common_areas , 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data


    @staticmethod
    def get_data_users():
        DataService.create_folder()
        return DataService.read_data_user() if DataService.check_file_data_user() else {}


    @staticmethod
    def get_log():
        DataService.create_folder()
        return DataService.read_data_log() if DataService.check_file_data_log() else {}


path_dir = os.environ.get('LOCALAPPDATA') + r'\Enterprise Control'

path_common_areas = DataService.get_common_areas_path()