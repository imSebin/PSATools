import tkinter as tk
from tkinter import *

class Menu:
    def __init__(self, master: Tk):
        self.master = master
        self.menu_bar = tk.Menu(self.master)

        self.filemenu = tk.Menu(self.menu_bar, tearoff=0)
        self.add_filemenu_items(self.filemenu)
        self.menu_bar.add_cascade(label="File", menu=self.filemenu)

        self.editmenu = tk.Menu(self.menu_bar, tearoff=0)
        self.add_editmenu_items(self.editmenu)
        self.menu_bar.add_cascade(label="Edit", menu=self.editmenu)

        self.viewmenu = tk.Menu(self.menu_bar, tearoff=0)
        self.add_editmenu_items(self.viewmenu)
        self.menu_bar.add_cascade(label="View", menu=self.editmenu)

        self.helpmenu = tk.Menu(self.menu_bar, tearoff=0)
        self.add_helpmenu_items(self.helpmenu)
        self.menu_bar.add_cascade(label="Help", menu=self.helpmenu)

    def get_menu_bar(self) -> tk.Menu:
        return self.menu_bar

    def add_filemenu_items(self, filemenu: tk.Menu):
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save As...", command=self.save_as_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)

    def add_editmenu_items(self, editmenu: tk.Menu):
        pass

    def add_viewmenu_items(self, viewmenu: tk.Menu):
        pass

    def add_helpmenu_items(self, helpmenu: tk.Menu):
        pass

    @staticmethod
    def new_file():
        print("New File")

    @staticmethod
    def open_file():
        print("Open File")

    @staticmethod
    def save_file():
        print("Save File")

    @staticmethod
    def save_as_file():
        print("Save As File")