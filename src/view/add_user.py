from __future__ import annotations

import customtkinter as ctk
from src.view.config_view import *
from src.model.model import *

class CreateUserFrame(ctk.CTkFrame):

    def __init__(self, main_page: GetDataUser, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_page = main_page
        self.__main_label = None
        self.__input_name = None
        self.__input_zone = None
        self.__config_label()
        self.__config_inputs()
        self.__config_menu_btn()

    def __config_label(self):
        self.__add_user = ctk.CTkLabel(self, text=au_tt, text_color=au_ttc, font=au_ft)
        self.__add_user.place(relx=0.20, rely=0.15)

    def __config_inputs(self):
        self.__input_name = ctk.CTkEntry(self, width=i_wh, height=i_ht, placeholder_text=in_phtt_cu,
                                         placeholder_text_color=i_phttc, fg_color=i_fgc, font=i_ft)
        self.__input_name.place(relx=0.18, rely=0.25)

        self.__input_zone = ctk.CTkEntry(self, width=i_wh, height=i_ht, placeholder_text=iz_phtt_cu,
                                         placeholder_text_color=i_phttc, fg_color=i_fgc, font=i_ft)
        self.__input_zone.place(relx=0.18, rely=0.37)

    def __config_menu_btn(self):
        self.__add_btn = ctk.CTkButton(self, width=ad_wh, height=ad_ht, text=ad_tt, font=ad_ft,
                                         text_color=ad_ttc, fg_color=ad_fgc)
        self.__add_btn.place(relx=0.18, rely=0.55)
        self.__add_btn.configure(command=self.__main_page.add_btn_click_handler)

        self.__del_btn = ctk.CTkButton(self, width=d_wh, height=d_ht, text=d_tt, font=d_ft,
                                        text_color=d_ttc, fg_color=d_fgc)
        self.__del_btn.place(relx=0.59, rely=0.55)
        self.__del_btn.configure()

        self.__save_btn = ctk.CTkButton(self, width=s_wh, height=s_ht, text=s_tt, font=s_ft,
                                          text_color=s_ttc, fg_color=s_fgc)
        self.__save_btn.place(relx=0.22, rely=0.7)
        self.__save_btn.configure(command=self.__main_page.cancel_button_click_handler)

        self.__cancel_btn = ctk.CTkButton(self, width=c_wh, height=c_ht, text=c_tt, font=c_ft,
                                          text_color=c_ttc, fg_color=c_fgc)
        self.__cancel_btn.place(relx=0.22, rely=0.82)
        self.__cancel_btn.configure(command=self.__main_page.cancel_button_click_handler)

    @property
    def name(self):
        return self.__input_name.get()


    @property
    def zone(self):
        return self.__input_zone.get()



class GetDataUser(ctk.CTkToplevel):

    def __init__(self, main_window):
        super().__init__()
        self.__main_window = main_window
        self.__user = None
        self.__main_frame = None
        self.__main_window.protocol("WM_DELETE_WINDOW", self.__main_window.on_exit_click)
        self.__config_window()
        self.__config_frame()


    def __config_window(self):
        self.geometry(gt)
        self.title(ttl)
        self.resizable(rz_wh, rz_ht)


    def __config_frame(self):
        self.__main_frame = CreateUserFrame(self, master=self, width=fr_wh, height=fr_ht)
        self.__main_frame.pack()
        self.__main_frame.pack_propagate(False)


    def add_btn_click_handler(self):
        self.__user = User(self.__main_frame.name, self.__main_frame.zone)
        self.__user.add_access_zone()


    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        self.__main_window.deiconify()

        self.destroy()


