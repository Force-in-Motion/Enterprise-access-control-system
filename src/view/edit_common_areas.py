from __future__ import annotations

import customtkinter as ctk

from src.controller.controller import CommonAreasController
from service.process import Processing
from settings.config_edit_common_areas import *


class EditCommonAreasFrame(ctk.CTkFrame):

    def __init__(self, main_page: EditCommonAreas, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_page = main_page
        self.__main_label = None
        self.__input_zone = None
        self.__config_label()
        self.__config_inputs()
        self.__config_menu_btn()


    def __config_label(self):
        self.__edit_zone = ctk.CTkLabel(self, text=au_tt, text_color=au_ttc, font=au_ft)
        self.__edit_zone.place(relx=0.15, rely=0.12)


    def __config_inputs(self):
        self.__input_zone = ctk.CTkEntry(self, width=iz_wh, height=iz_ht, placeholder_text=in_phtt_cu, text_color=iz_tc,
                                         placeholder_text_color=iz_phttc, fg_color=iz_fgc, font=iz_ft)
        self.__input_zone.place(relx=0.18, rely=0.27)


    def __config_menu_btn(self):
        self.__add_zone_btn = ctk.CTkButton(self, width=az_wh, height=az_ht, text=az_tt, font=az_ft,
                                         text_color=az_ttc, fg_color=az_fgc)
        self.__add_zone_btn.place(relx=0.19, rely=0.45)
        self.__add_zone_btn.configure(command=self.__main_page.on_add_click)

        self.__del_zone_btn = ctk.CTkButton(self, width=dz_wh, height=dz_ht, text=dz_tt, font=dz_ft,
                                        text_color=dz_ttc, fg_color=dz_fgc)
        self.__del_zone_btn.place(relx=0.59, rely=0.45)
        self.__del_zone_btn.configure(command=self.__main_page.on_del_click)

        self.__save_btn = ctk.CTkButton(self, width=s_wh, height=s_ht, text=s_tt, font=s_ft,
                                          text_color=s_ttc, fg_color=s_fgc)
        self.__save_btn.place(relx=0.22, rely=0.65)
        self.__save_btn.configure(command=self.__main_page.on_save_click)

        self.__cancel_btn = ctk.CTkButton(self, width=c_wh, height=c_ht, text=c_tt, font=c_ft,
                                          text_color=c_ttc, fg_color=c_fgc)
        self.__cancel_btn.place(relx=0.22, rely=0.78)
        self.__cancel_btn.configure(command=self.__main_page.on_cancel_click)


    @property
    def zone(self):
        return self.__input_zone



class EditCommonAreas(ctk.CTkToplevel):

    def __init__(self, main_window):
        super().__init__()
        self.__main_window = main_window
        self.__main_frame = None
        self.__controller = CommonAreasController()
        self.protocol("WM_DELETE_WINDOW", Processing.on_close)
        self.__config_window()
        self.__config_frame()


    def __config_window(self):
        self.geometry(gt)
        self.title(ttl)
        self.resizable(rz_wh, rz_ht)


    def __config_frame(self):
        self.__main_frame = EditCommonAreasFrame(self, master=self, width=fr_wh, height=fr_ht)
        self.__main_frame.pack()
        self.__main_frame.pack_propagate(False)


    def on_add_click(self):
        self.__controller.add_button_click_handler(self.__main_frame.zone.get())
        self.__main_frame.zone.delete(0, ctk.END)


    def on_del_click(self):
        self.__controller.del_button_click_handler(self.__main_frame.zone.get())
        self.__main_frame.zone.delete(0, ctk.END)


    def on_save_click(self):
        self.__controller.save_button_click_handler()


    def on_cancel_click(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        self.__main_window.deiconify()

        self.destroy()


