from __future__ import annotations

import customtkinter as ctk
from src.view.add_user import GetDataUser
from src.controller.controller import MainPageController
from src.view.config_view import *


class MainFrame(ctk.CTkFrame):

    def __init__(self, main_page: MainPage, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_page = main_page
        self.__main_label = None
        self.__input_name = None
        self.__input_zone = None
        self.__config_label()
        self.__config_inputs()
        self.__config_menu_btn()


    def __config_label(self):
        self.__main_label = ctk.CTkLabel(self, text=ml_tt, text_color=ml_ttc, font=ml_ft)
        self.__main_label.place(relx=0.2, rely=0.12)


    def __config_inputs(self):
        self.__input_name = ctk.CTkEntry(self, width=id_wh, height=id_ht, placeholder_text=in_phtt, text_color=id_tc,
                                         placeholder_text_color=id_phttc, fg_color=id_fgc , font=id_ft)
        self.__input_name.place(relx=0.18, rely=0.25)

        self.__input_zone = ctk.CTkEntry(self, width=id_wh, height=id_ht, placeholder_text=iz_phtt, text_color=id_tc,
                                         placeholder_text_color=id_phttc, fg_color=id_fgc , font=id_ft)
        self.__input_zone.place(relx=0.18, rely=0.37)


    def __config_menu_btn(self):
        self.__enter_btn = ctk.CTkButton(self, width=en_wh, height=en_ht, text=en_tt, font=en_ft,
                                       text_color=en_ttc, fg_color=en_fgc)
        self.__enter_btn.place(relx=0.18, rely=0.55)
        self.__enter_btn.configure(command=self.__main_page.on_enter_click)

        self.__exit_btn = ctk.CTkButton(self, width=ex_wh, height=ex_ht, text=ex_tt, font=ex_ft,
                                          text_color=ex_ttc, fg_color=ex_fgc)
        self.__exit_btn.place(relx=0.59, rely=0.55)
        self.__exit_btn.configure(command=self.__main_page.on_exit_click)

        self.__create_btn = ctk.CTkButton(self, width=cr_wh, height=cr_ht, text=cr_tt, font=cr_ft,
                                          text_color=cr_ttc, fg_color=cr_fgc)
        self.__create_btn.place(relx=0.22, rely=0.75)
        self.__create_btn.configure(command=self.__main_page.create_button_click_handler)


    @property
    def name(self):
        return self.__input_name


    @property
    def zone(self):
        return self.__input_zone



class MainPage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.__controller = MainPageController()
        self.__create_user_page = None
        self.__config_window()
        self.__config_frame()


    def __config_window(self):
        self.geometry(geometry)
        self.title(title)
        self.resizable(rzb_wh, rzb_ht)


    def __config_frame(self):
        self.__main_frame = MainFrame(self, master=self, width=f_wh, height=f_ht)
        self.__main_frame.pack()
        self.__main_frame.pack_propagate(False)


    def on_enter_click(self):
        self.__controller.enter_button_click_handler(self.__main_frame.name.get(), self.__main_frame.zone.get())
        self.__main_frame.name.delete(0, ctk.END), self.__main_frame.zone.delete(0, ctk.END)


    def on_exit_click(self):
        self.__controller.exit_btn_click_handler()
        self.destroy()



    def create_button_click_handler(self):
        self.__controller.exit_btn_click_handler()
        self.__create_user_page = GetDataUser(self)
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


MainPage.run()