import json
import os

path_dir = os.environ.get('LOCALAPPDATA') + r'\Enterprise Control'

path_common_areas = r'..\utilits\storage\common_areas.json'


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
        Проверяет наличие файла txt по указанному пути, в данном случае в папке
        :return: True или False
        """
        file = path_dir + r'\data_log.json'

        if os.path.isfile(file):
            return True
        else:
            return False


    @staticmethod
    def check_file_data_employee() -> bool:
        """
        Проверяет наличие файла txt по указанному пути, в данном случае в папке
        :return: True или False
        """
        file = path_dir + r'\data_employee.json'

        if os.path.isfile(file):
            return True
        else:
            return False

    @staticmethod
    def read_data_employees():
        with open(path_dir + r'\data_user.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data

    @staticmethod
    def write_data_employees(data):
        with open(path_dir + r'\data_user.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            return True


    @staticmethod
    def read_data_log():
        with open(path_dir + r'\data_log.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data


    @staticmethod
    def write_data_log(data):
        with open(path_dir + r'\data_employee.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            return True


    @staticmethod
    def read_data_common_areas():
        with open(path_dir + r'\common_areas.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data

