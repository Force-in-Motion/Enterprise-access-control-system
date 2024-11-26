

class HandlerMenu:
    def __init__(self, main_page, data_combobox):

        self.__data_combobox = data_combobox
        self.__main_page = main_page

    def create_page(self):
        from src.view.add_user import CreateUser

        if self.__data_combobox == 'Добавить нового пользователя':

            create_user = CreateUser(self.__main_page)
