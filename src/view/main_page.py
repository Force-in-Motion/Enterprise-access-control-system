from __future__ import annotations

from PIL import Image
import customtkinter as ctk
from src.controller.controller import SecurityController
from settings.config_main_page import *


class MainFrame(ctk.CTkFrame):
    """
    Класс- контейнер, содержащий в себе все остальные виджеты и элементы страницы
    """
    def __init__(self, main_page: MainPage, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_page = main_page
        self.__main_label = None
        self.__input_name = None
        self.__input_zone = None
        self.__combobox = None
        self.__config_label()
        self.__config_inputs()
        self.__config_menu_btn()
        self.__config_combobox()


    def __config_label(self) -> None:
        """
        Формирует текстовые элементы страницы
        :return: None
        """
        self.__main_label = ctk.CTkLabel(self, text=ml_tt, text_color=ml_ttc, font=ml_ft)
        self.__main_label.place(relx=0.2, rely=0.1)

        self.__strip_label = ctk.CTkLabel(self, text=sl_tt, text_color=sl_tc, font=sl_ft)
        self.__strip_label.place(relx=0.001, rely=0.55)


    def __config_inputs(self) -> None:
        """
        Формирует поля ввода данных пользователя
        :return: None
        """
        self.__input_name = ctk.CTkEntry(self, width=id_wh, height=id_ht, placeholder_text=in_phtt, text_color=id_tc,
                                         placeholder_text_color=id_phttc, fg_color=id_fgc , font=id_ft)
        self.__input_name.place(relx=0.18, rely=0.22)

        self.__input_zone = ctk.CTkEntry(self, width=id_wh, height=id_ht, placeholder_text=iz_phtt, text_color=id_tc,
                                         placeholder_text_color=id_phttc, fg_color=id_fgc , font=id_ft)
        self.__input_zone.place(relx=0.18, rely=0.32)


    def __config_combobox(self) -> None:
        """
        Формирует комбобокс, позволяющий пользователю выбирать элементы меню
        :return: None
        """
        self.__combobox = ctk.CTkComboBox(self, width=cb_wh, height=cb_ht, text_color=cb_tc, fg_color=cb_fgc,font=cb_ft,
                              dropdown_fg_color=cb_dfgc, dropdown_text_color=cb_dtc, dropdown_font=cb_df, justify=cb_jf)
        self.__combobox.set(var)
        self.__combobox.configure(values=cb_values)
        self.__combobox.place(relx=0.2, rely=0.7)


    def __config_menu_btn(self) -> None:
        """
        Формирует меню кнопок, управляющее возможностями страницы
        :return: None
        """
        self.__enter_btn = ctk.CTkButton(self, width=en_wh, height=en_ht, text=en_tt, font=en_ft,
                                       text_color=en_ttc, fg_color=en_fgc)
        self.__enter_btn.place(relx=0.18, rely=0.45)
        self.__enter_btn.configure(command=self.__main_page.on_enter_click)

        self.__exit_btn = ctk.CTkButton(self, width=ex_wh, height=ex_ht, text=ex_tt, font=ex_ft,
                                          text_color=ex_ttc, fg_color=ex_fgc)
        self.__exit_btn.place(relx=0.59, rely=0.45)
        self.__exit_btn.configure(command=self.__main_page.on_exit_click)

        self.__confirm_btn = ctk.CTkButton(self, width=cr_wh, height=cr_ht, text=cr_tt, font=cr_ft,
                                          text_color=cr_ttc, fg_color=cr_fgc)
        self.__confirm_btn.place(relx=0.3, rely=0.82)
        self.__confirm_btn.configure(command=self.__main_page.on_confirm_click)

        self.__img_btn = ctk.CTkImage(light_image=Image.open(path_img), size=size_img)
        self.__statistic_btn = ctk.CTkButton(self, image=self.__img_btn, width=sb_wh, height=sb_ht, text=sb_tt, corner_radius=0,
                                             hover_color='#2E2A2A', fg_color='#2E2A2A')
        self.__statistic_btn.place(relx=0.87, rely=0.87)
        self.__statistic_btn.configure(command=self.__main_page.on_statistic_click)


    @property
    def menu(self):
        """
        Создает объект проперти, позволяющий напрямую взаимодействовать с данными пользователя
        :return: ctk.CTkComboBox
        """
        return self.__combobox


    @property
    def name(self):
        """
        Создает объект проперти, позволяющий напрямую взаимодействовать с данными пользователя
        :return: ctk.CTkEntry
        """
        return self.__input_name


    @property
    def zone(self):
        """
        Создает объект проперти, позволяющий напрямую взаимодействовать с данными пользователя
        :return: ctk.CTkEntry
        """
        return self.__input_zone



class MainPage(ctk.CTk):
    """
    Мэйн класс страницы, содержащий ключевые методы, отвечающие за функционал страницы
    """
    def __init__(self):
        super().__init__()
        self.__controller = SecurityController()
        self.protocol("WM_DELETE_WINDOW", self.on_exit_click)
        self.__config_window()
        self.__config_frame()


    def __config_window(self) -> None:
        """
        Формирует параметры и стили главной страницы модуля
        :return: None
        """
        self.geometry(geometry)
        self.title(title)
        self.resizable(rzb_wh, rzb_ht)


    def __config_frame(self) -> None:
        """
        Формирует мэйн фрейм главной страницы, содержащий остальные элементы и виджеты страницы
        :return: None
        """
        self.__main_frame = MainFrame(self, master=self, width=f_wh, height=f_ht)
        self.__main_frame.pack()
        self.__main_frame.pack_propagate(False)


    def on_enter_click(self) -> None:
        """
        При нажатии на кнопку вызывает метод соответствующего контроллера и передает ему необходимые данные для проверки и передачи в модуль
        :return: None
        """
        self.__controller.enter_button_click_handler(self.__main_frame.name.get(), self.__main_frame.zone.get())
        self.__main_frame.name.delete(0, ctk.END), self.__main_frame.zone.delete(0, ctk.END)


    def on_exit_click(self) -> None:
        """
        При нажатии на кнопку вызывает метод соответствующего контроллера
        :return: None
        """
        self.__controller.exit_btn_click_handler()
        self.destroy()


    def on_confirm_click(self) -> None:
        """
        При нажатии на кнопку вызывает метод соответствующего контроллера и передает ему необходимые данные для проверки и передачи в модуль
        :return: None
        """
        self.__controller.confirm_btn_click_handler(self.__main_frame.menu.get(), self)
        self.withdraw()


    def on_statistic_click(self) -> None:
        """
        При нажатии на кнопку вызывает метод соответствующего контроллера и передает ему необходимые данные для его работы
        :return: None
        """
        self.__controller.statistic_btn_click_handler(self)
        self.withdraw()


    @classmethod
    def run(cls):
        """
        Запускает главное окно приложения
        """
        page = cls()
        page.lift()
        page.attributes('-topmost', True)
        page.mainloop()

