import os
import json
import shutil
import sys
from tkinter import *
from tkinter import ttk


class app:
    def __init__(self, master: Tk, path, genre_lst):
        # Instantiate class
        self.master = master
        self.master.geometry("800x500")
        self.path = path
        self.index = 0
        self.dict_instance = self.reset_dict()
        self.genre_lst = genre_lst
        self.window1()

    def window1(self):
        # Instantiate frames
        genre_frame = LabelFrame(self.master, text="Set Genre", padx=10, pady=5)
        genre_frame.pack(padx=10, pady=10, side="right", fill="both", expand=True, anchor="w")
        filename_frame = LabelFrame(self.master, padx=10, pady=5)
        filename_frame.pack(padx=10, pady=10, side="top", anchor="w")
        title_frame = LabelFrame(self.master, text="Set Title", padx=10, pady=5)
        title_frame.pack(padx=10, pady=10, side="top", fill="y", expand=True, anchor="w")
        anchor_frame = LabelFrame(self.master, text="Set Author", padx=10, pady=5)
        anchor_frame.pack(padx=10, pady=10, side="top", fill="y", expand=True, anchor="w")
        status_frame = LabelFrame(self.master, text="Set Status", padx=10, pady=5)
        status_frame.pack(padx=10, pady=10, side="top", fill="y", expand=True, anchor="w")

        # Check if there already exists details.json
        if os.path.exists(self.path + str(os.listdir(self.path)[self.index]) + "/details.json"):
            with open(self.path + str(os.listdir(self.path)[self.index]) + "/details.json") as infile:
                self.dict_instance = json.load(infile)
        else:
            self.dict_instance = self.reset_dict()

        # Filename
        ttk.Label(filename_frame, text="Current Filename: " + os.listdir(self.path)[self.index]).pack(anchor="w")
        filename_entry = ttk.Entry(filename_frame, width=30)
        filename_entry.pack(anchor="w")
        def file_btn():
            if filename_entry.get() in os.listdir(self.path):
                self.index = os.listdir(self.path).index(filename_entry.get())
                for element in self.master.winfo_children():
                    element.destroy()
                self.window1()
            else:
                pass
        ttk.Button(filename_frame, text="Go to file", command=file_btn).pack(anchor="w")

        # Title
        title_label = ttk.Label(title_frame, text="Title: " + self.dict_instance["title"], width=30)
        title_label.pack(anchor="w")
        title_entry = ttk.Entry(title_frame, width=30)
        title_entry.pack(anchor="w")
        def title_btn():
            self.dict_instance.update({"title": title_entry.get()})
            title_label.config(text="Title: " + self.dict_instance["title"])
        ttk.Button(title_frame, text="Set Title", command=title_btn).pack(anchor="w")

        # Author
        author_label = ttk.Label(anchor_frame, text="Author: " + self.dict_instance["author"])
        author_label.pack(anchor="w")
        author_entry = ttk.Entry(anchor_frame)
        author_entry.pack(anchor="w")
        def author_btn():
            self.dict_instance.update({"author": author_entry.get()})
            author_label.config(text="Author: " + self.dict_instance["author"])
        ttk.Button(anchor_frame, text="Set Author", command=author_btn).pack(anchor="w")

        # Status
        status_label = ttk.Label(status_frame, text="Status: " + self.dict_instance["status"])
        status_label.pack(anchor="w")
        def status_btn0():
            self.dict_instance.update({"status": str(0)})
            status_label.config(text="Status: " + self.dict_instance["status"])
        def status_btn1():
            self.dict_instance.update({"status": str(1)})
            status_label.config(text="Status: " + self.dict_instance["status"])
        def status_btn2():
            self.dict_instance.update({"status": str(2)})
            status_label.config(text="Status: " + self.dict_instance["status"])
        ttk.Button(status_frame, text="Unknown", command=status_btn0).pack()
        ttk.Button(status_frame, text="Ongoing", command=status_btn1).pack()
        ttk.Button(status_frame, text="Completed", command=status_btn2).pack()

        # Genre/Tags
        genre_label = ttk.Label(genre_frame, text="Genre: " + str(self.dict_instance["genre"])[:80] +
                                                  "\n" + str(self.dict_instance["genre"])[80:])
        genre_label.pack(anchor="w")
        genre_frame1 = LabelFrame(genre_frame)
        genre_frame1.pack(side="left", anchor="w")
        genre_frame2 = LabelFrame(genre_frame)
        genre_frame2.pack(side="left", anchor="w")
        genre_frame3 = LabelFrame(genre_frame)
        genre_frame3.pack(side="left", anchor="w")
        genre_frame4 = LabelFrame(genre_frame)
        genre_frame4.pack(side="left", anchor="w")
        checks = []
        count = 0
        for genre in self.genre_lst:
            count += 1
            bool1 = BooleanVar()
            if count < 16:
                c = Checkbutton(genre_frame1, text=genre, variable=bool1)
                c.pack(anchor="w")
                checks.append([bool1, c])
            elif count < 31:
                c = Checkbutton(genre_frame2, text=genre, variable=bool1)
                c.pack(anchor="w")
                checks.append([bool1, c])
            elif count < 46:
                c = Checkbutton(genre_frame3, text=genre, variable=bool1)
                c.pack(anchor="w")
                checks.append([bool1, c])
            elif count < 56:
                c = Checkbutton(genre_frame4, text=genre, variable=bool1)
                c.pack(anchor="w")
                checks.append([bool1, c])
        def genre_btn():
            checked = []
            for checklist in checks:
                if checklist[0].get():
                    checked.append(checklist[1].cget("text"))
            self.dict_instance.update({"genre": checked})
            genre_label.config(text="Genre: " + str(self.dict_instance["genre"])[:80] +
                                    "\n" + str(self.dict_instance["genre"])[80:])
        ttk.Button(genre_frame, text="Set genre", command=genre_btn).pack(pady=(250, 0), anchor="se")

        ttk.Button(genre_frame, text="Download JSON", command=self.create_json).pack(pady=(30, 0), anchor="se")

        ttk.Button(genre_frame, text="Previous: " + str(os.listdir(self.path)[self.index - 1]) if self.index >= 1 else "EOF",
                   command=self.prev).pack(pady=(10, 0), anchor="se")
        ttk.Button(genre_frame, text="Next: " + str(os.listdir(self.path)[self.index + 1]) if self.index <= len(os.listdir(self.path)) else "EOF",
                   command=self.next).pack(anchor="se")

    def prev(self):
        if self.index - 1 < 0:
            pass
        else:
            self.index -= 1
            for element in self.master.winfo_children():
                element.destroy()
            self.window1()

    def next(self):
        if self.index + 1 >= len(os.listdir(self.path)):
            pass
        else:
            self.index += 1
            for element in self.master.winfo_children():
                element.destroy()
            self.window1()

    def reset_dict(self):
        ndict = {
            "title": os.listdir(self.path)[self.index],
            "author": "",
            "artist": "",
            "description": "",
            "genre": [],
            "status": "2",
            "_status values": ["0 = Unknown", "1 = Ongoing", "2 = Completed", "3 = Licensed"]
        }
        return ndict

    def create_json(self):
        with open(self.path + str(os.listdir(self.path)[self.index]) + "/details.json", "w") as outfile:
            json.dump(self.dict_instance, outfile)

    def window2(self):
        pass


if __name__ == '__main__':
    import_path = 'C:/Users/sebin/PycharmProjects/TachiyomiFileCleaner/Final1 Tachiyomi JSON/'
    lst = ['Analphagia', 'Beastiality', 'Birth', 'Bondage', 'Brother', 'Crossdressing', 'Cumflation', 'Cunnilingus',
           'Exhibitionism', 'Femdom', 'Fingering', 'Futanari', 'Harem', 'Incest', 'Insertion', 'Leglock', 'Lolicon',
           'Mother', 'Oyakodon', 'Pregnant', 'Rape_F', 'Rape_M', 'Royalty', 'Scat', 'School', 'Shotacon', 'Sister',
           'Teacher', 'Throatpie', 'Unbirth', 'X-ray', 'Yaoi', 'Agata', 'Fuyuno_Mikan', 'Mizuryu_Kei', 'Nyuu',
           'Quzilax', 'Case_Closed', 'Genshin_Impact', 'League_Of_Legends', 'Negi_Sensei', 'One_Piece', 'Overwatch',
           'Shingeki_No_Kyojin', 'Shokugeki_No_Soma']
    root = Tk()
    app(root, import_path, lst)
    root.mainloop()
