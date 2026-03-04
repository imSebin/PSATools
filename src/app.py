import os

import customtkinter as ctk
from customtkinter import CTkImage
import tkinter.font as tkfont
from CTkToolTip import CTkToolTip

from PIL import Image

import menu as mb
import data.get_portfolio as dat

class App:
    def __init__(self, master: ctk.CTk, path):
        self.master = master
        self.res_path = path + "\\res"
        self.src_path = path + "\\src"

        self.master.title("Pokemon TCG Organizer")
        self.master.geometry("1280x720")
        self.master.resizable(False, False)
        self.master.iconbitmap(self.res_path + "\sebin.ico")
        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(size=10)
        self.master.option_add("font", default_font)

        self.pokemon = "gardevoir"
        port = dat.portfolio(self.res_path)
        self.data = port.dct[self.pokemon]
        self.expansions = list(dict.fromkeys([self.data[card]['expansion'] for card in self.data.keys()]))
        self.curr_expansion = self.expansions[0]
        self.versions = [item for item in list(self.data.keys()) if self.data[item]["expansion"] == self.curr_expansion]
        self.curr_version = self.versions[0]

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=10)
        self.master.grid_rowconfigure(2, weight=3)
        self.master.grid_columnconfigure(0, weight=3)
        self.master.grid_columnconfigure(1, weight=7)
        self.master.grid_columnconfigure(2, weight=10)
        self.window()

    def window(self):
        self.menu_bar()

        # ____________ #
        # Left Section #
        # ____________ #

        pokemon_frame = ctk.CTkFrame(self.master)
        pokemon_frame.grid(row=0, column=0, padx=15, pady=5, sticky="nsew")
        ctk.CTkLabel(pokemon_frame, text=f"Pokémon TCG :: {self.pokemon.upper()}", font=("Helvetica", 18, "bold")).pack(expand=True)

        expansion_frame = ctk.CTkScrollableFrame(self.master)
        expansion_frame.grid(row=1, column=0, padx=15, pady=5, sticky="nsew")
        for expansion in self.expansions:
            text = f"{expansion}"
            e_btn = ctk.CTkButton(expansion_frame, text=f"{text}" if len(text) < 35 else f"{text[:35]}...", command=lambda t=expansion: self.change_window(t, None))
            e_btn.pack(pady=3, fill="x")
            CTkToolTip(e_btn, message=expansion)

        version_frame = ctk.CTkScrollableFrame(self.master)
        version_frame.grid(row=2, column=0, padx=15, pady=5, sticky="nsew")
        for version in self.versions:
            text = str(version).partition(" ")[2]
            v_btn = ctk.CTkButton(version_frame, text=f"{text}" if len(text) < 30 else f"{text[:30]}...", command=lambda t=version: self.change_window(None, t))
            v_btn.pack(pady=3, fill="x")
            CTkToolTip(v_btn, message=text)

        # ______________ #
        # Center Section #
        # ______________ #

        content_frame = ctk.CTkFrame(self.master, fg_color="#6D5143")
        content_frame.grid(row=0, rowspan=3, column=1, padx=15, pady=5, sticky="ew")
        raw = Image.open(f"{self.res_path}\\imgs\\cards\\282_0_0_0.jpg")
        img = CTkImage(light_image=raw, dark_image=raw, size=(320, 440)) # 8:11
        panel = ctk.CTkLabel(content_frame, image=img, text="Card")
        panel.image = img # Need to rid of bug that occurs where it makes the image reappear
        panel.pack()

        # _____________ #
        # Right Section #
        # _____________ #

        info_frame = ctk.CTkFrame(self.master)
        info_frame.grid(row=0, rowspan=3, column=2, padx=15, pady=5, sticky="nsew")
        exp = ctk.CTkTextbox(info_frame, width=350, height=2, wrap="word", font=("Helvetica", 12, "bold"), fg_color="#5A3E32")
        exp.pack(expand=True)
        exp.insert(1.0, f"Expansion: {self.curr_expansion}")
        ver = ctk.CTkTextbox(info_frame, width=350, height=2, wrap="word", font=("Helvetica", 12, "bold"), fg_color="#5A3E32")
        ver.pack(expand=True)
        ver.insert(1.0, f"Version: {self.curr_version}")

    def change_window(self, new_exp, new_ver):
        # self.cascade(self.master)
        if not new_ver:
            self.curr_expansion = new_exp
            self.versions = [item for item in list(self.data.keys()) if self.data[item]["expansion"] == self.curr_expansion]
            self.curr_version = self.versions[0]
        elif not new_exp:
            self.curr_version = new_ver
        self.window()

    def menu_bar(self):
        # Menu Bar
        menu_bar = mb.Menu(self.master)
        self.master.config(menu=menu_bar.get_menu_bar())

    @staticmethod
    def cascade(frame):
        for element in frame.winfo_children():
            element.destroy()

if __name__ == '__main__':

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme(os.getcwd() + "\\themes\\coffee.json")
    ctk_obj = ctk.CTk()

    App(ctk_obj, os.getcwd())
    ctk_obj.mainloop()

