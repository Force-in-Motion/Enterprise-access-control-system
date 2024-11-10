
from src.model.model import *
from tkinter.messagebox import *


class UserController:
    """
    Класс контроллер, обрабатывает полученные данные, проверяет соответствие их типов ожидаемым
    И вызывает соответствующие методы модели, передавая им проверенные данные
    """

    def __init__(self):
        self.__user = CreateUser()
        self.__old_data = self.__user.load_data

    def add_button_click_handler(self, name: str, access_zone: str) -> None:
        """
        Выполняет проверки получаемых данных, а так же дублирование имен, вызывает метод модели и передает проверенные данные для добавления пользователя
        :param name: Принимает имя пользователя в виде строки
        :param access_zone: Принимает зону или список зон в виде строки через запятую
        :return: None
        """
        assert name != '' and access_zone != '', showerror('Ошибка ввода', 'Пустая строка не может быть принята')

        assert name not in self.__user.load_data, showerror('Ошибка ввода', 'Пользователь с таким именем уже существует')

        self.__user.add_access_zone(name, access_zone)


    def del_button_click_handler(self, name):
        """
        Выполняет проверки получаемых данных, вызывает метод модели и передает проверенные данные для удаления пользователя
        :param name: Принимает имя пользователя в виде строки
        :return: None
        """
        assert name != '', showerror('Ошибка ввода', 'Пустая строка не может быть принята')

        self.__user.remove_user(name)






    def save_button_click_handler(self):

        # assert self.__old_data != self.__user.load_data, showerror('Ошибка данных', 'Вы не внесли изменения, сохранять нечего')



        self.__user.save()
