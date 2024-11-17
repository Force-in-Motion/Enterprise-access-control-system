from static.processing_data import Processing
from service.data_service import DataService as ds
from utilits.tools.tools import *
from tkinter.messagebox import *


class User:
    """
    Создает нового сотрудника и определяет зоны доступные ему
    """
    def __init__(self):
        self.__data_users = Processing.get_data_users()


    def add_access_zone(self, name: str, access_zone: str) -> bool:
        """
        Создает нового пользователя и определяет доступные для него зоны
        :param name: Принимает имя пользователя
        :param access_zone: Принимает название зон, доступных пользователю
        :return: bool
        """
        self.__data_users[name] = access_zone.split(',')

        showinfo('Успех', 'Пользователь успешно добавлен')
        return True


    def remove_user(self, name: str) -> bool:
        """
        Удаляет пользователя из базы данных
        :param name: Принимает имя пользователя
        :return: bool
        """
        if name in self.__data_users:

            del self.__data_users[name]

            showinfo('Успех', 'Пользователь успешно удален')
            return True

        showerror('Ошибка ввода', 'Такого пользователя нет в базе данных')
        return False


    def save(self) -> bool:
        """
        Сохраняет данные в файл
        :return: bool
        """
        ds.write_data_user(self.__data_users)

        showinfo('Успех', 'Данные успешно сохранены')

        return True


    @property
    def data_users(self) -> dict:
        return self.__data_users



class DataStorage:
    """
    Управляет данными статистики ( записывает в базу или получает из нее )
    """
    def __init__(self):
        self.__data_log = Processing.get_log()
        self.__data_log['granted'] = []
        self.__data_log['denied'] = []


    def add_granted(self, data) -> None:
        """
        Добавляет в базу статистики данные об успешных авторизациях пользователей
        :param data: Принимает данные в виде строки
        :return: None
        """
        self.__data_log['granted'].append(data)

    def add_denied(self, data) -> None:
        """
        Добавляет в базу статистики данные об не успешных авторизациях пользователей
        :param data: Принимает данные в виде строки
        :return: None
        """
        self.__data_log['denied'].append(data)

    @property
    def granted(self) -> list[str]:
        return self.__data_log['granted']


    @property
    def denied(self) -> list[str]:
        return self.__data_log['denied']


    def save(self) -> None:
        """
        Перезаписывает в базу полученные данные, если файла нет - создает его
        :return: None
        """
        ds.write_data_log(self.__data_log)



class SecuritySystem:
    """
    Управляет авторизацией пользователей и их уровнями доступа
    """
    def __init__(self):
        self.__data_users = Processing.get_load_data()
        self.__common_areas = ds.read_data_common_areas()
        self.__storage = DataStorage()


    def enter_zone(self, name: str, zone: str) -> bool:
        """
        Предоставляет пользователю доступ в систему если он соответствует требованиям, иначе сообщает об отказе в предоставлении доступа
        :param name: Принимает имя пользователя
        :param zone: Принимает название зоны для получения доступа
        :return: bool
        """
        access_zone = self.__data_users[name]
        if zone in self.__common_areas:
            showinfo('Вход разрешен', f'Вы вошли в зону {zone}')
            self.__storage.add_granted(f'Пользователь с именем {name} вошел в зону {zone}')
            return True

        if zone in access_zone:
            showinfo('Вход разрешен', f'Вы вошли в зону {zone}')
            self.__storage.add_granted(f'Пользователь с именем {name} вошел в зону {zone}')
            return True

        showerror('Вход запрещен', f'Вход в зону {zone} вам запрещен')
        self.__storage.add_denied(f'Пользователю с именем {name} отказано в доступе в зону {zone}')
        return False


    @property
    def storage(self):
        return self.__storage




