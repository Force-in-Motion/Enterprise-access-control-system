from __future__ import annotations

import customtkinter as ctk
from src.controller.controller import UserController
from service.process import Processing
from settings.config_add_user import *


class CreateUserFrame(ctk.CTkFrame):
    """
    Класс- контейнер, содержащий в себе все остальные виджеты и элементы страницы
    """
    def __init__(self, main_page: CreateUser, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_page = main_page
        self.__main_label = None
        self.__input_name = None
        self.__input_zone = None
        self.__config_label()
        self.__config_inputs()
        self.__config_menu_btn()


    def __config_label(self) -> None:
        """
        Формирует текстовые элементы страницы
        :return: None
        """
        self.__add_user = ctk.CTkLabel(self, text=au_tt, text_color=au_ttc, font=au_ft)
        self.__add_user.place(relx=0.17, rely=0.12)


    def __config_inputs(self) -> None:
        """
        Формирует поля ввода данных пользователя
        :return: None
        """
        self.__input_name = ctk.CTkEntry(self, width=i_wh, height=i_ht, placeholder_text=in_phtt_cu, text_color=i_tc,
                                         placeholder_text_color=i_phttc, fg_color=i_fgc, font=i_ft)
        self.__input_name.place(relx=0.18, rely=0.25)

        self.__input_zone = ctk.CTkEntry(self, width=i_wh, height=i_ht, placeholder_text=iz_phtt_cu, text_color=i_tc,
                                         placeholder_text_color=i_phttc, fg_color=i_fgc, font=i_ft)
        self.__input_zone.place(relx=0.18, rely=0.37)


    def __config_menu_btn(self) -> None:
        """
        Формирует меню кнопок, управляющее возможностями страницы
        :return: None
        """
        self.__add_btn = ctk.CTkButton(self, width=ad_wh, height=ad_ht, text=ad_tt, font=ad_ft,
                                         text_color=ad_ttc, fg_color=ad_fgc)
        self.__add_btn.place(relx=0.18, rely=0.55)
        self.__add_btn.configure(command=self.__main_page.on_add_click)

        self.__cancel_btn = ctk.CTkButton(self, width=c_wh, height=c_ht, text=c_tt, font=c_ft,
                                        text_color=c_ttc, fg_color=c_fgc)
        self.__cancel_btn.place(relx=0.59, rely=0.55)
        self.__cancel_btn.configure(command=self.__main_page.on_cancel_click)

        self.__save_btn = ctk.CTkButton(self, width=s_wh, height=s_ht, text=s_tt, font=s_ft,
                                          text_color=s_ttc, fg_color=s_fgc)
        self.__save_btn.place(relx=0.22, rely=0.75)
        self.__save_btn.configure(command=self.__main_page.on_save_click)


    @property
    def name(self) -> ctk.CTkEntry:
        """
        Создает объект проперти, позволяющий напрямую взаимодействовать с данными пользователя
        :return: ctk.CTkEntry
        """
        return self.__input_name


    @property
    def zone(self) -> ctk.CTkEntry:
        """
        Создает объект проперти, позволяющий напрямую взаимодействовать с данными пользователя
        :return: ctk.CTkEntry
        """
        return self.__input_zone



class CreateUser(ctk.CTkToplevel):
    """
    Мэйн класс страницы, содержащий ключевые методы, отвечающие за функционал страницы
    """
    def __init__(self, main_window):
        super().__init__()
        self.__main_window = main_window
        self.__main_frame = None
        self.__controller = UserController()
        self.protocol("WM_DELETE_WINDOW", Processing.on_close)
        self.__config_window()
        self.__config_frame()


    def __config_window(self) -> None:
        """
        Формирует параметры и стили главной страницы модуля
        :return: None
        """
        self.geometry(gt)
        self.title(ttl)
        self.resizable(rz_wh, rz_ht)


    def __config_frame(self) -> None:
        """
        Формирует мэйн фрейм главной страницы, содержащий остальные элементы и виджеты страницы
        :return: None
        """
        self.__main_frame = CreateUserFrame(self, master=self, width=fr_wh, height=fr_ht)
        self.__main_frame.pack()
        self.__main_frame.pack_propagate(False)


    def on_add_click(self) -> None:
        """
        При нажатии на кнопку вызывает метод соответствующего контроллера и передает ему необходимые данные для проверки и передачи в модуль
        :return: None
        """
        self.__controller.add_user_button_click_handler(self.__main_frame.name.get(), self.__main_frame.zone.get())
        self.__main_frame.name.delete(0, ctk.END), self.__main_frame.zone.delete(0, ctk.END)


    def on_save_click(self) -> None:
        """
        При нажатии на кнопку вызывает метод соответствующего контроллера
        :return: None
        """
        self.__controller.save_user_data_button_click_handler()


    def on_cancel_click(self) -> None:
        """
        При нажатии на кнопку вызывает метод соответствующего контроллера
        :return: None
        """
        self.__main_window.deiconify()

        self.destroy()


