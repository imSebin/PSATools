import customtkinter as ctk
from CTkMenuBar import *

import os

class Menu:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.menu = CTkTitleMenu(self.master)
        self.menu.x_offset = self.menu.x_offset + 25

        self.filemenu = self.menu.add_cascade("File")
        self.editmenu = self.menu.add_cascade("Edit")
        self.viewmenu = self.menu.add_cascade("View")
        self.helpmenu = self.menu.add_cascade("Help")

        self.add_filemenu_dropdown(self.filemenu)
        # self.add_editmenu_dropdown(self.editmenu)
        self.add_viewmenu_dropdown(self.viewmenu)
        # self.add_helpmenu_dropdown(self.helpmenu)
    
    def add_filemenu_dropdown(self, filemenu):
        dropdown = CustomDropdownMenu(widget=filemenu)
        dropdown.add_option(option="New")
        dropdown.add_option(option="Open")
        dropdown.add_option(option="Save")
        dropdown.add_option(option="Export")
        dropdown.add_option(option="Exit", command=lambda: self.master.quit())

    def add_viewmenu_dropdown(self, viewmenu):
        dropdown = CustomDropdownMenu(widget=viewmenu)
        screen_size_subdropdown = dropdown.add_submenu("Change Resolution")
        screen_size_subdropdown.add_option(option="1280 x 720", 
                                           command=lambda: self.master.breakpoint_handler.change_ratios("small"))
        screen_size_subdropdown.add_option(option="1600 x 900", 
                                           command=lambda: self.master.breakpoint_handler.change_ratios("medium"))
        screen_size_subdropdown.add_option(option="2560 x 1440", 
                                           command=lambda: self.master.breakpoint_handler.change_ratios("large"))
        dropdown.add_option(option="Light/Dark Mode Toggle", 
                            command=lambda: ctk.set_appearance_mode(self.master.helper.light_or_dark()))
        theme_select_subdropdown = dropdown.add_submenu("Change Theme")
        for theme in os.listdir(f"{self.master.res_path}themes/"):
            theme_select_subdropdown.add_option(option=theme[:-5].capitalize(), 
                                                command=lambda t=theme: self.master.change_theme(t))

