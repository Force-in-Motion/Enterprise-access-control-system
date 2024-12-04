from service.service import DataService as ds
from service.process import Processing


class HandlerMenu:
    """
    Класс работающий с меню кнопок главной страницы и открывающий другие окна при нажатии на кнопки
    """
    def __init__(self):
        self.__create_user = None
        self.__del_user = None
        self.__statistic = None


    def open_add_user_page(self, main_page) -> None:
        """
        Открывает окно добавления нового пользователя
        :param main_page: Принимает окно, являющееся родительским для открываемого окна
        :return: None
        """
        from src.view.add_user import CreateUser

        self.__create_user = CreateUser(main_page)


    def open_del_user_page(self, main_page) -> None:
        """
        Открывает окно удаления пользователя
        :param main_page: Принимает окно, являющееся родительским для открываемого окна
        :return: None
        """
        from src.view.del_user import DelUser

        self.__del_user = DelUser(main_page)


    def open_edit_common_areas(self, main_page) -> None:
        """
        Открывает окно редактирования списка общедоступных зон
        :param main_page: Принимает окно, являющееся родительским для открываемого окна
        :return: None
        """
        from src.view.edit_common_areas import EditCommonAreas

        self.__del_user = EditCommonAreas(main_page)


    def open_statistic_page(self, main_page) -> None:
        """
        Открывает окно статистики и выводит на него информацию из файла и из временной памяти
        :param main_page: Принимает окно, являющееся родительским для открываемого окна
        :return: None
        """
        from src.view.statistic import Statistic

        self.__statistic = Statistic(main_page)

        data = ds.get_log()

        value = Processing.converts_data_to_str(data)

        self.__statistic.scroll.set_label_text(value)
