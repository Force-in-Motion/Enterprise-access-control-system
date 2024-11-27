from service.process import Processing
from service.service import DataService as ds
from tkinter.messagebox import *


class SecuritySystem:
    """
    Управляет авторизацией пользователей и их уровнями доступа
    """
    def __init__(self, log):
        self.__data_users = Processing.get_data_users()
        self.__common_areas = ds.read_data_common_areas()
        self.__log = log


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
            self.__log.add_granted(f'Пользователь с именем {name} вошел в зону {zone}')
            return True

        if zone in access_zone:
            showinfo('Вход разрешен', f'Вы вошли в зону {zone}')
            self.__log.add_granted(f'Пользователь с именем {name} вошел в зону {zone}')
            return True

        showerror('Вход запрещен', f'Вход в зону {zone} вам запрещен')
        self.__log.add_denied(f'Пользователю с именем {name} отказано в доступе в зону {zone}')
        return False

