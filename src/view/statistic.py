import customtkinter as ctk
from settings.config_statistic import *

class Scroll(ctk.CTkScrollableFrame):
    def __init__(self, main_page, *args, **kwargs):
        super().__init__(main_page, *args, **kwargs)
        self.__main_page = main_page
        self.__text = None
        self.__label_text = None
        self.__config_text()


    def __config_text(self) -> None:
        self.__label_text = ctk.CTkLabel(self, text=self.__text, text_color=s_ltc, font=s_lft)
        self.__label_text.grid(row=1, column=1, padx=10, pady=10)


    @property
    def text(self):
        return self.__text


    @text.setter
    def text(self, val):
        self.__text = val



class Statistic(ctk.CTkToplevel):
    def __init__(self, main_window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window
        self.__scroll = None
        self.__config_scroll()
        self.__config_window()
        self.__config_btn()


    def __config_window(self):
        self.geometry(geometry)
        self.title(title)
        self.resizable(rzb_wh, rzb_ht)


    def __config_scroll(self):
        self.__scroll = Scroll(self, width=s_wh, height=s_ht, fg_color=s_fgc)
        self.__scroll.pack()


    def __config_btn(self):
        self.__cancel_btn = ctk.CTkButton(self, width=250, height=40, fg_color=cb_fgc, text_color=cb_ttc, text=cb_tt, font=cb_ft)
        self.__cancel_btn.place(relx=0.32, rely=0.85)
        self.__cancel_btn.configure(command=self.on_cancel_click)


    def on_cancel_click(self):
        self.__main_window.deiconify()
        self.destroy()

        
    @property
    def scroll(self):
        return self.__scroll