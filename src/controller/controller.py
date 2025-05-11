from service.service import DataService as ds
from src.model.authorization import SecuritySystem
from src.model.log import LogStorage
from src.model.users import User
from src.model.menu import HandlerMenu
from tkinter.messagebox import *


LOG = LogStorage()

class UserController:
    """
    Класс контроллер, обрабатывает полученные данные, проверяет соответствие их типов ожидаемым
    И вызывает соответствующие методы модели, передавая им проверенные данные
    """
    def __init__(self):
        self.__user = User(LOG)
        self.__old_data = self.__user.data_users.copy()


    def add_user_button_click_handler(self, name: str, access_zone: str) -> None:
        """
        Выполняет проверки получаемых данных, а так же дублирование имен, вызывает метод модели и передает проверенные данные для добавления пользователя
        :param name: Принимает имя пользователя в виде строки
        :param access_zone: Принимает зону или список зон в виде строки через запятую
        :return: None
        """
        assert name != '' and access_zone != '', showerror('Ошибка ввода', 'Пустая строка не может быть принята')

        assert name not in self.__user.data_users, showerror('Ошибка ввода', 'Пользователь с таким именем уже существует')

        self.__user.add_access_zone(name, access_zone)


    def del_user_button_click_handler(self, name: str) -> None:
        """
        Выполняет проверки получаемых данных, вызывает метод модели и передает проверенные данные для удаления пользователя
        :param name: Принимает имя пользователя в виде строки
        :return: None
        """
        assert name != '', showerror('Ошибка ввода', 'Пустая строка не может быть принята')

        self.__user.del_user(name)


    def save_user_data_button_click_handler(self) -> None:
        """
        Выполняет проверки данных, если в данные вносились изменения вызывает метод модели, сохраняющий изменения в файле
        :return:
        """
        assert self.__old_data != self.__user.data_users, showerror('Ошибка данных', 'Вы не внесли изменения, сохранять нечего')

        self.__user.save()

        self.__old_data = self.__user.data_users.copy()




class SecurityController:
    """
    Класс контроллер, обрабатывает полученные данные, проверяет соответствие их типов ожидаемым
    И вызывает соответствующие методы модели, передавая им проверенные данные
    """

    def __init__(self):
        self.__security = SecuritySystem(LOG)
        self.__menu = HandlerMenu()


    def enter_button_click_handler(self, name: str, zone: str) -> None:
        """
        Выполняет проверки получаемых данных, вызывает метод модели и передает проверенные данные для авторизации пользователя
        :param name: Принимает имя пользователя в виде строки
        :param zone: Принимает зону для входа пользователя в виде строки
        :return:
        """
        data_users = ds.get_data_users()

        assert name != '' and zone != '', showerror('Ошибка ввода', 'Пустая строка не может быть принята')

        assert name in data_users, showerror('Ошибка ввода','Пользователь с таким именем отсутствует в базе')

        self.__security.enter_zone(name, zone, data_users)


    def confirm_btn_click_handler(self, data_combobox: str, main_page) -> None:
        """
        Обрабатывает клик по кнопке подтверждения, в зависимости от того какие данные вернет комбобокс, переадресовывает вызов метода
        :param data_combobox: Данные комбобокса
        :param main_page: Страница, которая является родительской для открываемого окна
        :return: None
        """
        assert data_combobox != '', showerror('Ошибка ввода', 'Пустая строка не может быть принята')

        if data_combobox == 'Добавить нового пользователя':
            self.__menu.open_add_user_page(main_page)

        if data_combobox == 'Удалить пользователя':
            self.__menu.open_del_user_page(main_page)

        if data_combobox == 'Редактирование зон общего доступа':
            self.__menu.open_edit_common_areas(main_page)


    def statistic_btn_click_handler(self, main_page) -> None:
        """
        Обращаясь к нужному объекту вызывает его метод, открывающий окно статистики
        :param main_page: Страница, которая является родительской для открываемого окна
        :return: None
        """
        self.__menu.open_statistic_page(main_page)


    def add_common_areas_button_click_handler(self, zone) -> None:
        """
        Проверяет полученные данные, обращаясь к нужному объекту вызывает его метод, добавляющий общедоступную зону
        :return: None
        """
        assert zone != '', showerror('Ошибка ввода', 'Пустая строка не может быть принята')

        assert zone not in self.__security.common_areas["ca"], showerror('Ошибка ввода', 'Такая зона уже есть в списке')

        self.__security.add_common_areas(zone)


    def del_common_areas_button_click_handler(self, zone) -> None:
        """
        Проверяет полученные данные, обращаясь к нужному объекту вызывает его метод, удаляющий общедоступную зону
        :return: None
        """
        assert zone != '', showerror('Ошибка ввода', 'Пустая строка не может быть принята')

        assert zone in self.__security.common_areas["ca"], showerror('Ошибка ввода', 'Невозможно удалить, такой зоны нет в списке')

        self.__security.del_common_areas(zone)


    def save_common_areas_button_click_handler(self) -> None:
        """
        Обращаясь к нужному объекту вызывает его метод, записывающий изменения общедоступных зон в файл и в файл статистики
        :return: None
        """
        self.__security.save_common_areas()


    def exit_btn_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке выхода со страницы, вызывает метод модели, сохраняющий данные об авторизации пользователей в базе статистики
        :return:
        """
        LOG.save()