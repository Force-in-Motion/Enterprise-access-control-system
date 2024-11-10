from static.processing_data import Processing
from service.data_service import DataService as ds
from utilits.tools.tools import *
from tkinter.messagebox import *


class CreateUser:
    """
    Создает нового сотрудника и определяет зоны доступные ему
    """
    def __init__(self):
        self.__load_data = Processing.get_load_data()

    def add_access_zone(self, name: str, access_zone: str) -> bool:
        """
        Создает нового пользователя и определяет доступные для него зоны
        :param name: Принимает имя пользователя
        :param access_zone: Принимает название зон, доступных пользователю
        :return: bool
        """
        self.__load_data[name] = access_zone.split(',')

        showinfo('Успех', 'Пользователь успешно добавлен')

        return True


    def remove_user(self, name) -> bool:
        """
        Удаляет пользователя из базы данных
        :param name: Принимает имя пользователя
        :return: bool
        """

        if name in self.__load_data:

            del self.__load_data[name]

            showinfo('Успех', 'Пользователь успешно удален')
            return True

        showerror('Ошибка ввода', 'Такого пользователя нет в базе данных')
        return False


    def save(self) -> bool:
        """
        Сохраняет данные в файл
        :return: bool
        """
        ds.write_data_user(self.__load_data)

        showinfo('Успех', 'Данные успешно сохранены')

        print('Successfull')

        return True


    @property
    def load_data(self):
        return self.__load_data









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
        self.__data_employees = ds.read_data_user() if ds.check_file_data_user() else None
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

