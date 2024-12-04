import customtkinter as ctk

from service.process import Processing
from settings.config_statistic import *




class Scroll(ctk.CTkScrollableFrame):
    """
    Класс- контейнер, содержащий в себе статистику в виде текста
    """
    def __init__(self, main_page, *args, **kwargs):
        super().__init__(main_page, *args, **kwargs)
        self.__main_page = main_page
        self.__label_text = None
        self.__config_text()


    def __config_text(self) -> None:
        """
        Формирует текстовые элементы страницы
        :return: None
        """
        self.__label_text = ctk.CTkLabel(self, text='', text_color=s_ltc, font=s_lft, justify=s_jf)
        self.__label_text.grid( padx=(10, 0), pady=10)

    def set_label_text(self, value) -> None:
        """
        Назначает текстовому элементу страницы новое значение
        :return: None
        """
        self.__label_text.configure(text=value)


class Statistic(ctk.CTkToplevel):
    """
    Мэйн класс страницы, содержащий ключевые методы, отвечающие за функционал страницы
    """
    def __init__(self, main_window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window
        self.__scroll = None
        self.protocol("WM_DELETE_WINDOW", Processing.on_close)
        self.__config_scroll()
        self.__config_window()
        self.__config_btn()


    def __config_window(self) -> None:
        """
        Формирует параметры и стили главной страницы модуля
        :return: None
        """
        self.geometry(geometry)
        self.title(title)
        self.resizable(rzb_wh, rzb_ht)


    def __config_scroll(self) -> None:
        """
        Формирует скролл фрейм страницы статистики, содержащий остальные элементы и виджеты страницы
        :return: None
        """
        self.__scroll = Scroll(self, width=s_wh, height=s_ht, fg_color=s_fgc)
        self.__scroll.pack()


    def __config_btn(self) -> None:
        """
        Формирует меню кнопок, управляющее возможностями страницы
        :return: None
        """
        self.__cancel_btn = ctk.CTkButton(self, width=250, height=40, fg_color=cb_fgc, text_color=cb_ttc, text=cb_tt, font=cb_ft)
        self.__cancel_btn.place(relx=0.32, rely=0.85)
        self.__cancel_btn.configure(command=self.on_cancel_click)


    def on_cancel_click(self) -> None:
        """
        При нажатии на кнопку вызывает метод соответствующего контроллера
        :return: None
        """
        self.__main_window.deiconify()
        self.destroy()


    @property
    def scroll(self):
        """
         Создает объект проперти, позволяющий напрямую взаимодействовать с скролл фреймом
         :return: ctk.CTkEntry
         """
        return self.__scroll