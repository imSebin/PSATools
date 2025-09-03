from tkinter import *

class menu:
    def __init__(self, master: Tk):
        self.master = master
        self.menu_bar = Menu(self.master)

        self.filemenu = Menu(self.menu_bar, tearoff=0)
        self.add_filemenu_items(self.filemenu)
        self.menu_bar.add_cascade(label="File", menu=self.filemenu)

        self.editmenu = Menu(self.menu_bar, tearoff=0)
        self.add_editmenu_items(self.editmenu)
        self.menu_bar.add_cascade(label="Edit", menu=self.editmenu)

        self.viewmenu = Menu(self.menu_bar, tearoff=0)
        self.add_editmenu_items(self.viewmenu)
        self.menu_bar.add_cascade(label="View", menu=self.editmenu)

        self.helpmenu = Menu(self.menu_bar, tearoff=0)
        self.add_helpmenu_items(self.helpmenu)
        self.menu_bar.add_cascade(label="Help", menu=self.helpmenu)

    def get_menu_bar(self) -> Menu:
        return self.menu_bar

    def add_filemenu_items(self, filemenu: Menu):
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save As...", command=self.save_as_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)

    def add_editmenu_items(self, editmenu: Menu):
        pass

    def add_viewmenu_items(self, viewmenu: Menu):
        pass

    def add_helpmenu_items(self, helpmenu: Menu):
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