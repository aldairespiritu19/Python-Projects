
## Python Ver: 3.9.6


## Author:     Aldair Espiritu



## Purpose:    Create a GUI that allows the user to browse through folders
##             and allows the user to manually initiate the file check.





from tkinter import *
import tkinter as tk
from tkinter import filedialog
import shutil
import os
import datetime

import file_transfer_gui
import file_transfer_func

# Create user window
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Frame height and width
        self.master = master
        self.master.minsize(500, 300)
        self.master.maxsize(500, 300)

        # Title
        self.master.title("File Transfer System")

        self.master.configure(bg="#F0F0F0")

        file_transfer_gui.load_gui(self)





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root) 
    root.mainloop() 
