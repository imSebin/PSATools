from tkinter import ttk
import customtkinter as ctk
import tkinter.font as tkfont
from customtkinter import CTkImage
from CTkToolTip import CTkToolTip

from PIL import Image
from window import window
import os

import helper as hp
import menu as mb
import data.get_portfolio as dat

# Customtkinter Configuration
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme(f"{os.getcwd()}/res/themes/coffee.json")


class Launcher(ctk.CTk):
    def __init__(self):
        # Instantiation
        super().__init__()
        self.helper = hp.helper(self)
        self.breakpoint_handler = hp.breakpoint_handler(self)
    
        # Paths
        self.res_path = f"{os.getcwd()}/res/"
        self.src_path = f"{os.getcwd()}/src/"
        
        # Window
        self.title("Pokémon TCG Database")
        self.menu_bar = mb.Menu(self)
        self.breakpoint_handler.change_ratios("medium")
        self.resizable(False, False)
        self.iconbitmap(f"{self.res_path}sebin.ico")
        self.side_bar()
        self.main_window()

        # Keybinds
        self.bind('<Escape>', lambda e: self.quit())

        # Font
        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(size=10)
        self.option_add("font", default_font)
    
    def side_bar(self):
        side_bar = ctk.CTkFrame(self)
        side_bar.pack(side="left", fill="y")
        side_bar.pack_propagate(False)
        side_bar.configure(width=250)

    def main_window(self):
        win = window()

    def change_window(self):
        pass
    
    def change_theme(self, theme):
        """Change the theme and rebuild UI"""
        ctk.set_default_color_theme(f"{self.res_path}themes/{theme}")
        fg_color = ctk.ThemeManager.theme["CTk"]["fg_color"]
        self.configure(fg_color=fg_color)
        for widget in self.winfo_children():
            widget.destroy()
        self.menu_bar = mb.Menu(self)
        self.side_bar()
        self.main_window()

if __name__ == '__main__':
    app = Launcher()
    app.mainloop()