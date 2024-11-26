import customtkinter as ctk
from settings.config_statistic import *

class Scroll(ctk.CTkScrollableFrame):
    def __init__(self, main_page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_page = main_page
        self.__text = None
        self.__config_text()


    def __config_text(self) -> None:
        self.__text = ctk.CTkLabel(self, text='qqqqqqqqqqqq')
        self.__text.place(relx=0.1, rely=0.1)



class Statistic(ctk.CTkToplevel):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__scroll = None
        self.__config_scroll()
        self.__config_window()


    def __config_window(self):
        self.geometry(geometry)
        self.title(title)
        self.resizable(rzb_wh, rzb_ht)


    def __config_scroll(self):
        self.__scroll = Scroll(self, width=s_wh, height=s_ht)