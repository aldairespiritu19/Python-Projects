
## Python Ver: 3.9.6


## Author:     Aldair Espiritu


## Purpose:    Create a user interface that allows user to input text
##             and opens the html file with the input text in a web browser.
           






from tkinter import *
import tkinter as tk
import webpage_generator_gui
import webpage_generator_func


# Create user window
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self, master, *args, **kwargs)


        # Frame height and width
        self.master = master
        self.master.minsize(350, 100)
        self.master.maxsize(350, 100)

        # Title
        self.master.title("Webpage Generator")

        self.master.configure(bg="#F0F0F0")

        webpage_generator_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk() 
    App = ParentWindow(root) 
    root.mainloop()
