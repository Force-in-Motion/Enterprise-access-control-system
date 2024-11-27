

class HandlerMenu:
    def __init__(self, main_page):
        self.__main_page = main_page
        self.__create_user = None
        self.__statistic = None

    def open_add_user_page(self):
        from src.view.add_user import CreateUser

        self.__create_user = CreateUser(self.__main_page)


    def open_statistic_page(self, val):
        from src.view.statistic import Statistic

        self.__statistic = Statistic(self.__main_page)

        self.__statistic.scroll.text = val
