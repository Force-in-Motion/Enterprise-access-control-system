
from service.data_service import DataService as ds
from utilits.tools.tools import *
from tkinter.messagebox import *


class User:
    """
    Создает нового сотрудника и определяет зоны доступные ему или добавляет доступные зоны ранее созданному сотруднику
    """
    def __init__(self, name: str, access_zone: str):
        self.__name = name
        self.__access_zone = access_zone.split(', ')
        self.__load_data = ds.read_data_employees() if ds.check_file_data_employee() else {}

    def add_access_zone(self) -> bool:
        """
        Добавляет доступную для сотрудника зону
        :param data: принимает название зоны
        :return: bool
        """
        self.__load_data[self.__name] = self.__access_zone
        showinfo('Успех', 'Пользователь успешно добавлен')

        return True


    def save(self) -> bool:
        """
        Сохраняет данные в файл
        :return: bool
        """

        if ds.write_data_employees(self.__load_data):
            showinfo('Успех', 'Пользователь успешно добавлен')
        return True









class DataStorage:

    def __init__(self):
        self.__data_log = ds.read_data_log() if ds.check_file_data_log() else {}


    def get_access_granted(self) -> list[str]:
        return self.__data_log['granted']


    def get_access_denied(self) -> list[str]:
        return self.__data_log['denied']

    def save(self) -> bool:
        return True if ds.write_data_log(self.__data_log) else False




class SecuritySystem:
    def __init__(self, name: str, zone: str):
        self.__name = name
        self.__zone = zone
        self.__data_employees = ds.read_data_employees() if ds.check_file_data_employee() else None
        self.__data_common_areas = ds.read_data_common_areas()
        self.__access_zone = self.__data_employees[self.__name]
        self.__storage = DataStorage()
        self.__granted = self.__storage.get_access_granted()
        self.__denied = self.__storage.get_access_denied()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def zone(self) -> str:
        return self.__zone

    @property
    def data_employees(self) -> dict:
        return self.__data_employees

    @property
    def access_zone(self) -> dict:
        return self.__access_zone

    @property
    def common_areas(self) -> str:
        return self.__data_common_areas['ca']

    @property
    def granted(self):
        return self.__granted

    @property
    def denied(self):
        return self.__denied



    # @validation_enter(name, zone, access_zone, common_areas, data_employees)
    # @validation_log(name, granted, denied)
    def enter_zone(self) -> bool:
        """
        Проверяет наличие принятой зоны доступа
        :param employee:
        :param zone:
        :return:
        """
        showinfo('Confirm access', 'Enter successful')

        return True

