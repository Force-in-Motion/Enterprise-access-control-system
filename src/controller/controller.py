from service.process import Processing
from src.model.authorization import SecuritySystem
from src.model.log import LogStorage
from src.model.users import User
from src.model.menu import HandlerMenu
from tkinter.messagebox import *


class UserController:
    """
    Класс контроллер, обрабатывает полученные данные, проверяет соответствие их типов ожидаемым
    И вызывает соответствующие методы модели, передавая им проверенные данные
    """

    def __init__(self):
        self.__log = LogStorage()
        self.__user = User(self.__log)
        self.__old_data = self.__user.data_users.copy()

    def add_button_click_handler(self, name: str, access_zone: str) -> None:
        """
        Выполняет проверки получаемых данных, а так же дублирование имен, вызывает метод модели и передает проверенные данные для добавления пользователя
        :param name: Принимает имя пользователя в виде строки
        :param access_zone: Принимает зону или список зон в виде строки через запятую
        :return: None
        """
        assert name != '' and access_zone != '', showerror('Ошибка ввода', 'Пустая строка не может быть принята')

        assert name not in self.__user.data_users, showerror('Ошибка ввода', 'Пользователь с таким именем уже существует')

        self.__user.add_access_zone(name, access_zone)


    def del_button_click_handler(self, name: str) -> None:
        """
        Выполняет проверки получаемых данных, вызывает метод модели и передает проверенные данные для удаления пользователя
        :param name: Принимает имя пользователя в виде строки
        :return: None
        """
        assert name != '', showerror('Ошибка ввода', 'Пустая строка не может быть принята')

        self.__user.remove_user(name)


    def save_button_click_handler(self) -> None:
        """
        Выполняет проверки данных, если в данные вносились изменения вызывает метод модели, сохраняющий изменения в файле
        :return:
        """
        assert self.__old_data != self.__user.data_users, showerror('Ошибка данных', 'Вы не внесли изменения, сохранять нечего')

        self.__user.save()

        self.__old_data = self.__user.data_users.copy()



class MainPageController:
    """
    Класс контроллер, обрабатывает полученные данные, проверяет соответствие их типов ожидаемым
    И вызывает соответствующие методы модели, передавая им проверенные данные
    """

    def __init__(self, main_page):
        self._main_page = main_page
        self.__log = LogStorage()
        self.__security = SecuritySystem(self.__log)
        self.__menu = HandlerMenu( self._main_page)



    def enter_button_click_handler(self, name: str, zone: str) -> None:
        """
        Выполняет проверки получаемых данных, вызывает метод модели и передает проверенные данные для авторизации пользователя
        :param name: Принимает имя пользователя в виде строки
        :param zone: Принимает зону для входа пользователя в виде строки
        :return:
        """
        data_users = Processing.get_data_users()

        assert name != '' and zone != '', showerror('Ошибка ввода', 'Пустая строка не может быть принята')

        assert name in data_users, showerror('Ошибка ввода','Пользователь с таким именем отсутствует в базе')

        self.__security.enter_zone(name, zone)


    def confirm_btn_click_handler(self, data_combobox: str):

        assert data_combobox != '', showerror('Ошибка ввода', 'Пустая строка не может быть принята')

        if data_combobox == 'Добавить нового пользователя':

            self.__menu.open_add_user_page()


    def statistic_btn_click_handler(self, val):

        self.__menu.open_statistic_page(val)


    def exit_btn_click_handler(self):
        """
        Обрабатывает клик по кнопке выхода со страницы, вызывает метод модели, сохраняющий данные об авторизации пользователей в базе статистики
        :return:
        """
        self.__log.save()
