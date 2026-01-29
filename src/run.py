import customtkinter as ctk
from customtkinter import CTkImage
import tkinter.font as tkfont
from CTkToolTip import CTkToolTip

from PIL import Image
import os

import menu.menu as mb
import data.get_portfolio as dat

# ctk.set_appearance_mode("Dark")
ctk.set_appearance_mode("Light")
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

        # Font
        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(size=10)
        self.option_add("font", default_font)

if __name__ == '__main__':
    app = Launcher()
    app.mainloop()