
from service.service import DataService as ds
from tkinter.messagebox import *


class User:
    """
    Создает нового сотрудника и определяет зоны доступные ему
    """
    def __init__(self, log):
        self.__log = log
        self.__data_users = ds.get_data_users()


    def add_access_zone(self, name: str, access_zone: str) -> bool:
        """
        Создает нового пользователя и определяет доступные для него зоны
        :param name: Принимает имя пользователя
        :param access_zone: Принимает название зон, доступных пользователю
        :return: bool
        """
        self.__data_users[name] = access_zone.split(',')

        self.__log.add_statistic('add_user', f'Добавлен пользователь с именем {name}. Доступные зоны: {access_zone}')

        showinfo('Успех', 'Пользователь успешно добавлен')

        return True


    def del_user(self, name: str) -> bool:
        """
        Удаляет пользователя из базы данных
        :param name: Принимает имя пользователя
        :return: bool
        """
        if name in self.__data_users:

            del self.__data_users[name]

            self.__log.add_statistic('del_user', f'Пользователь с именем {name} удален из базы данных')

            showinfo('Успех', 'Пользователь успешно удален')
            return True

        showerror('Ошибка ввода', 'Такого пользователя нет в базе данных')
        return False


    def save(self) -> bool:
        """
        Сохраняет данные в файл
        :return: bool
        """
        self.__log.save()

        ds.write_data_user(self.__data_users)

        showinfo('Успех', 'Данные успешно сохранены')

        return True


    @property
    def data_users(self) -> dict:
        return self.__data_users
