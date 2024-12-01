
from service.service import DataService as ds
from tkinter.messagebox import *


class SecuritySystem:
    """
    Управляет авторизацией пользователей и их уровнями доступа
    """
    def __init__(self, log):
        self.__data_users = ds.get_data_users()
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
            self.__log.add_statistic('granted', f'Пользователь с именем {name} вошел в зону {zone}')
            return True

        if zone in access_zone:
            showinfo('Вход разрешен', f'Вы вошли в зону {zone}')
            self.__log.add_statistic('granted', f'Пользователь с именем {name} вошел в зону {zone}')
            return True

        showerror('Вход запрещен', f'Вход в зону {zone} вам запрещен')
        self.__log.add_statistic('denied', f'Пользователю с именем {name} отказано в доступе в зону {zone}')
        return False


    def add_common_areas(self, zone):

        self.__common_areas["ca"].append(zone)

        showinfo('Добавлена зона', f'Зона {zone} успешно добавлена в список общедоступных')

        self.__log.add_statistic('add_zone', f'Зона {zone} добавлена в список общедоступных')


    def del_common_areas(self, zone):

        self.__common_areas["ca"].remove(zone)

        showinfo('Удалена зона', f'Зона {zone} успешно удалена из списка общедоступных')

        self.__log.add_statistic('del_zone', f'Зона {zone} удалена из списка общедоступных')


    def save(self):
        """
        Сохраняет данные в файл
        :return: bool
        """
        self.__log.save()

        ds.write_data_common_areas(self.__common_areas)

        showinfo('Успех', 'Данные успешно сохранены')

        return True


    @property
    def common_areas(self):
        return self.__common_areas