import customtkinter as ctk

class breakpoint_handler:
    def __init__(self, master):
        self.master = master
    
    def change_ratios(self, size):
        match(size):
            case "small":
                self.master.geometry("%dx%d+%d+%d" % self.calculate_dimensions(1280, 720))        
            case "medium":
                self.master.geometry("%dx%d+%d+%d" % self.calculate_dimensions(1600, 900))
            case "large":
                self.master.geometry("%dx%d+%d+%d" % self.calculate_dimensions(2560, 1440))
    
    def calculate_dimensions(self, width, height) -> tuple[int, int, int, int]:
        w = width
        h = height
        x = (self.master.winfo_screenwidth() / 2) - (w / 2)
        y = (self.master.winfo_screenheight() / 2) - (h / 2)
        return w, h, x, y

class helper:
    def __init__(self, master):
        self.master = master
    
    def light_or_dark(self):
        return "Light" if ctk.get_appearance_mode() == "Dark" or ctk.get_appearance_mode() == "System" else "Dark"