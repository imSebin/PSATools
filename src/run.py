import customtkinter as ctk
from customtkinter import CTkImage
import tkinter.font as tkfont
from CTkToolTip import CTkToolTip

from PIL import Image
from window import window
import os

import menu.menu as mb
import data.get_portfolio as dat

ctk.set_appearance_mode("Dark")
# ctk.set_appearance_mode("Light")
ctk.set_default_color_theme(f"{os.getcwd()}/themes/coffee.json")

class Launcher(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Paths
        self.res_path = f"{os.getcwd()}/res/"
        self.src_path = f"{os.getcwd()}/src/"

        # Window
        self.title("Pokémon TCG Database")
        self.geometry(f"{1280}x{720}")
        self.resizable(False, False)
        self.iconbitmap(self.res_path + "/sebin.ico")
        self.menu_bar()

        # Font
        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(size=10)
        self.option_add("font", default_font)
    
    def menu_bar(self):
        # Menu Bar
        menu_bar = mb.Menu(self)
        self.config(menu=menu_bar.get_menu_bar())

    def main_window(self):
        window = window(self)

    def change_window(self, pokemon, version):
        pass
        # # Destroy all widgets in the window
        # for widget in self.winfo_children():
        #     widget.destroy()
        # # Recreate the App with new parameters
        # app = App(self, os.getcwd())
        # if version is None:
        #     app.curr_version = app.versions[0]
        # else:
        #     app.curr_version = version
        # app.pokemon = pokemon
        # app.data = app.data = dat.portfolio(self.res_path).dct[app.pokemon]
        # app.expansions = list(dict.fromkeys([app.data[card]['expansion'] for card in app.data.keys()]))
        # app.versions = [item for item in list(app.data.keys()) if app.data[item]["expansion"] == app.curr_expansion]
        # app.window()

if __name__ == '__main__':
    app = Launcher()
    app.mainloop()