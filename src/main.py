from locale import windows_locale

import requests
import json
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

TOKEN = ""


class app:
    def __init__(self, master: Tk, path):
        self.master = master
        self.master.geometry("1000x800")
        self.path = path
        self.portfolio = self.get_portfolio()
        self.index = ["gardevoir", "2003", "base"]
        self.curr_release_lst = self.portfolio.get(self.index[0])[0].get(self.index[1])
        for i, dct in enumerate(self.curr_release_lst):
            if self.index[2] in dct.keys():
                self.curr_expansion = dct
                break
        self.curr = self.curr_expansion[self.index[2]]
        self.portfolio_window()

    def portfolio_window(self):
        # Instantiate frames
        image_frame = LabelFrame(self.master, text="Card Description", padx=10, pady=10)
        image_frame.pack(padx=10, pady=10, side="right", fill="both", expand=True)
        pokemon_name_frame = LabelFrame(self.master, padx=10, pady=5)
        pokemon_name_frame.pack(padx=10, pady=10, side="top", fill="x")
        selection_frame = LabelFrame(self.master, text="Selection & Categories", padx=10, pady=5)
        selection_frame.pack(padx=10, pady=10, side="top", fill="both", expand=True)
        sub_selection_frame = LabelFrame(self.master, text="Sub-selection", padx=10, pady=5)
        sub_selection_frame.pack(padx=10, pady=10, side="top", fill="both", expand=True)
        tool_frame = LabelFrame(self.master, text="Tools", padx=10, pady=5)
        tool_frame.pack(padx=10, pady=10, side="left", fill="x")

        # Image
        raw = Image.open("C:/Users/sebin/PycharmProjects/PSATools/res/imgs/" + str(self.curr.get("img")))
        raw = raw.resize((320, 440)) # 8:11
        img = ImageTk.PhotoImage(raw)
        panel = tk.Label(image_frame, image=img)
        panel.image = img
        panel.pack(side="top", pady=30)

        # if not self.curr["cert_number"] == "N/A":
        #     self.curr["psa_10_pop"] = str(get_by_cert(int(self.curr["cert_number"]))["PSACert"]["TotalPopulation"])

        image_label_1 = ttk.Label(image_frame, text="Year: " + self.curr["released"], font="Helvetica 12 bold")
        image_label_2 = ttk.Label(image_frame, text="Expansion: " + self.curr["expansion"], font="Helvetica 12 bold")
        image_label_3 = ttk.Label(image_frame, text="Number: " + self.curr["number"], font="Helvetica 12 bold")
        image_label_4 = ttk.Label(image_frame, text="PSA 10 Population: " + self.curr["psa_10_pop"], font="Helvetica 12 bold")
        image_label_5 = ttk.Label(image_frame, text="Obtained: " + self.curr["obtained"], font="Helvetica 12 bold")
        image_label_6 = ttk.Label(image_frame, text="Cert Number: " + self.curr["cert_number"], font="Helvetica 12 bold")
        image_label_1.pack(anchor="center")
        image_label_2.pack(anchor="center")
        image_label_3.pack(anchor="center")
        image_label_4.pack(anchor="center")
        image_label_5.pack(anchor="center")
        image_label_6.pack(anchor="center")

        # Collection Name
        ttk.Label(pokemon_name_frame, text="Collection: " + self.index[0].title()).pack(anchor="w")

        # Selection
        selection_label = ttk.Label(selection_frame, text="By Artwork")
        selection_label.pack(anchor="w")

        #TODO: CHANGE JSON FORMAT
    

        # Sub-selection
        sub_selection_label = ttk.Label(sub_selection_frame, text="By Versions of Same Artwork")
        sub_selection_label.pack(anchor="w")

        # Tools/Change Attributes
        tool_obtained_frame = LabelFrame(tool_frame)
        tool_obtained_frame.pack(padx=5, pady=5, fill="x")
        tool_obtained_label = ttk.Label(tool_obtained_frame, text="Obtained: " + str(self.curr["obtained"]))
        tool_obtained_label.pack(anchor="w")
        def obtained_btn():
            self.curr.update({"obtained": "True"})
            tool_obtained_label.config(text="Obtained: " + str(self.curr["obtained"]))
        ttk.Button(tool_obtained_frame, text="Obtained", command=obtained_btn).pack(side="left")
        def not_obtained_btn():
            self.curr.update({"obtained": "False"})
            tool_obtained_label.config(text="Obtained: " + str(self.curr["obtained"]))
        ttk.Button(tool_obtained_frame, text="Not Obtained", command=not_obtained_btn).pack(side="left")

        tool_alternate_frame = LabelFrame(tool_frame)
        tool_alternate_frame.pack(padx=5, pady=5, fill="x")
        tool_alternate_label = ttk.Label(tool_alternate_frame, text="Alternate: " + str(self.curr["alternate"]))
        tool_alternate_label.pack(anchor="w")
        def alternate_btn():
            self.curr.update({"alternate": "True"})
            tool_alternate_label.config(text="Alternate: " + str(self.curr["alternate"]))
        ttk.Button(tool_alternate_frame, text="Alternate", command=alternate_btn).pack(side="left")
        def not_alternate_btn():
            self.curr.update({"alternate": "False"})
            tool_alternate_label.config(text="Alternate: " + str(self.curr["alternate"]))
        ttk.Button(tool_alternate_frame, text="Not Alternate", command=not_alternate_btn).pack(side="left")

        tool_authenticator_frame = LabelFrame(tool_frame)
        tool_authenticator_frame.pack(padx=5, pady=5, fill="x")
        tool_authenticator_label = ttk.Label(tool_authenticator_frame, text="Authenticator: " + self.curr['authenticator'])
        tool_authenticator_label.pack(anchor="w")
        tool_authenticator_entry = ttk.Entry(tool_authenticator_frame)
        tool_authenticator_entry.pack(anchor="w")
        def authenticator_btn():
            self.curr.update({"authenticator": tool_authenticator_entry.get().upper()})
            tool_authenticator_label.config(text="Authenticator: " + self.curr["authenticator"])
        ttk.Button(tool_authenticator_frame, text="Set Authenticator", command=authenticator_btn).pack(anchor="w")

    # Load saved collection portfolio
    def get_portfolio(self):
        with open(self.path) as infile:
            return json.load(infile)

    # Save collection portfolio to portfolio.JSON
    def save_portfolio(self):
        with open(self.path) as outfile:
            json.dump(self.portfolio, outfile)

    # Open new window to add a variety to curr
    def create_window(self):
        win = ttk.LabelFrame(self.master)


def create_default_page(name: str):
    dct = {
        name: {
            "category": "TCG Cards",
            "expansion": "Pokemon",
            "language": "English",
            "released": "",
            "number": "",
            "type": "Psychic",
            "rarity": "Rare Holo",
            "psa_10_pop": "0",
            "cert_number": "",
            "obtained": "True",
            "alternate": "False",
            "authenticator": "PSA",
            "grade": "10",
            "img": ""
        }
    }
    return dct


def cascade(frame):
    for element in frame.winfo_children():
        element.destroy()


def get_by_cert(cert_num):
    response = requests.get("https://api.psacard.com/publicapi/cert/GetByCertNumber/" + str(cert_num),
                            headers={'Authorization': "bearer " + TOKEN})
    d = response.json()
    return d


def get_image_by_cert(cert_num):
    response = requests.get("https://api.psacard.com/publicapi/cert/GetImagesByCertNumber/" + str(cert_num),
                            headers={'Authorization': "bearer " + TOKEN})
    d = response.json()
    return d


if __name__ == '__main__':
    portfolio_path = 'C:/Users/sebin/PycharmProjects/PSARepo/portfolio.json'
    root = Tk()
    app(root, portfolio_path)
    root.mainloop()
    # returned_info = get_by_cert(25032566)
    # beaut = json.dumps(returned_info, indent=4, sort_keys=True)
    # print(returned_info)

